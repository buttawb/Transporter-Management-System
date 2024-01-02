import calendar
from imaplib import _Authenticator
from io import BytesIO
import os
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from dashboard.models import *
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from PIL import Image
from django.core.files.base import ContentFile
from datetime import datetime
from django.urls import reverse


# def remove_null_images(request):
#     # Search for records with D_Image containing 'Null'
#     drivers_with_null = Driver.objects.filter(D_Image='Null')

#     # Iterate over the matching records and set D_Image to None
#     for driver in drivers_with_null:
#         driver.D_Image = None
#         driver.save()

#     return HttpResponse("Records updated successfully.")
# def import_drivers_from_images(request):
#     image_folder = '/Users/AWB/Downloads/img'

#     for filename in os.listdir(image_folder):
#         driver_number = os.path.splitext(filename)[0]

#         try:
#             driver = Driver.objects.get(D_Number=driver_number)
#             driver.D_Image = f'driver_images/{filename}'
#             driver.save()
#         except Driver.DoesNotExist:
#             # Driver doesn't exist - do something or simply pass
#             pass

#     return HttpResponse("Drivers updated successfully.")
# def count_uploaded_images(request):
#     # Count the number of drivers with non-null and non-empty D_Image fields
#     count = Driver.objects.exclude(D_Image__exact='').count()

#     return HttpResponse(f"Number of uploaded images: {count}")

# import pandas as pd

# def match_driver_ids(request):
#     # Specify the path to the CSV file
#     csv_file_path = '/Users/AWB/Desktop/Book2.csv'  # Update with the actual path

#     # Function to get ID from D_Number
#     def get_driver_id(d_number):
#         try:
#             driver = Driver.objects.get(D_Number=d_number)
#             return driver.D_ID
#         except Driver.DoesNotExist:
#             return None

#     # Read the CSV file
#     df = pd.read_csv(csv_file_path)

#     # Create a new column 'Driver_ID' in the DataFrame to store the corresponding ID
#     df['Driver_ID'] = df['D_Number'].apply(get_driver_id)

#     # Save the updated DataFrame to a new CSV file in the root directory
#     output_csv_file_path = os.path.join(os.getcwd(), 'output.csv')
#     df.to_csv(output_csv_file_path, index=False)

#     # Serve the newly created CSV file for download
#     with open(output_csv_file_path, 'rb') as csv_file:
#         response = HttpResponse(csv_file.read(), content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename=output.csv'
#         return response
# import csv
# def update_models_from_csv(request):
#     with open('/Users/AWB/Desktop/tb.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)

#         for row in csv_reader:
#             if len(row) >= 3:
#                 # 1st column: Driver ID
#                 driver_id = int(row[0])

#                 # Get or create the Driver
#                 driver, created = Driver.objects.get_or_create(D_ID=driver_id)

#                 # Iterate through the columns starting from the second column (index 1)
#                 for column_index, meeting_count in enumerate(row[1:], start=1):
#                     if meeting_count:
#                         # Get the corresponding MeetingTopic object by its ID
#                         meeting_topic_id = column_index

#                         # Convert the meeting_count to an integer
#                         try:
#                             meeting_count = int(meeting_count)
#                         except ValueError:
#                             # Handle the case where the meeting_count is not an integer
#                             continue

#                         # Retrieve the corresponding MeetingTopic object by ID
#                         meeting_topic = tool_box_meeting_topics.objects.get(id=meeting_topic_id)

#                         # Create or update records in driver_tool_box_meeting_attended
#                         driver_tool_box_meeting_attended.objects.update_or_create(
#                             meeting_attended_by=driver,
#                             meetings_attended=meeting_topic,
#                             defaults={'no_of_times_meeting_attended': meeting_count}
#                         )

#     return HttpResponse("Models updated from CSV file.")

@transaction.atomic
def add_driver_training(request, D_ID):
    driver = get_object_or_404(Driver, D_ID=D_ID)
    drills = annual_drill.objects.all()
    training = annual_training.objects.all()
    try:
        if request.method == 'POST':
            train = request.POST.get('train')
            drill = request.POST.get('drill')
            date = request.POST.get('date')

            traing = annual_training.objects.get(train_name=train)
            drilling = annual_drill.objects.get(drill_name=drill)
            
            training_no = ('train'+str(traing.id)+'_completed_date')
            meeting_train, created_train = annual_training_driver.objects.get_or_create(user=driver, defaults={training_no: date})

            if not created_train:
                try:
                    setattr(meeting_train, training_no, date)
                    meeting_train.save()
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
            else:
                meeting_train = annual_training_driver(user=driver,  **{training_no: date})
                meeting_train.save()

            drilling_no = ('train'+str(drilling.id)+'_completed_date')
            meeting_drill, created_drill = annual_drill_driver.objects.get_or_create(user=driver, defaults={drilling_no: date})

            if not created_drill:
                setattr(meeting_drill, drilling_no, date)
                meeting_drill.save()
            else:
                meeting_drill = annual_drill_driver(user=driver,  **{drilling_no: date})
                meeting_drill.save()
            
            driver_view_url = reverse('driverview', args=[D_ID])
            return HttpResponseRedirect(driver_view_url)
            
        else:
            context = {'driver': driver, 'drills': drills, 'training': training}
            return render(request, 'training/add_training.html', context)
    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/')
            


