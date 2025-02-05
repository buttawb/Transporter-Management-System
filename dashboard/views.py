import calendar
from datetime import date, datetime
from io import BytesIO
from PIL import Image

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from dashboard.models import (
    Company,
    VehicleMaker,
    VehicleOwner,
    Vehicle,
    Location,
    Driver,
    UserImage,
    AnnualTraining,
    AnnualDrill,
    AnnualDrillDriver,
    AnnualTrainingDriver,
    Violation,
    DriverViolation,
    ToolBoxMeetingTopic,
    DriverToolBoxMeetingAttended
)


# -----------------------------------------------------------
# Driver Training & Drill Views
# -----------------------------------------------------------

@transaction.atomic
def add_driver_training(request, driver_id):
    """
    Adds or updates a specific training & drill date for a given driver.
    """
    driver = get_object_or_404(Driver, id=driver_id)
    drills = AnnualDrill.objects.all()
    training = AnnualTraining.objects.all()

    try:
        if request.method == 'POST':
            training_id = request.POST.get('training_id')
            drill_id = request.POST.get('drill_id')
            date_val = request.POST.get('completion_date')

            traing = AnnualTraining.objects.get(id=training_id)
            drilling = AnnualDrill.objects.get(id=drill_id)

            # Example: 'train1_completed_date' for AnnualTrainingDriver
            training_no = f"train{traing.id}_completed_date"
            meeting_train, created_train = AnnualTrainingDriver.objects.get_or_create(
                driver=driver, defaults={training_no: date_val}
            )
            if not created_train:
                # We already have an entry. Just update the relevant training date field
                setattr(meeting_train, training_no, date_val)
                meeting_train.save()

            # Similarly for the drill
            drilling_no = f"train{drilling.id}_completed_date"
            meeting_drill, created_drill = AnnualDrillDriver.objects.get_or_create(
                driver=driver, defaults={drilling_no: date_val}
            )
            if not created_drill:
                setattr(meeting_drill, drilling_no, date_val)
                meeting_drill.save()

            driver_view_url = reverse('driverview', args=[driver_id])
            return HttpResponseRedirect(driver_view_url)

        else:
            context = {'driver': driver, 'drills': drills, 'training': training}
            return render(request, 'training/add_training.html', context)

    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/')


@transaction.atomic
def add_tbm(request, driver_id):
    """
    Increments the times a given driver has attended a specific Toolbox Meeting.
    """
    driver = get_object_or_404(Driver, id=driver_id)
    tbms = ToolBoxMeetingTopic.objects.all()

    if request.method == 'POST':
        meeting_topic_id = request.POST.get('meeting_topic')
        meeting_topic = get_object_or_404(ToolBoxMeetingTopic, id=meeting_topic_id)

        existing_record = DriverToolBoxMeetingAttended.objects.filter(
            driver=driver,
            meeting_topic=meeting_topic
        ).first()

        if existing_record:
            existing_record.attendance_count += 1
            existing_record.save()
        else:
            DriverToolBoxMeetingAttended.objects.create(
                driver=driver,
                meeting_topic=meeting_topic,
                attendance_count=1
            )

        return redirect('driverview', driver_id=driver.id)

    context = {
        'driver': driver,
        'tbms': tbms,
    }
    return render(request, 'tbm/add_tbm.html', context)


@transaction.atomic
def add_driver_violation(request, D_ID):
    """
    Adds a violation record for a given driver.
    """
    driver = get_object_or_404(Driver, id=D_ID)
    violation_list = Violation.objects.all()
    try:
        if request.method == 'POST':
            violation_type = request.POST.get('violationType')
            violation_obj = Violation.objects.get(violation_type=violation_type)

            violation_date = request.POST.get('violationDate')
            details = request.POST.get('details')

            driver_violation = DriverViolation(
                driver=driver,
                violation=violation_obj,
                violation_date=violation_date,
                violation_notes=details
            )
            driver_violation.save()

            driver_view_url = reverse('driverview', args=[D_ID])
            return HttpResponseRedirect(driver_view_url)

        else:
            context = {'driver': driver, 'violations': violation_list}
            return render(request, 'violation/add_driver_violation.html', context)

    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/')


# -----------------------------------------------------------
# Company CRUD
# -----------------------------------------------------------

