from datetime import date
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


# ------------------------------------------------------------------------------
# Choice constants example
# ------------------------------------------------------------------------------
HTV = 'HTV'
PSV = 'PSV'
LTV = 'LTV'

DL_STATUS_CHOICES = [
    (HTV, 'HTV'),
    (PSV, 'PSV'),
    (LTV, 'LTV'),
]


# ------------------------------------------------------------------------------
# Company
# ------------------------------------------------------------------------------
class Company(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Company ID")
    abbreviation = models.CharField(
        max_length=10,
        verbose_name="Abbreviation"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Company Name"
    )

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# VehicleMaker
# ------------------------------------------------------------------------------
class VehicleMaker(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Vehicle Maker ID")
    name = models.CharField(max_length=255, verbose_name="Vehicle Maker Name")

    class Meta:
        verbose_name_plural = "Vehicle Makers"

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# VehicleOwner
# ------------------------------------------------------------------------------
class VehicleOwner(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Vehicle Owner ID")
    name = models.CharField(max_length=255, verbose_name="Vehicle Owner Name")

    class Meta:
        verbose_name_plural = "Vehicle Owners"

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# Vehicle
# ------------------------------------------------------------------------------
class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    tl_number = models.CharField(max_length=255, null=True, verbose_name="TL Number")
    capacity = models.IntegerField(null=True, verbose_name="Capacity")
    chambers = models.CharField(max_length=255, null=True, verbose_name="Chambers")

    omc = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Oil Marketing Company"
    )
    maker = models.ForeignKey(
        VehicleMaker,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Maker"
    )
    model = models.IntegerField(null=True, verbose_name="Model")
    engine_number = models.CharField(max_length=255, null=True, verbose_name="Engine Number")
    chassis_number = models.CharField(max_length=255, null=True, verbose_name="Chassis Number")

    lease_company = models.ForeignKey(
        VehicleOwner,
        on_delete=models.CASCADE,
        null=True,
        related_name="lease_company_vehicles",
        verbose_name="Lease Company"
    )
    lease_bank = models.ForeignKey(
        VehicleOwner,
        on_delete=models.CASCADE,
        null=True,
        related_name="lease_bank_vehicles",
        verbose_name="Lease Bank"
    )
    status = models.CharField(max_length=255, null=True, verbose_name="Status")
    vehicle_type = models.CharField(max_length=255, null=True, verbose_name="Type")
    trailer_id = models.CharField(max_length=255, null=True, verbose_name="Trailer ID")
    brand = models.CharField(max_length=255, null=True, verbose_name="Brand")
    nha_configuration_class = models.CharField(
        max_length=255,
        null=True,
        verbose_name="NHA Configuration Class"
    )
    gross_empty_trailer_weight = models.CharField(
        max_length=255,
        null=True,
        verbose_name="Gross Empty Trailer Weight"
    )

    dip_chart_date = models.DateField(null=True, verbose_name="DIP CHART Date")
    insurance_date = models.DateField(null=True, verbose_name="Insurance Date")
    tax_paid_date = models.DateField(null=True, verbose_name="Tax Paid Date")
    fitness_date = models.DateField(null=True, verbose_name="Fitness Date")
    q_fom_date = models.DateField(null=True, verbose_name="Q FOM Date")
    route_permit_date = models.DateField(null=True, verbose_name="Route Permit Date")

    class Meta:
        verbose_name_plural = "Vehicles"

    def __str__(self):
        # Example: Return TL Number if you prefer
        return self.tl_number if self.tl_number else f"Vehicle {self.id}"


# ------------------------------------------------------------------------------
# Location
# ------------------------------------------------------------------------------
class Location(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Location ID")
    name = models.CharField(max_length=255, verbose_name="Location Name")

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# Driver
# ------------------------------------------------------------------------------
class Driver(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Driver ID")
    driver_number = models.CharField(max_length=20, null=True, verbose_name="Driver Number")
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Oil Marketing Company"
    )
    image = models.ImageField(
        max_length=500,
        null=True,
        blank=True,
        upload_to='driver_images/',
        verbose_name="Driver Image"
    )
    name = models.CharField(max_length=255, null=True, verbose_name="Driver Name")
    father_name = models.CharField(max_length=255, null=True, verbose_name="Father Name")
    cnic = models.CharField(max_length=13, null=True, verbose_name="CNIC")
    cnic_validity = models.DateField(null=True, blank=True, verbose_name="CNIC Validity Date")
    cell_phone_num = models.CharField(max_length=20, null=True, verbose_name="Cell Phone Number")
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")

    dl_status = models.CharField(
        max_length=3,
        choices=DL_STATUS_CHOICES,
        null=True,
        verbose_name="Driving License Status"
    )
    motorway_trained = models.CharField(
        max_length=14,
        null=True,
        verbose_name="Motorway Trained"
    )
    ddc_issue_date = models.DateField(null=True, blank=True, verbose_name="Motorway Certification Issue Date")
    address = models.TextField(null=True, verbose_name="Address")
    license_no = models.CharField(max_length=20, null=True, verbose_name="License Number")
    htv_license_authority = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="HTV License Authority"
    )
    htv_license_issue_date = models.DateField(null=True, blank=True, verbose_name="HTV License Issue Date")
    htv_license_expiry_date = models.DateField(null=True, blank=True, verbose_name="HTV License Expiry Date")
    ddc_expiry_date = models.DateField(null=True, blank=True, verbose_name="DDC Expiry Date")

    education = models.CharField(max_length=16, null=True, verbose_name="Education")

    medical_status = models.BooleanField(null=True, verbose_name="Medical Status")
    medical_report_date = models.DateField(null=True, blank=True, verbose_name="Medical Report Date")
    lab_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lab Name")
    medical_expiry_date = models.DateField(null=True, blank=True, verbose_name="Medical Expiry Date")
    blood_group = models.CharField(max_length=10, verbose_name="Blood Group")

    medical_health = models.CharField(max_length=5, null=True, verbose_name="Medical Health")

    joining_date = models.DateField(null=True, blank=True, verbose_name="Joining Date")
    salary_increment_date = models.DateField(null=True, blank=True, verbose_name="Salary Increment Date")
    experience = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        verbose_name="Experience (years)"
    )
    leave_date = models.DateField(null=True, blank=True, verbose_name="Leave Date")
    leave_resume_date = models.DateField(null=True, blank=True, verbose_name="Leave Resume Date")
    driving_age = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        verbose_name="Driving Age (years)"
    )
    previous_company = models.CharField(max_length=255, null=True, blank=True, verbose_name="Previous Company")
    tank_lorry = models.CharField(max_length=255, null=True, verbose_name="Tank Lorry")

    # Computed field
    age = models.IntegerField(blank=True, null=True, verbose_name="Age")

    class Meta:
        verbose_name_plural = "Drivers"

    def save(self, *args, **kwargs):
        if self.dob:
            today = date.today()
            self.age = today.year - self.dob.year - (
                (today.month, today.day) < (self.dob.month, self.dob.day)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else f"Driver {self.id}"


# ------------------------------------------------------------------------------
# User Image
# ------------------------------------------------------------------------------
class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        max_length=500,
        null=True,
        upload_to='user_images/',
        verbose_name="User Image"
    )