@transaction.atomic
def add_tbm(request, D_ID):
    driver = get_object_or_404(Driver, D_ID=D_ID)
    tbm = tool_box_meeting_topics.objects.all()
    # Save it into driver_violation table
    try:
        if request.method == 'POST':
            meeting_topic = request.POST.get('meeting_topic') 
            tbm_obj = tool_box_meeting_topics.objects.get(meeting_topic=meeting_topic)
            meetings_old = driver_tool_box_meeting_attended.objects.get(meeting_attended_by=driver, meetings_attended=tbm_obj)
            

            
            existing_record = driver_tool_box_meeting_attended.objects.filter(
            meeting_attended_by=driver,
            meetings_attended=tbm_obj
            ).first()

            if existing_record is None:
                # If no record exists, create a new one
                tool = driver_tool_box_meeting_attended(
                    meeting_attended_by=driver,
                    meetings_attended=tbm_obj,
                    no_of_times_meeting_attended=meetings_old.no_of_times_meeting_attended + 1
                )
                tool.save()
            else:
                # A record with the same values already exists, you can update it if needed
                existing_record.no_of_times_meeting_attended += 1
                existing_record.save()
            
            driver_view_url = reverse('driverview', args=[D_ID])
            return HttpResponseRedirect(driver_view_url)
        else:
            context = {'driver': driver, 'tbms': tbm}
            return render(request, 'tbm/add_tbm.html', context)
    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/')


@transaction.atomic
def add_driver_violation(request, D_ID):
    driver = get_object_or_404(Driver, D_ID=D_ID)
    violation = Violations.objects.all()
    # Save it into driver_violation table
    try:
        if request.method == 'POST':
            violation_type = request.POST.get('violationType') 
            violation_obj = Violations.objects.get(violation_type=violation_type)
           
            violation_date = request.POST.get('violationDate')
            details = request.POST.get('details')

            
            driver_violation = Driver_Violation(
                driver=driver,
                violation=violation_obj,
                violation_date=violation_date,
                violation_notes=details
            )
            driver_violation.save()  
            driver_view_url = reverse('driverview', args=[D_ID])
           
            return HttpResponseRedirect(driver_view_url)
        else:
            context = {'driver': driver, 'violations': violation}
            return render(request, 'violation/add_driver_violation.html', context)
    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/')


@transaction.atomic
def delete_company(request, company_id):
    entry = get_object_or_404(Company, cid=company_id)  # Replace with your model
    entry.delete()
    return redirect('/company')


@transaction.atomic
def add_maker(request):
    try:
        if request.method == 'POST':
            vehicle = VehicleMaker()
            vehicle.VMNAME = request.POST.get('maker')
            vehicle.save()

            return HttpResponseRedirect('/makers')
        else:
            return render(request, 'vehicle_maker/add_vm.html', {'action': "Add"})
    except Exception:
        return HttpResponseRedirect('/makers')


@transaction.atomic
def edit_maker(request, maker_id):
    maker = get_object_or_404(VehicleMaker, VMid=maker_id)
    try:
        if request.method == 'POST':
            maker.VMNAME = request.POST.get('maker')
            maker.save()

            return HttpResponseRedirect('/makers')
    except Exception:
        return HttpResponseRedirect('/makers')
    return render(request, 'vehicle_maker/add_vm.html', {'maker': maker, 'action': "Edit"})


@transaction.atomic
def delete_maker(request, maker_id):
    try:
        maker = get_object_or_404(VehicleMaker, VMid=maker_id)
        maker.delete()

        return HttpResponseRedirect('/makers')
    except Exception:
        return HttpResponseRedirect('/makers')