@transaction.atomic
def delete_company(request, company_id):
    """
    Deletes a Company by ID.
    """
    entry = get_object_or_404(Company, id=company_id)
    entry.delete()
    return redirect('/company')


@transaction.atomic
def add_company(request):
    """
    Creates a new Company record using the add_company.html template.
    """
    # Optional: restrict to superuser
    if not request.user.is_superuser:
        # or handle this differently as needed
        logout(request)
        return render(request, 'user/login.html', {
            'error_head': "You do not have authority to perform this operation.",
            'log': 'Log In with Full Access Account.'
        })

    if request.method == 'POST':
        # Creating a new Company
        abbreviation = request.POST.get('abbreviation')
        name = request.POST.get('name')

        Company.objects.create(
            abbreviation=abbreviation,
            name=name
        )
        return redirect('/company')  # or wherever you list companies

    else:
        # Render the form with an empty company context
        context = {
            'action': "Add",
            'company': None
        }
        return render(request, 'company/add_company.html', context)


@transaction.atomic
def edit_company(request, company_id):
    """
    Edits an existing Company by ID.
    """
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {
            'error_head': "You do not have the authority to perform this operation.",
            'log': 'Log In with Full Access Account.'
        })

    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        company.abbreviation = request.POST.get('abbreviation')
        company.name = request.POST.get('name')
        company.save()
        return redirect('/company')

    else:
        context = {
            'action': "Edit",
            'company': company
        }
        return render(request, 'company/add_company.html', context)


# -----------------------------------------------------------
# VehicleMaker CRUD
# -----------------------------------------------------------

@transaction.atomic
def add_maker(request):
    """
    Adds a new VehicleMaker.
    """
    try:
        if request.method == 'POST':
            vehicle = VehicleMaker()
            vehicle.name = request.POST.get('maker')
            vehicle.save()
            return HttpResponseRedirect('/makers')
        else:
            return render(request, 'vehicle_maker/add_vm.html', {'action': "Add"})
    except Exception:
        return HttpResponseRedirect('/makers')


@transaction.atomic
def edit_maker(request, maker_id):
    """
    Edits an existing VehicleMaker by ID.
    """
    maker = get_object_or_404(VehicleMaker, id=maker_id)
    try:
        if request.method == 'POST':
            maker.name = request.POST.get('maker')
            maker.save()
            return HttpResponseRedirect('/makers')
    except Exception:
        return HttpResponseRedirect('/makers')

    return render(request, 'vehicle_maker/add_vm.html', {'maker': maker, 'action': "Edit"})


@transaction.atomic
def delete_maker(request, maker_id):
    """
    Deletes a VehicleMaker by ID.
    """
    try:
        maker = get_object_or_404(VehicleMaker, id=maker_id)
        maker.delete()
        return HttpResponseRedirect('/makers')
    except Exception:
        return HttpResponseRedirect('/makers')


# -----------------------------------------------------------
# VehicleOwner CRUD
# -----------------------------------------------------------

@transaction.atomic
def add_owner(request):
    """
    Adds a new VehicleOwner.
    """
    try:
        if request.method == 'POST':
            owner = VehicleOwner()
            vowner = request.POST.get('vowner')
            owner.name = vowner
            owner.save()
            return HttpResponseRedirect('/owners')
        else:
            return render(request, 'vehicle_owner/add_vo.html', {'action': "Add"})
    except Exception:
        return HttpResponseRedirect('/owners')


@transaction.atomic
def edit_owner(request, owner_id):
    """
    Edits an existing VehicleOwner by ID.
    """
    owner = get_object_or_404(VehicleOwner, id=owner_id)
    try:
        if request.method == 'POST':
            owner.name = request.POST.get('vowner')
            owner.save()
            return HttpResponseRedirect('/owners')
    except Exception:
        return HttpResponseRedirect('/owners')

    return render(request, 'vehicle_owner/add_vo.html', {'owner': owner, 'action': "Edit"})


@transaction.atomic
def delete_owner(request, owner_id):
    """
    Deletes a VehicleOwner by ID.
    """
    try:
        owner = get_object_or_404(VehicleOwner, id=owner_id)
        owner.delete()
        return HttpResponseRedirect('/owners')
    except Exception:
        return HttpResponseRedirect('/owners')


# -----------------------------------------------------------
# Driver CRUD
# -----------------------------------------------------------