# ------------------------------------------------------------------------------
# AnnualTraining
# ------------------------------------------------------------------------------
class AnnualTraining(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Training Name")
    training_month = models.CharField(max_length=50, verbose_name="Training Month")

    class Meta:
        verbose_name = "HSE Training"
        verbose_name_plural = "HSE Trainings"

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# AnnualDrill
# ------------------------------------------------------------------------------
class AnnualDrill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Drill Name")
    drilling_month = models.CharField(max_length=50, verbose_name="Drill Month")

    class Meta:
        verbose_name = "Drill Training"
        verbose_name_plural = "Drill Trainings"

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# AnnualDrillDriver
# ------------------------------------------------------------------------------
class AnnualDrillDriver(models.Model):
    id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="Driver")

    train1_completed_date = models.DateField(null=True, blank=True)
    train2_completed_date = models.DateField(null=True, blank=True)
    train3_completed_date = models.DateField(null=True, blank=True)
    train4_completed_date = models.DateField(null=True, blank=True)
    train5_completed_date = models.DateField(null=True, blank=True)
    train6_completed_date = models.DateField(null=True, blank=True)
    train7_completed_date = models.DateField(null=True, blank=True)
    train8_completed_date = models.DateField(null=True, blank=True)
    train9_completed_date = models.DateField(null=True, blank=True)
    train10_completed_date = models.DateField(null=True, blank=True)
    train11_completed_date = models.DateField(null=True, blank=True)
    train12_completed_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Drill Driver"
        verbose_name_plural = "Drill Drivers"