@transaction.atomic
def add_owner(request):
    try:
        if request.method == 'POST':
            owner = VehicleOwner()
            vowner = request.POST.get('vowner')
            owner.VO_name = vowner
            owner.save()

            return HttpResponseRedirect('/owners')
        else:
            return render(request, 'vehicle_owner/add_vo.html', {'action': "Add"})
    except Exception:
        return HttpResponseRedirect('/owners')


@transaction.atomic
def edit_owner(request, owner_id):
    owner = get_object_or_404(VehicleOwner, VO_id=owner_id)
    try:
        if request.method == 'POST':
            owner.VO_name = request.POST.get('vowner')
            owner.save()

            return HttpResponseRedirect('/owners')
    except Exception:
        return HttpResponseRedirect('/owners')
    return render(request, 'vehicle_owner/add_vo.html', {'owner': owner, 'action': "Edit"})


@transaction.atomic
def delete_owner(request, owner_id):
    try:
        owner = get_object_or_404(VehicleOwner, VO_id=owner_id)
        owner.delete()

        return HttpResponseRedirect('/owners')
    except Exception:
        return HttpResponseRedirect('/owners')


@transaction.atomic
def add_driver(request):
    omcc = Company.objects.all()
    locc = Location.objects.all()

    try:
        if request.method == 'POST':
             # Retrieve data directly from request.POST
            id = request.POST.get('id')
            user_image = request.FILES.get('image')
            name = request.POST.get('name')
            father_name = request.POST.get('father_name')
            cnic = request.POST.get('cnic')
            cnic_date = request.POST.get('cnic_date')
            cell = request.POST.get('cell')
            education = request.POST.get('education')
            dob = request.POST.get('dob')
            address = request.POST.get('address')
            driving_license_status = request.POST.get('driving_license_status')
            motorway_trained = request.POST.get('motorway_trained')
            motorway_certification_issue = request.POST.get('motorway_certification_issue')
            license_no = request.POST.get('license_no')
            htc_license = request.POST.get('htc_license')
            htv_license_issue = request.POST.get('htv_license_issue')
            htv_license_expiry = request.POST.get('htv_license_expiry')
            oil_market = request.POST.get('Oil_Marketing_Company')
            medical_health = request.POST.get('medical_health')
            medical_issue = request.POST.get('medical_issue')
            medical_expiry = request.POST.get('medical_expiry')
            lab = request.POST.get('lab')
            ddc_expiry = request.POST.get('ddc_expiry')
            bg = request.POST.get('bg')
            joining = request.POST.get('joining')
            increment = request.POST.get('increment')
            leave = request.POST.get('leave')
            resume = request.POST.get('resume')
            driving_age = request.POST.get('driving_age')
            previous_company = request.POST.get('previous_company')
            tank_lorry = request.POST.get('tank_lorry')
            experience = request.POST.get('experience')

            omc_obj = Company.objects.get(cname=oil_market)
            htv_obj = Location.objects.get(Lname=htc_license)

            if user_image:
                image = Image.open(user_image)

                width, height = image.size
                new_size = min(width, height)
                
                left = (width - new_size) / 2
                top = (height - new_size) / 2
                right = (width + new_size) / 2
                bottom = (height + new_size) / 2
                image = image.crop((left, top, right, bottom))
                image = image.resize((200, 200), Image.LANCZOS)

                image_data = BytesIO()
                image.save(image_data, format='JPEG')
                image_name = user_image.name
                # driver.D_Image.save(user_image.name, ContentFile(image_data.getvalue()))
            else:
                image_data = None
                image_name = None

            driver = Driver(
                D_Number=id,
                D_Image=image_data,
                D_Name=name,
                Father_Name=father_name,
                CNIC=cnic,
                CNIC_Validity=cnic_date if cnic_date else None,
                Cell_Phone_Num=cell,
                Education=education,
                DOB=datetime.strptime(dob, '%Y-%m-%d') if dob else None,
                Address=address,
                DL_Status=driving_license_status if driving_license_status else None,
                Motorway_Trained=motorway_trained if motorway_trained else None,
                DDC_Issue_Date=motorway_certification_issue if motorway_certification_issue else None,
                License_No=license_no if license_no else None,
                HTV_License_Authority=htv_obj,
                HTV_License_Issue_Date=htv_license_issue if htv_license_issue else None,
                HTV_License_Expiry_Date=htv_license_expiry if htv_license_expiry else None,
                Oil_Marketing_Company=omc_obj,
                Medical_Health=medical_health if medical_health else None,
                Report_Date=medical_issue if medical_issue else None,
                Lab_Name=lab if lab else None,
                DDC_Expiry_Date=ddc_expiry if ddc_expiry else None,
                Blood_Group=bg if bg else None,
                Joining_Date=joining if joining else None,
                Salary_Increment_Date=increment if increment else None,
                Leave_Date=leave if leave else None,
                Leave_Resume=resume if resume else None,
                Driving_Age=driving_age if driving_age else None,
                Previous_Company=previous_company if previous_company else None,
                Tank_Lorry=tank_lorry if tank_lorry else None,
                Experience=experience if experience else None,
                Expiry_Date=medical_expiry if medical_expiry else None
            )
            driver.save()
            
            return HttpResponseRedirect('/drivers')
            
        else:
            context = {'omc': omcc, 'loc': locc, 'action': "Add"}
            return render(request, 'driver/add_driver.html', context)
    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/drivers')