@transaction.atomic
def add_driver(request):
    """
    Creates a new Driver record using the 'driver/add_driver.html' template.
    """
    omc = Company.objects.all()   # For dropdown (Oil Marketing Company)
    loc = Location.objects.all()  # For dropdown (HTV License Authority)

    if request.method == 'POST':
        # Create a new Driver instance (unsaved at first)
        driver = Driver()

        # Personal Info
        driver.driver_number = request.POST.get('driver_number')
        driver.name = request.POST.get('name')
        driver.father_name = request.POST.get('father_name')
        driver.cnic = request.POST.get('cnic')
        driver.cnic_validity = request.POST.get('cnic_validity') or None
        driver.cell_phone_num = request.POST.get('cell_phone_num')
        driver.education = request.POST.get('education')
        driver.dob = request.POST.get('dob') or None
        driver.address = request.POST.get('address')

        # License Info
        driver.dl_status = request.POST.get('dl_status')
        driver.ddc_issue_date = request.POST.get('ddc_issue_date') or None
        driver.license_no = request.POST.get('license_no')

        # ForeignKey for HTV License Authority (Location)
        htv_license_authority_id = request.POST.get('htv_license_authority')
        if htv_license_authority_id:
            driver.htv_license_authority_id = int(htv_license_authority_id)

        driver.htv_license_issue_date = request.POST.get('htv_license_issue_date') or None
        driver.htv_license_expiry_date = request.POST.get('htv_license_expiry_date') or None

        # Medical & DDC
        company_id = request.POST.get('company')
        if company_id:
            driver.company_id = int(company_id)

        driver.medical_health = request.POST.get('medical_health')
        driver.medical_report_date = request.POST.get('medical_report_date') or None
        driver.medical_expiry_date = request.POST.get('medical_expiry_date') or None
        driver.lab_name = request.POST.get('lab_name')
        driver.ddc_expiry_date = request.POST.get('ddc_expiry_date') or None
        driver.blood_group = request.POST.get('blood_group')

        # Other Information
        driver.joining_date = request.POST.get('joining_date') or None
        driver.salary_increment_date = request.POST.get('salary_increment_date') or None
        driver.leave_date = request.POST.get('leave_date') or None
        driver.leave_resume_date = request.POST.get('leave_resume_date') or None
        driver.experience = request.POST.get('experience') or None
        driver.previous_company = request.POST.get('previous_company')
        driver.tank_lorry = request.POST.get('tank_lorry')

        # Handle driver image if a new file is uploaded
        user_image = request.FILES.get('image')
        if user_image:
            image_pil = Image.open(user_image)
            # Crop & resize to 200x200 if needed
            width, height = image_pil.size
            new_size = min(width, height)

            left = (width - new_size) / 2
            top = (height - new_size) / 2
            right = (width + new_size) / 2
            bottom = (height + new_size) / 2

            image_pil = image_pil.crop((left, top, right, bottom))
            image_pil = image_pil.resize((200, 200), Image.LANCZOS)

            image_data = BytesIO()
            image_pil.save(image_data, format='JPEG')
            image_data.seek(0)

            driver.image.save(
                user_image.name,
                ContentFile(image_data.getvalue()),
                save=False
            )

        # Finally save the new driver
        driver.save()

        # Redirect to the newly created driver's detail page
        return redirect('/driverview/' + str(driver.id) + '/')

    # GET request: Show empty form
    context = {
        'driver': None,  # No existing driver yet
        'omc': omc,
        'loc': loc,
        'action': "Add"
    }
    return render(request, 'driver/add_driver.html', context)