# ------------------------------------------------------------------------------
# AnnualTrainingDriver
# ------------------------------------------------------------------------------
class AnnualTrainingDriver(models.Model):
    id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="Driver")

    train1_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN1 Completed Date")
    train2_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN2 Completed Date")
    train3_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN3 Completed Date")
    train4_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN4 Completed Date")
    train5_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN5 Completed Date")
    train6_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN6 Completed Date")
    train7_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN7 Completed Date")
    train8_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN8 Completed Date")
    train9_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN9 Completed Date")
    train10_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN10 Completed Date")
    train11_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN11 Completed Date")
    train12_completed_date = models.DateField(null=True, blank=True, verbose_name="TRAIN12 Completed Date")

    class Meta:
        verbose_name = "HSE Training Driver"
        verbose_name_plural = "HSE Training Drivers"


# ------------------------------------------------------------------------------
# Violations
# ------------------------------------------------------------------------------
class Violation(models.Model):
    id = models.AutoField(primary_key=True)
    violation_type = models.CharField(max_length=255, verbose_name="Violation Type")

    class Meta:
        verbose_name = "Violation"
        verbose_name_plural = "Violations"

    def __str__(self):
        return self.violation_type


# ------------------------------------------------------------------------------
# DriverViolation
# ------------------------------------------------------------------------------
class DriverViolation(models.Model):
    id = models.AutoField(primary_key=True)
    violation = models.ForeignKey(
        Violation,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Violation"
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Driver"
    )
    violation_date = models.DateField(null=True, verbose_name="Violation Date")
    violation_notes = models.TextField(null=True, verbose_name="Violation Notes")

    class Meta:
        verbose_name = "Driver Violation"
        verbose_name_plural = "Driver Violations"

    def __str__(self):
        # Safely handle if driver or violation is None
        driver_name = self.driver.name if self.driver else "Unknown Driver"
        violation_name = self.violation.violation_type if self.violation else "Unknown Violation"
        return f"{driver_name} - {violation_name} - {self.violation_date}"


# ------------------------------------------------------------------------------
# ToolBoxMeetingTopic
# ------------------------------------------------------------------------------
class ToolBoxMeetingTopic(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255, verbose_name="Tool Box Meeting Topic")

    class Meta:
        verbose_name = "Tool Box Meeting"
        verbose_name_plural = "Tool Box Meetings"

    def __str__(self):
        return self.topic


# ------------------------------------------------------------------------------
# DriverToolBoxMeetingAttended
# ------------------------------------------------------------------------------
class DriverToolBoxMeetingAttended(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_topic = models.ForeignKey(
        ToolBoxMeetingTopic,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Meeting Topic"
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Driver"
    )
    no_of_times_attended = models.IntegerField(verbose_name="Times Attended")

    def __str__(self):
        driver_name = self.driver.name if self.driver else "Unknown Driver"
        topic_name = self.meeting_topic.topic if self.meeting_topic else "Unknown Topic"
        return f"{driver_name} attended '{topic_name}' {self.no_of_times_attended} time(s)"