@transaction.atomic
def add_vehicle(request):
    vehicle_makers = VehicleMaker.objects.all()
    vehicle_owners = VehicleOwner.objects.all()
    company = Company.objects.all()

    if request.method == 'POST':
        # Check if selected foreign key values exist in related models
        omc_exists = Company.objects.get(cname=request.POST.get('omc'))
        make_exists = VehicleMaker.objects.get(VMNAME=request.POST.get('vmake'))
        lease_company_exist = VehicleOwner.objects.get(VO_name=request.POST.get('lease_company'))
        lease_bank_exist = VehicleOwner.objects.get(VO_name=request.POST.get('lease_bank'))


        # Create a new vehicle object with the extracted data
        new_vehicle = Vehicle(
            TL_Number=request.POST.get('tl_number'),
            Capacity=request.POST.get('capacity'),
            OMC=omc_exists,
            Make=make_exists,
            Chambers=request.POST.get('chambers'),
            Model=request.POST.get('model'),
            Engine_Number=request.POST.get('engine_number'),
            Chassis_Number=request.POST.get('chassis_number'),
            LEASE_COMPANY=lease_company_exist,
            LEASE_BANK=lease_bank_exist,
            Status=request.POST.get('status'),
            Type=request.POST.get('type'),
            Trailer_ID=request.POST.get('trailer_id'),
            Brand=request.POST.get('brand'),
            NHA_Configuration_Class=request.POST.get('nha'),
            Gross_Empty_Trailer_Weight=request.POST.get('gross'),
            DIP_CHART_Date=request.POST.get('vd_ed'),
            INSURANCE_Date=request.POST.get('vr_ed'),
            TAX_PAID_Date=request.POST.get('vt_ed'),
            FITNISSE_Date=request.POST.get('vf_ed'),
            Q_FOM_Date=request.POST.get('vq_ed'),
            Route_Permit_Date=request.POST.get('vrp_ed')
        )

            # Save the new vehicle object
        new_vehicle.save()

        return HttpResponseRedirect('/vehicles/all')

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
    vehicle_makers = VehicleMaker.objects.all()
    vehicle_owners = VehicleOwner.objects.all()
    company = Company.objects.all()

    
    vehicle = Vehicle.objects.get(pk=vehicle_id)

    

    if request.method == 'POST':
    # Check if selected foreign key values exist in related models
        omc_exists = Company.objects.get(cname=request.POST.get('omc'))
        make_exists = VehicleMaker.objects.get(VMNAME=request.POST.get('vmake'))
        lease_company_exist = VehicleOwner.objects.get(VO_name=request.POST.get('lease_company'))
        lease_bank_exist = VehicleOwner.objects.get(VO_name=request.POST.get('lease_bank'))
        # Create a new vehicle object with the extracted data
        new_vehicle = Vehicle(
            TL_Number=request.POST.get('tl_number'),
            Capacity=request.POST.get('capacity'),
            OMC=omc_exists,
            Make=make_exists,
            Chambers=request.POST.get('chambers'),
            Model=request.POST.get('model'),
            Engine_Number=request.POST.get('engine_number'),
            Chassis_Number=request.POST.get('chassis_number'),
            LEASE_COMPANY=lease_company_exist,
            LEASE_BANK=lease_bank_exist,
            Status=request.POST.get('status'),
            Type=request.POST.get('type'),
            Trailer_ID=request.POST.get('trailer_id'),
            Brand=request.POST.get('brand'),
            NHA_Configuration_Class=request.POST.get('nha'),
            Gross_Empty_Trailer_Weight=request.POST.get('gross'),
            DIP_CHART_Date=request.POST.get('vd_ed'),
            INSURANCE_Date=request.POST.get('vr_ed'),
            TAX_PAID_Date=request.POST.get('vt_ed'),
            FITNISSE_Date=request.POST.get('vf_ed'),
            Q_FOM_Date=request.POST.get('vq_ed'),
            Route_Permit_Date=request.POST.get('vrp_ed')
        )

            # Save the new vehicle object
        new_vehicle.save()

        return HttpResponseRedirect('/vehicles/all')
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
    pass