@transaction.atomic
def edit_driver(request, driver_id):
    """
    View to update an existing Driver's information.
    Renders the 'driver/add_driver.html' (or similar) template.
    """
    driver = get_object_or_404(Driver, id=driver_id)
    omc = Company.objects.all()  # For the "Oil Marketing Company" dropdown
    loc = Location.objects.all() # For the "HTV License Authority" dropdown

    if request.method == 'POST':
        # Personal Info
        driver.driver_number = request.POST.get('driver_number')
        driver.name = request.POST.get('name')
        driver.father_name = request.POST.get('father_name')
        driver.cnic = request.POST.get('cnic')
        driver.cnic_validity = request.POST.get('cnic_validity') or None
        driver.cell_phone_num = request.POST.get('cell_phone_num')
        driver.education = request.POST.get('education')
        driver.dob = request.POST.get('dob') or None
        driver.address = request.POST.get('address')

        # License Info
        driver.dl_status = request.POST.get('dl_status')
        driver.ddc_issue_date = request.POST.get('ddc_issue_date') or None
        driver.license_no = request.POST.get('license_no')

        # ForeignKey: htv_license_authority
        htv_license_authority_id = request.POST.get('htv_license_authority')
        if htv_license_authority_id:
            driver.htv_license_authority_id = int(htv_license_authority_id)

        driver.htv_license_issue_date = request.POST.get('htv_license_issue_date') or None
        driver.htv_license_expiry_date = request.POST.get('htv_license_expiry_date') or None

        # Medical & DDC
        company_id = request.POST.get('company')
        if company_id:
            driver.company_id = int(company_id)

        driver.medical_health = request.POST.get('medical_health')
        driver.medical_report_date = request.POST.get('medical_report_date') or None
        driver.medical_expiry_date = request.POST.get('medical_expiry_date') or None
        driver.lab_name = request.POST.get('lab_name')
        driver.ddc_expiry_date = request.POST.get('ddc_expiry_date') or None
        driver.blood_group = request.POST.get('blood_group')

        # Other Information
        driver.joining_date = request.POST.get('joining_date') or None
        driver.salary_increment_date = request.POST.get('salary_increment_date') or None
        driver.leave_date = request.POST.get('leave_date') or None
        driver.leave_resume_date = request.POST.get('leave_resume_date') or None
        driver.experience = request.POST.get('experience') or None
        driver.previous_company = request.POST.get('previous_company')
        driver.tank_lorry = request.POST.get('tank_lorry')

        # Handle driver image if a new file is uploaded
        user_image = request.FILES.get('image')
        if user_image:
            image_pil = Image.open(user_image)
            # Cropping to square if you want
            width, height = image_pil.size
            new_size = min(width, height)
            left = (width - new_size) / 2
            top = (height - new_size) / 2
            right = (width + new_size) / 2
            bottom = (height + new_size) / 2

            # Crop and resize
            image_pil = image_pil.crop((left, top, right, bottom))
            image_pil = image_pil.resize((200, 200), Image.LANCZOS)

            # Save to memory
            image_data = BytesIO()
            image_pil.save(image_data, format='JPEG')
            image_data.seek(0)
            # Overwrite existing image
            driver.image.save(user_image.name, ContentFile(image_data.getvalue()), save=False)

        # Finally, save the updated driver record
        driver.save()

        return redirect('/driverview/' + str(driver.id) + '/')

    # GET request: show the form
    context = {
        'driver': driver,
        'omc': omc,
        'loc': loc,
        'action': "Edit"
    }
    return render(request, 'driver/add_driver.html', context)


@transaction.atomic
def delete_driver(request):
    """
    Deletes a Driver (implement your own logic).
    """
    pass


# -----------------------------------------------------------
# Vehicle CRUD
# -----------------------------------------------------------

@transaction.atomic
def add_vehicle(request):
    """
    Adds a new Vehicle.
    """
    vehicle_makers = VehicleMaker.objects.all()
    vehicle_owners = VehicleOwner.objects.all()
    company = Company.objects.all()

    if request.method == 'POST':
        # Check if selected foreign key values exist
        omc_exists = Company.objects.get(name=request.POST.get('omc'))
        make_exists = VehicleMaker.objects.get(name=request.POST.get('vmake'))
        lease_company_exist = VehicleOwner.objects.get(name=request.POST.get('lease_company'))
        lease_bank_exist = VehicleOwner.objects.get(name=request.POST.get('lease_bank'))

        new_vehicle = Vehicle(
            tl_number=request.POST.get('tl_number'),
            capacity=request.POST.get('capacity'),
            omc=omc_exists,
            maker=make_exists,
            chambers=request.POST.get('chambers'),
            model=request.POST.get('model'),
            engine_number=request.POST.get('engine_number'),
            chassis_number=request.POST.get('chassis_number'),
            lease_company=lease_company_exist,
            lease_bank=lease_bank_exist,
            status=request.POST.get('status'),
            vehicle_type=request.POST.get('type'),
            trailer_id=request.POST.get('trailer_id'),
            brand=request.POST.get('brand'),
            nha_configuration_class=request.POST.get('nha'),
            gross_empty_trailer_weight=request.POST.get('gross'),
            dip_chart_date=request.POST.get('vd_ed'),
            insurance_date=request.POST.get('vr_ed'),
            tax_paid_date=request.POST.get('vt_ed'),
            fitness_date=request.POST.get('vf_ed'),
            q_fom_date=request.POST.get('vq_ed'),
            route_permit_date=request.POST.get('vrp_ed')
        )
        new_vehicle.save()
        return HttpResponseRedirect('/vehicleview/' + str(new_vehicle.id) + '/')

    context = {
        'vehicle_makers': vehicle_makers,
        'vehicle_owners': vehicle_owners,
        'company': company,
        'form_heading': "Add a new Vehicle",
        'action': "Add"
    }
    return render(request, 'vehicle/add_vehicle.html', context)


@transaction.atomic
def edit_vehicle(request, vehicle_id):
    """
    Edits an existing Vehicle by ID.
    """
    vehicle_makers = VehicleMaker.objects.all()
    vehicle_owners = VehicleOwner.objects.all()
    company = Company.objects.all()

    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        omc_exists = Company.objects.get(name=request.POST.get('omc'))
        make_exists = VehicleMaker.objects.get(name=request.POST.get('vmake'))
        lease_company_exist = VehicleOwner.objects.get(name=request.POST.get('lease_company'))
        lease_bank_exist = VehicleOwner.objects.get(name=request.POST.get('lease_bank'))

        vehicle.tl_number = request.POST.get('tl_number')
        vehicle.capacity = request.POST.get('capacity')
        vehicle.omc = omc_exists
        vehicle.maker = make_exists
        vehicle.chambers = request.POST.get('chambers')
        vehicle.model = request.POST.get('model')
        vehicle.engine_number = request.POST.get('engine_number')
        vehicle.chassis_number = request.POST.get('chassis_number')
        vehicle.lease_company = lease_company_exist
        vehicle.lease_bank = lease_bank_exist
        vehicle.status = request.POST.get('status')
        vehicle.vehicle_type = request.POST.get('type')
        vehicle.trailer_id = request.POST.get('trailer_id')
        vehicle.brand = request.POST.get('brand')
        vehicle.nha_configuration_class = request.POST.get('nha')
        vehicle.gross_empty_trailer_weight = request.POST.get('gross')
        vehicle.dip_chart_date = request.POST.get('vd_ed')
        vehicle.insurance_date = request.POST.get('vr_ed')
        vehicle.tax_paid_date = request.POST.get('vt_ed')
        vehicle.fitness_date = request.POST.get('vf_ed')
        vehicle.q_fom_date = request.POST.get('vq_ed')
        vehicle.route_permit_date = request.POST.get('vrp_ed')
        vehicle.save()

        return HttpResponseRedirect('/vehicleview/' + str(vehicle.id) + '/')

    context = {
        'vehicle_makers': vehicle_makers,
        'vehicle_owners': vehicle_owners,
        'vehicle': vehicle,
        'company': company,
        'form_heading': "Edit Vehicle Details",
        'action': "Edit",
    }
    return render(request, 'vehicle/add_vehicle.html', context)


@transaction.atomic
def delete_vehicle(request):
    """
    Deletes a Vehicle (implement your own logic).
    """
    pass


# -----------------------------------------------------------
# Driver & Vehicle Listing / Detail
# -----------------------------------------------------------