@transaction.atomic
def edit_driver(request, driver_id):
    driver = Driver.objects.get(D_ID=driver_id)
    omcc = Company.objects.all()
    locc = Location.objects.all()

    try:
        if request.method == 'POST':
             # Retrieve data directly from request.POST
            id = request.POST.get('id')
            user_image = request.FILES.get('image')
            name = request.POST.get('name')
            father_name = request.POST.get('father_name')
            cnic = request.POST.get('cnic')
            cnic_date = request.POST.get('cnic_date')
            cell = request.POST.get('cell')
            education = request.POST.get('education')
            dob = request.POST.get('dob')
            address = request.POST.get('address')
            driving_license_status = request.POST.get('driving_license_status')
            motorway_trained = request.POST.get('motorway_trained')
            motorway_certification_issue = request.POST.get('motorway_certification_issue')
            license_no = request.POST.get('license_no')
            htc_license = request.POST.get('htc_license')
            htv_license_issue = request.POST.get('htv_license_issue')
            htv_license_expiry = request.POST.get('htv_license_expiry')
            oil_market = request.POST.get('Oil_Marketing_Company')
            medical_health = request.POST.get('medical_health')
            medical_issue = request.POST.get('medical_issue')
            medical_expiry = request.POST.get('medical_expiry')
            lab = request.POST.get('lab')
            ddc_expiry = request.POST.get('ddc_expiry')
            bg = request.POST.get('bg')
            joining = request.POST.get('joining')
            increment = request.POST.get('increment')
            leave = request.POST.get('leave')
            resume = request.POST.get('resume')
            driving_age = request.POST.get('driving_age')
            previous_company = request.POST.get('previous_company')
            tank_lorry = request.POST.get('tank_lorry')
            experience = request.POST.get('experience')

            omc_obj = Company.objects.get(cname=oil_market)
            htv_obj = Location.objects.get(Lname=htc_license)

            if user_image:
                image = Image.open(user_image)

                width, height = image.size
                new_size = min(width, height)
                
                left = (width - new_size) / 2
                top = (height - new_size) / 2
                right = (width + new_size) / 2
                bottom = (height + new_size) / 2
                image = image.crop((left, top, right, bottom))
                image = image.resize((200, 200), Image.LANCZOS)

                image_data = BytesIO()
                image.save(image_data, format='JPEG')
                driver.D_Image.save(user_image.name, ContentFile(image_data.getvalue()))

            driver.D_Number = id
            driver.D_Name = name
            driver.Father_Name = father_name
            driver.CNIC = cnic
            driver.CNIC_Validity = cnic_date if cnic_date else None
            driver.Cell_Phone_Num = cell
            driver.Education = education
            driver.DOB = datetime.strptime(dob, '%Y-%m-%d') if dob else None
            driver.Address = address
            driver.DL_Status = driving_license_status if driving_license_status else None
            driver.Motorway_Trained = motorway_trained if motorway_trained else None
            driver.DDC_Issue_Date = motorway_certification_issue if motorway_certification_issue else None
            driver.License_No = license_no if license_no else None
            driver.HTV_License_Authority = htv_obj
            driver.HTV_License_Issue_Date = htv_license_issue if htv_license_issue else None
            driver.HTV_License_Expiry_Date = htv_license_expiry if htv_license_expiry else None
            driver.Oil_Marketing_Company = omc_obj
            driver.Medical_Health = medical_health if medical_health else None
            driver.Report_Date = medical_issue if medical_issue else None
            driver.Lab_Name = lab if lab else None
            driver.DDC_Expiry_Date = ddc_expiry if ddc_expiry else None
            driver.Blood_Group = bg if bg else None
            driver.Joining_Date = joining if joining else None
            driver.Salary_Increment_Date = increment if increment else None
            driver.Leave_Date = leave if leave else None
            driver.Leave_Resume = resume if resume else None
            driver.Driving_Age = driving_age if driving_age else None
            driver.Previous_Company = previous_company if previous_company else None
            driver.Tank_Lorry = tank_lorry if tank_lorry else None
            driver.Experience = experience if experience else None
            driver.Expiry_Date = medical_expiry if medical_expiry else None
            driver.save()
            
            return HttpResponseRedirect('/drivers')
            
        else:
            context = {'driver': driver, 'omc': omcc, 'loc': locc, 'action': "Edit"}
            return render(request, 'driver/add_driver.html', context)
    except Exception as e:
        print(str(e))
        return HttpResponseRedirect('/drivers')