def driver_view(request, driver_id):
    """
    Displays details of a single Driver, including training & TBM info.
    """
    driver = get_object_or_404(Driver, id=driver_id)

    date_fields = {
        'cnic_validity': driver.cnic_validity,
        'Motorway_Cissue_Date': driver.ddc_issue_date,
        'HTV_License_Issue_Date': driver.htv_license_issue_date,
        'HTV_License_Expiry_Date': driver.htv_license_expiry_date,
        'DDC_Date': driver.ddc_expiry_date,
        'Report_Date': driver.medical_report_date,
        'Expiry_Date': driver.medical_expiry_date,
        'Joining_Date': driver.joining_date,
        'Salary_Increment_Date': driver.salary_increment_date,
        'Leave_Date': driver.leave_date,
        'Leave_Resume': driver.leave_resume_date,
    }

    for field_name, field_date in date_fields.items():
        if field_date:
            status_message = get_date_status(field_date, field_name)
            setattr(driver, f"{field_name}_status", status_message)

    # Example of retrieving Drills / Training data
    annual_drill_data = AnnualDrill.objects.all()
    attendance_data = AnnualTrainingDriver.objects.filter(driver=driver)

    tbm = DriverToolBoxMeetingAttended.objects.filter(driver=driver).values_list(
        'no_of_times_attended', flat=True
    )
    tbm_data = list(tbm)

    context = {
        'driver': driver,
        'annual_drill_data': annual_drill_data,
        'driver_attendance': attendance_data,
        'tbm_data': tbm_data,
    }
    return render(request, 'driver/driver_view.html', context)


def vehicle_view(request, vehicle_id):
    """
    Displays details of a single Vehicle.
    """
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    context = {'vehicle': vehicle}
    return render(request, 'vehicle/vehicleview.html', context)


# -----------------------------------------------------------
# Utility: Login/Logout
# -----------------------------------------------------------

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'user/login.html')


def logout_user(request):
    logout(request)
    return redirect('/loginuser')


# -----------------------------------------------------------
# Helpers for Date Status
# -----------------------------------------------------------

def get_date_status(date_val, field_name):
    current_date = datetime.now().date()
    days_remaining = (date_val - current_date).days
    if days_remaining <= 0:
        return "Expired"
    elif days_remaining <= 90:
        return "Close to Expiry"
    else:
        return "Valid"


# -----------------------------------------------------------
# Driver Listing
# -----------------------------------------------------------

def get_driver(request):
    """
    Shows a list of all drivers with date-expiry statuses computed.
    """
    drivers = Driver.objects.all().order_by('name')
    for driver in drivers:
        date_fields = {
            'cnic_validity': driver.cnic_validity,
            'Motorway_Cissue_Date': driver.ddc_issue_date,
            'HTV_License_Issue_Date': driver.htv_license_issue_date,
            'HTV_License_Expiry_Date': driver.htv_license_expiry_date,
            'DDC_Date': driver.ddc_expiry_date,
            'Report_Date': driver.medical_report_date,
            'Expiry_Date': driver.medical_expiry_date,
            'Joining_Date': driver.joining_date,
            'Salary_Increment_Date': driver.salary_increment_date,
            'Leave_Date': driver.leave_date,
            'Leave_Resume': driver.leave_resume_date,
        }
        for field_name, field_date in date_fields.items():
            if field_date:
                status_message = get_date_status(field_date, field_name)
                setattr(driver, f"{field_name}_status", status_message)

    context = {'drivers': drivers}
    return render(request, 'driver/driver.html', context)


# -----------------------------------------------------------
# Vehicle Listing
# -----------------------------------------------------------

def get_vehicle(request, filter):
    """
    Shows a filtered list of Vehicles based on `filter`.
    For example, filter by OMC (Company).
    """
    if filter == 'apl':
        vehicles = Vehicle.objects.filter(omc_id=4)
        image = '/static/images/attock-logo.png'
    elif filter == 'pso':
        vehicles = Vehicle.objects.filter(omc_id=6)
        image = '/static/images/pso-logo.png'
    elif filter == 'go':
        vehicles = Vehicle.objects.filter(omc_id=5)
        image = '/static/images/go-logo.png'
    elif filter == 'tppl':
        omc_ids = [1, 2, 3]
        vehicles = Vehicle.objects.filter(omc_id__in=omc_ids)
        image = '/static/images/total-logo.png'
    elif filter == 'all':
        vehicles = Vehicle.objects.all()
        image = ''
    else:
        vehicles = Vehicle.objects.none()
        image = ''

    for vehicle in vehicles:
        date_fields = {
            'tax_expiry': vehicle.tax_paid_date,
            'fitness_expiry': vehicle.fitness_date,
            'road_insurance': vehicle.insurance_date,
            'Dip_Chart': vehicle.dip_chart_date,
            'Q_Fom': vehicle.q_fom_date,
            'Route': vehicle.route_permit_date,
        }
        for field_name, field_date in date_fields.items():
            if field_date:
                status_message = get_date_status(field_date, field_name)
                setattr(vehicle, f"{field_name}_status", status_message)

    context = {'vehicles': vehicles, 'image': image}
    return render(request, 'vehicle/vehicle.html', context)


# -----------------------------------------------------------
# VehicleMaker / VehicleOwner / Company
# -----------------------------------------------------------

def get_vehicle_maker(request):
    vehicle_makers = VehicleMaker.objects.all()
    return render(request, 'vehicle_maker/vehicle_makers.html', {'vehicle_makers': vehicle_makers})


def get_vehicle_owner(request):
    vehicle_owners = VehicleOwner.objects.all()
    return render(request, 'vehicle_owner/vehicle_owner.html', {'vehicle_owners': vehicle_owners})


def get_company(request):
    companies = Company.objects.all()
    return render(request, 'company/company.html', {'companies': companies})


# -----------------------------------------------------------
# Dashboard
# -----------------------------------------------------------

def dashboard(request):
    """
    Renders a dashboard with counts and expired items for drivers/vehicles.
    """
    total_vehicles = Vehicle.objects.count()
    today = date.today()

    expired_cnic_list = []
    expired_ddc_list = []
    expired_htv_license_list = []
    expired_general_list = []

    drivers = Driver.objects.all()

    for driver in drivers:
        # Checking each expiration date
        if driver.cnic_validity and driver.cnic_validity < today:
            expired_cnic_list.append(driver)
        if driver.ddc_expiry_date and driver.ddc_expiry_date < today:
            expired_ddc_list.append(driver)
        if driver.htv_license_expiry_date and driver.htv_license_expiry_date < today:
            expired_htv_license_list.append(driver)
        if driver.medical_expiry_date and driver.medical_expiry_date < today:
            expired_general_list.append(driver)

    expired_cnic_list = sorted(expired_cnic_list, key=lambda x: x.name)
    expired_ddc_list = sorted(expired_ddc_list, key=lambda x: x.name)
    expired_htv_license_list = sorted(expired_htv_license_list, key=lambda x: x.name)
    expired_general_list = sorted(expired_general_list, key=lambda x: x.name)

    # Example "working days" calculation
    year = today.year
    month = today.month
    cal = calendar.monthcalendar(year, month)
    working_days = 0
    for week in cal:
        for day in week:
            # Sunday is 6
            if day != 0 and calendar.weekday(year, month, day) != 6:
                working_days += 1

    man_days_work = (58 + drivers.count()) * working_days

    # For TBM data: how many times each meeting is attended
    meetings_data = ToolBoxMeetingTopic.objects.prefetch_related('drivertoolboxmeetingattended_set')
    tbm_data = [meeting.drivertoolboxmeetingattended_set.count() for meeting in meetings_data]

    context = {
        'total_drivers': drivers.count(),
        'total_vehicles': total_vehicles,
        'man_days_work': man_days_work,
        'expired_cnic_list': expired_cnic_list,
        'expired_ddc_list': expired_ddc_list,
        'expired_htv_license_list': expired_htv_license_list,
        'expired_general_list': expired_general_list,
        'tbm_data': tbm_data,
    }
    return render(request, 'dashboard.html', context)


# -----------------------------------------------------------
# User Management (Django built-in User)
# -----------------------------------------------------------

def adduser(request):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {
            'error_head': "You do not have the authority to perform edit or delete operations.",
            'log': 'Log In with Full Access Account.'
        })

    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        access_level = request.POST.get('access-level')
        status = request.POST.get('status')
        user_image = request.FILES.get('user_image')

        is_superuser = True if access_level == "Full Access" else False
        is_active = True if status == "Active" else False

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.save()

        if user_image:
            user_image_obj = UserImage(user=user)
            image_pil = Image.open(user_image)
            if image_pil.mode == 'RGBA':
                image_pil = image_pil.convert('RGB')

            width, height = image_pil.size
            new_size = min(width, height)

            left = (width - new_size) / 2
            top = (height - new_size) / 2
            right = (width + new_size) / 2
            bottom = (height + new_size) / 2
            image_pil = image_pil.crop((left, top, right, bottom))
            image_pil = image_pil.resize((200, 200), Image.LANCZOS)

            image_data = BytesIO()
            image_pil.save(image_data, format='JPEG')
            user_image_obj.img.save(
                user_image.name, ContentFile(image_data.getvalue())
            )
            user_image_obj.save()

        return redirect('/allusers')

    return render(request, 'user/adduser.html', {'heading': "Adding User"})