@transaction.atomic
def delete_driver(request):
    pass


def get_violation(request):
    pass


def add_violation(request):
    pass


@transaction.atomic
def add_company(request):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {'error_head': "You do not have the authority to perform edit or delete operations. ", 'log': 'Log In with Full Access Account.'})
    try:
        if request.method == 'POST':
            company = Company()
            company.cabb = request.POST.get('cabb')
            company.cname = request.POST.get('company_name')
            company.save()

            return HttpResponseRedirect('/company')
        else:
            return render(request, 'company/add_company.html')
    except Exception:
        return HttpResponseRedirect('/company')


@transaction.atomic
def edit_company(request, company_id):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {'error_head': "You do not have the authority to perform edit or delete operations. ", 'log': 'Log In with Full Access Account.'})
    # Retrieve the company record based on company_id
    company = get_object_or_404(Company, cid=company_id)

    try:
        if request.method == 'POST':
            # Retrieve the data from the POST request
            cabb = request.POST.get('cabb')
            cname = request.POST.get('company_name')

            # Update the company record with the new data
            company.cabb = cabb
            company.cname = cname
            company.save()

            return HttpResponseRedirect('/company')
    except Exception:
        return HttpResponseRedirect('/company')
    return render(request, 'company/add_company.html', {'company': company,
                                                        'action': "Edit"})

def driver_view(request, driver_id):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})

    driver = get_object_or_404(Driver, D_ID=driver_id)
    
    # Retrieve training name and training month for the driver from annual_drill
    annual_drill_data = annual_drill.objects.all()
    
    # Retrieve the driver's attendance data
    attendance_data = annual_training_driver.objects.filter(user=driver)
    tbm = driver_tool_box_meeting_attended.objects.filter(meeting_attended_by=driver_id).values_list('no_of_times_meeting_attended', flat=True)
    tbm_data = list(tbm)

# Print the data in exact order

    context = {
        'driver': driver,
        'annual_drill_data': annual_drill_data,
        'driver_attendance': attendance_data,
        'tbm_data': tbm_data,
    }
    return render(request, 'driver/driver_view.html', context)


def vehicle_view(request, vehicle_id):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    # Retrieve training name and training month for the driver from annual_drill

    context = {
        'vehicle': vehicle
    }
    return render(request, 'vehicle/vehicleview.html', context)


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