def deleteuser(request, id):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {
            'error_head': "You do not have the authority to perform this operation.",
            'log': 'Log In with Full Access Account.'
        })
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/allusers')


def edituser(request, id):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {
            'error_head': "You do not have the authority to perform this operation.",
            'log': 'Log In with Full Access Account.'
        })

    user = User.objects.get(id=id)
    try:
        user_image_obj = UserImage.objects.get(user=user)
        flag = True
    except UserImage.DoesNotExist:
        user_image_obj = UserImage(user=user)
        flag = False

    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        # password = request.POST.get('password')
        access_level = request.POST.get('access-level')
        status = request.POST.get('status')

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = True if access_level == "Full Access" else False
        user.is_active = True if status == "Active" else False
        # if password.strip():
        #     user.set_password(password)
        user.save()

        user_image = request.FILES.get('user_image')
        if user_image:
            if flag:
                # remove old image object if you want to re-create
                user_image_obj.img.delete(save=False)

            image_pil = Image.open(user_image)
            if image_pil.mode == 'RGBA':
                image_pil = image_pil.convert('RGB')

            width, height = image_pil.size
            new_size = min(width, height)

            left = (width - new_size) / 2
            top = (height - new_size) / 2
            right = (width + new_size) / 2
            bottom = (height + new_size) / 2
            image_pil = image_pil.crop((left, top, right, bottom))
            image_pil = image_pil.resize((200, 200), Image.LANCZOS)

            image_data = BytesIO()
            image_pil.save(image_data, format='JPEG')

            user_image_obj.img.save(
                user_image.name, ContentFile(image_data.getvalue())
            )
            user_image_obj.save()

        return redirect('/allusers')

    initial_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'access_level': 'Full Access' if user.is_superuser else 'Read Only Access',
        'status': 'Active' if user.is_active else 'Disabled',
    }

    context = {
        'user': user,
        'initial_data': initial_data,
        'user_img': user_image_obj.img if flag else None,
        'heading': 'Editing User',
    }
    return render(request, 'user/adduser.html', context)


def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)


@login_required(login_url='/loginuser')
def allusers(request):
    users = User.objects.all()
    user_data = []
    for usr in users:
        user_image_obj = UserImage.objects.filter(user=usr).first()
        user_info = {'user': usr, 'user_image': user_image_obj}
        user_data.append(user_info)
    return render(request, 'user/users.html', {'user_data': user_data})


# -----------------------------------------------------------
# Example of monthly update of driver ages
# -----------------------------------------------------------

def update_driver_ages(request):
    """
    Example function to recalc driver ages from their DOB.
    """
    drivers = Driver.objects.all()
    for driver in drivers:
        if driver.dob:
            today = date.today()
            age = today.year - driver.dob.year - (
                (today.month, today.day) < (driver.dob.month, driver.dob.day)
            )
            driver.age = age
            driver.save()
    return redirect('/drivers')


# -----------------------------------------------------------
# Example: Querying all vehicles for TPPL
# -----------------------------------------------------------

def get_tppl(request):
    """
    Renders the same 'vehicle.html' but only for certain vehicles.
    """
    vehicles = Vehicle.objects.all()

    for vehicle in vehicles:
        date_fields = {
            'tax_expiry': vehicle.tax_paid_date,
            'fitness_expiry': vehicle.fitness_date,
            'road_insurance': vehicle.insurance_date,
            'Dip_Chart': vehicle.dip_chart_date,
            'Q_Fom': vehicle.q_fom_date,
            'Route': vehicle.route_permit_date,
        }
        for field_name, field_date in date_fields.items():
            if field_date:
                status_message = get_date_status(field_date, field_name)
                setattr(vehicle, f"{field_name}_status", status_message)

    return render(request, 'vehicle/vehicle.html', {'vehicles': vehicles})


# -----------------------------------------------------------
# Static Content
# -----------------------------------------------------------

def get_procedures(request):
    return render(request, 'static_content/procedures.html')


def get_emergency_procedures(request):
    return render(request, 'static_content/eprocedures.html')


def get_policies(request):
    return render(request, 'static_content/policies.html')