def get_driver(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    
    drivers = Driver.objects.all().order_by('D_Name')  # Query the database to get all drivers
    
    # Define a function to calculate the status message based on the date
    def get_date_status(date, field_name):
        current_date =  datetime.now().date()
        days_remaining = (date - current_date).days
        if days_remaining <= 0:
            return f"Expired"
        elif days_remaining <= 90:
            return f"Close to Expiry"
        else:
            return f"Valid"
    
    for driver in drivers:
        # Define a dictionary to store the date fields and their corresponding status messages
        date_fields = {
            'CNIC_Validity': driver.CNIC_Validity,
            'Motorway_Cissue_Date': driver.DDC_Issue_Date,
            'HTV_License_Issue_Date': driver.HTV_License_Issue_Date,
            'HTV_License_Expiry_Date': driver.HTV_License_Expiry_Date,
            'DDC_Date': driver.DDC_Expiry_Date,
            'Report_Date': driver.Report_Date,
            'Expiry_Date': driver.Expiry_Date,
            'Joining_Date': driver.Joining_Date,
            'Salary_Increment_Date': driver.Salary_Increment_Date,
            'Leave_Date': driver.Leave_Date,
            'Leave_Resume': driver.Leave_Resume,
        }
        
        # Calculate the status messages for each date field and add them to the driver object
        for field_name, field_date in date_fields.items():
            if field_date:
                status_message = get_date_status(field_date, field_name)
                setattr(driver, f"{field_name}_status", status_message)
    
    context = {
        'drivers': drivers,
    }
    
    return render(request, 'driver/driver.html', context)

def get_vehicle(request, filter):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    

    
    if filter == 'apl':
        vehicles = Vehicle.objects.filter(OMC_id=4)
        image = '/static/images/attock-logo.png'
    elif filter == 'pso':
        vehicles = Vehicle.objects.filter(OMC_id=6)
        image = '/static/images/pso-logo.png'
    elif filter == 'go':
        vehicles = Vehicle.objects.filter(OMC_id=5)
        image = '/static/images/go-logo.png'
    elif filter == 'tppl':
        omc_ids = [1, 2, 3]
        vehicles = Vehicle.objects.filter(OMC_id__in=omc_ids)
        image = "/static/images/total-logo.png"
    elif filter == 'all':
        vehicles = Vehicle.objects.all()
        image = ''

    def get_date_status(date, field_name):
        current_date =  datetime.now().date()
        days_remaining = (date - current_date).days
        if days_remaining <= 0:
            return f"Expired"
        elif days_remaining <= 90:
            return f"Close to Expiry"
        else:
            return f"Valid"
    
    for vehicle in vehicles:
        # Define a dictionary to store the date fields and their corresponding status messages
        date_fields = {
            'tax_expiry': vehicle.TAX_PAID_Date,
            'fitness_expiry': vehicle.FITNISSE_Date,
            'road_insurance': vehicle.INSURANCE_Date,
            'Dip_Chart': vehicle.DIP_CHART_Date,
            'Q_Fom': vehicle.Q_FOM_Date,
            'Route': vehicle.Route_Permit_Date,
        }
        
        # Calculate the status messages for each date field and add them to the driver object
        for field_name, field_date in date_fields.items():
            if field_date:
                status_message = get_date_status(field_date, field_name)
                setattr(vehicle, f"{field_name}_status", status_message)

    context = {'vehicles': vehicles, 'image': image}
    return render(request, 'vehicle/vehicle.html', context)


def get_vehicle_maker(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    vehicle_makers = VehicleMaker.objects.all()
    context = {'vehicle_makers': vehicle_makers}
    return render(request, 'vehicle_maker/vehicle_makers.html', context)


def get_vehicle_owner(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    vehicle_owners = VehicleOwner.objects.all()
    context = {'vehicle_owners': vehicle_owners}
    return render(request, 'vehicle_owner/vehicle_owner.html', context)


def get_company(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'company/company.html', context)


def logout_user(request):
    logout(request)
    return redirect('/loginuser')


def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    
    total_vehicles = Vehicle.objects.all().count()

    today = date.today()

    # Assuming your Driver model has fields CNIC_Validity, DDC_Expiry, HTV_License_Expiry, and Expiry_Date
    expired_cnic_list = []
    expired_ddc_list = []
    expired_htv_license_list = []
    expired_general_list = []

    # Replace 'Driver' with your actual model name
    drivers = Driver.objects.all()

    for driver in drivers:
        if driver.CNIC_Validity and driver.CNIC_Validity < today:
            expired_cnic_list.append(driver)
        if driver.DDC_Expiry_Date and driver.DDC_Expiry_Date < today:
            expired_ddc_list.append(driver)
        if driver.HTV_License_Expiry_Date and driver.HTV_License_Expiry_Date < today:
            expired_htv_license_list.append(driver)
        if driver.Expiry_Date and driver.Expiry_Date < today:
            expired_general_list.append(driver)

    expired_cnic_list = sorted(expired_cnic_list, key=lambda x: x.D_Name)
    expired_ddc_list = sorted(expired_ddc_list, key=lambda x: x.D_Name)
    expired_htv_license_list = sorted(expired_htv_license_list, key=lambda x: x.D_Name)
    expired_general_list = sorted(expired_general_list, key=lambda x: x.D_Name)

    today = date.today()
    year = today.year
    month = today.month
    cal = calendar.monthcalendar(year, month)
    working_days = 0

    for week in cal:
        for day in week:
            if day != 0 and calendar.weekday(year, month, day) != 6:  # 6 represents Sunday
                working_days += 1

    man_days_work = (58+int(drivers.count()))*working_days

    context = {
        'total_drivers': drivers.count,
        'total_vehicles': total_vehicles,
        'man_days_work': man_days_work,
        'expired_cnic_list': expired_cnic_list,
        'expired_ddc_list': expired_ddc_list,
        'expired_htv_license_list': expired_htv_license_list,
        'expired_general_list': expired_general_list,
    }
    return render(request, 'dashboard.html', context)


def adduser(request):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {'error_head': "You do not have the authority to perform edit or delete operations. ", 'log': 'Log In with Full Access Account.'})

    if request.method == 'POST':
        # Get data from the form
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        access_level = request.POST.get('access-level')
        status = request.POST.get('status')
        user_image = request.FILES.get('user_image')

        is_superuser = 1 if access_level == "Full Access" else 0
        is_active = 1 if status == "Active" else 0

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.save()

        user_image = request.FILES.get('user_image')
        if user_image:
            user_image_obj = User_Image(user=user)
            image = Image.open(user_image)

            width, height = image.size
            new_size = min(width, height)
            
            left = (width - new_size) / 2
            top = (height - new_size) / 2
            right = (width + new_size) / 2
            bottom = (height + new_size) / 2
            image = image.crop((left, top, right, bottom))
            image = image.resize((200, 200), Image.LANCZOS)

            image_data = BytesIO()
            image.save(image_data, format='JPEG')
            user_image_obj.img.save(user_image.name, ContentFile(image_data.getvalue()))
            user_image_obj.save()

        return redirect('/allusers')

    return render(request, 'user/adduser.html', {'heading': "Adding User"})


def deleteuser(request, id):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {'error_head': "You do not have the authority to perform edit or delete operations. ", 'log': 'Log In with Full Access Account.'})
    # Retrieve the user based on the 'id' parameter
    user = User.objects.get(id=id)

    # Delete the user
    user.delete()

    # Redirect to a success page or return a response
    return redirect('/allusers')


def edituser(request, id):
    if not request.user.is_superuser:
        logout_user(request)
        return render(request, 'user/login.html', {'error_head': "You do not have the authority to perform edit or delete operations. ", 'log': 'Log In with Full Access Account.'})
    # Retrieve the user based on the 'id' parameter
    user = User.objects.get(id=id)

    # Retrieve the user's image if it exists
    flag = True
    try:
        user_image_obj = User_Image.objects.get(user=user)
        flag =True
    except User_Image.DoesNotExist:
        user_image_obj = User_Image(user=user)
        flag = False
        
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        access_level = request.POST.get('access-level')
        status = request.POST.get('status')

        is_superuser = 1 if access_level == "Full Access" else 0
        is_active = 1 if status == "Active" else 0

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.save()

        user_image = request.FILES.get('user_image')
        if user_image:
            if flag:
                user_image_obj.delete()
            
            image = Image.open(user_image)
            width, height = image.size
            new_size = min(width, height)
            
            left = (width - new_size) / 2
            top = (height - new_size) / 2
            right = (width + new_size) / 2
            bottom = (height + new_size) / 2
            image = image.crop((left, top, right, bottom))
            image = image.resize((200, 200), Image.LANCZOS)

            image_data = BytesIO()
            image.save(image_data, format='JPEG')

            user_image_obj.img.save(user_image.name, ContentFile(image_data.getvalue()))
            user_image_obj.save()
            
        # Redirect to a success page or return a response
        return redirect('/allusers')
    
    # Populate the form fields with user data and pass the user's image to the template
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
        'user_img': user_image_obj.img,
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
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    # Get all users
    users = User.objects.all()
    # Create a list to store user data with associated user images
    user_data = []

    for user in users:
        # Query the User_Image table for the user's image
        user_image = User_Image.objects.filter(user=user).first()

        user_info = {
            'user': user,
            'user_image': user_image,
        }

        user_data.append(user_info)

    context = {'user_data': user_data}
    return render(request, 'user/users.html', context)



# def update_driver_ages(request):
#     drivers = Driver.objects.all()

#     for driver in drivers:
#         today = date.today()
#         age = today.year - driver.DOB.year - ((today.month, today.day) < (driver.DOB.month, driver.DOB.day))
#         driver.age = age
#         driver.save()

#     return redirect('/drivers')  



def get_tppl(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html', {'error_head': "You must Log In to continue "})
    vehicles = Vehicle.objects.all()

    def get_date_status(date, field_name):
        current_date =  datetime.now().date()
        days_remaining = (date - current_date).days
        if days_remaining <= 0:
            return f"Expired"
        elif days_remaining <= 90:
            return f"Close to Expiry"
        else:
            return f"Valid"
    
    for vehicle in vehicles:
        # Define a dictionary to store the date fields and their corresponding status messages
        date_fields = {
            'tax_expiry': vehicle.TAX_PAID_Date,
            'fitness_expiry': vehicle.FITNISSE_Date,
            'road_insurance': vehicle.INSURANCE_Date,
            'Dip_Chart': vehicle.DIP_CHART_Date,
            'Q_Fom': vehicle.Q_FOM_Date,
            'Route': vehicle.Route_Permit_Date,
        }
        
        # Calculate the status messages for each date field and add them to the driver object
        for field_name, field_date in date_fields.items():
            if field_date:
                status_message = get_date_status(field_date, field_name)
                setattr(vehicle, f"{field_name}_status", status_message)

    context = {'vehicles': vehicles}
    return render(request, 'vehicle/vehicle.html', context)


def get_procedures(request):
    return render(request, 'static_content/procedures.html')


def get_emergency_procedures(request):
    return render(request, 'static_content/eprocedures.html')


def get_policies(request):
    return render(request, 'static_content/policies.html')
