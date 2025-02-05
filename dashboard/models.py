from datetime import date
from django.db import models

from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Company(models.Model):
    cid = models.AutoField(primary_key=True, verbose_name="Company ID")
    cabb = models.CharField(
        max_length=10, verbose_name="Company Name abbreviation ")
    cname = models.CharField(max_length=255, verbose_name="Company Name")

    def __str__(self):
        return self.cname

    class Meta:
        verbose_name_plural = "Companies"


class VehicleMaker(models.Model):
    VMid = models.AutoField(primary_key=True, verbose_name="Vehicle Maker ID")
    VMNAME = models.CharField(
        max_length=255, verbose_name="Vehicle Maker Name")

    def __str__(self):
        return self.VMNAME

    class Meta:
        verbose_name_plural = "Vehicle Makers"


class VehicleOwner(models.Model):
    VO_id = models.AutoField(primary_key=True, verbose_name="Vehicle Owner ID")
    VO_name = models.CharField(
        max_length=255, verbose_name="Vehicle Owner Name")

    def __str__(self):
        return self.VO_name

    class Meta:
        verbose_name_plural = "Vehicle Owners"


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    TL_Number = models.CharField(max_length=255, null=True)
    Capacity = models.IntegerField(null=True)
    Chambers = models.CharField(max_length=255, null=True)
    OMC = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    Make = models.ForeignKey(VehicleMaker, on_delete=models.CASCADE, null=True)
    Model = models.IntegerField(null=True)
    Engine_Number = models.CharField(max_length=255, null=True)
    Chassis_Number = models.CharField(max_length=255, null=True)
    LEASE_COMPANY = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE, null=True, related_name="Vehicle_Owner_Lease")
    LEASE_BANK = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE, null=True, related_name="Vehicle_Owner_Bank")
    Status = models.CharField(max_length=255, null=True)
    Type = models.CharField(max_length=255, null=True)
    Trailer_ID = models.CharField(max_length=255, null=True)
    Brand = models.CharField(max_length=255, null=True)
    NHA_Configuration_Class = models.CharField(max_length=255, null=True)
    Gross_Empty_Trailer_Weight = models.CharField(max_length=255, null=True)
    DIP_CHART_Date = models.DateField(null=True)
    INSURANCE_Date = models.DateField(null=True)
    TAX_PAID_Date = models.DateField(null=True)
    FITNISSE_Date = models.DateField(null=True)
    Q_FOM_Date = models.DateField(null=True)
    Route_Permit_Date = models.DateField(null=True)

    def __str__(self):
        return self.VH_number

    class Meta:
        verbose_name_plural = "Vehicles"


class Location(models.Model):
    LID = models.AutoField(primary_key=True, verbose_name="Location ID")
    Lname = models.CharField(max_length=255, verbose_name="Location Name")

    def __str__(self):
        return self.Lname

    class Meta:
        verbose_name_plural = "Locations"


class Driver(models.Model):
    D_ID = models.AutoField(primary_key=True, verbose_name="Driver ID")
    D_Number = models.CharField(max_length=20, verbose_name="Driver Number",  null=True)
    Oil_Marketing_Company = models.ForeignKey(
        'Company', on_delete=models.CASCADE,
        verbose_name="Oil Marketing Company", null=True)
    D_Image = models.ImageField(max_length=500, null=True, blank=True,
                                upload_to='driver_images/')
    D_Name = models.CharField(max_length=255, verbose_name="Driver Name", null=True)
    Father_Name = models.CharField(max_length=255, verbose_name="Father Name", null=True)
    CNIC = models.CharField(max_length=13, null=True)
    CNIC_Validity = models.DateField(verbose_name="CNIC Validity Date",
                                     null=True, blank=True)
    Cell_Phone_Num = models.CharField(
        max_length=20, verbose_name="Cell Phone Number", null=True)
    DOB = models.DateField(verbose_name="Date of Birth", null=True, blank=True)

    # Choices for DL_Status field
    DL_STATUS_CHOICES = [
        ('HTV', 'HTV'),
        ('PSV', 'PSV'),
        ('LTV', 'LTV'),
    ]
    DL_Status = models.CharField(
        max_length=3, choices=DL_STATUS_CHOICES,
        verbose_name="Driving License Status", null=True)
    Motorway_Trained = models.CharField(max_length=14,
                                        verbose_name="Motorway Trained", null=True)
    DDC_Issue_Date = models.DateField(
        verbose_name="Motorway Certification Issue Date", null=True,
        blank=True)
    Address = models.TextField(verbose_name="Address", null=True)
    License_No = models.CharField(max_length=20, verbose_name="License Number", null=True)
    HTV_License_Authority = models.ForeignKey('Location',
                                              on_delete=models.CASCADE,
                                              verbose_name="HTV License Authority",
                                              null=True)
    HTV_License_Issue_Date = models.DateField(
        verbose_name="HTV License Issue Date", null=True, blank=True)
    HTV_License_Expiry_Date = models.DateField(
        verbose_name="HTV License Expiry Date", null=True, blank=True)
    DDC_Expiry_Date = models.DateField(verbose_name="DDC Date", null=True, blank=True)

    Education = models.CharField(
        max_length=16, verbose_name="Education", null=True)

    Medical = models.BooleanField(verbose_name="Medical Status", null=True)
    Report_Date = models.DateField(
        null=True, blank=True, verbose_name="Medical Report Date")
    Lab_Name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Lab Name")
    Expiry_Date = models.DateField(
        null=True, blank=True, verbose_name="Medical Expiry Date")
    Blood_Group = models.CharField(
        max_length=10, verbose_name="Blood Group")

    Medical_Health = models.CharField(
        max_length=5, verbose_name="Medical Health", null=True)

    Joining_Date = models.DateField(verbose_name="Joining Date", null=True,
                                    blank=True)
    Salary_Increment_Date = models.DateField(
        verbose_name="Salary Increment Date", null=True, blank=True)
    Experience = models.PositiveIntegerField(
        validators=[MinValueValidator(0)], verbose_name="Experience (years)", null=True)
    Leave_Date = models.DateField(
        null=True, blank=True, verbose_name="Leave Date")
    Leave_Resume = models.DateField(
        null=True, blank=True, verbose_name="Leave Resume Date")
    Driving_Age = models.PositiveIntegerField(
        validators=[MinValueValidator(0)], verbose_name="Driving Age (years)", null=True)
    Previous_Company = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Previous Company")
    Tank_Lorry = models.CharField(max_length=255, verbose_name="Tank Lorry", null=True)
    age = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        today = date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        self.age = age
        super(Driver, self).save(*args, **kwargs)

    def __str__(self):
        return self.D_Name

    class Meta:
        verbose_name_plural = "Drivers"


class User_Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(max_length=500, null=True, upload_to='user_images/')


class annual_training(models.Model):
    id = models.AutoField(primary_key=True)
    train_name = models.CharField(max_length=255, verbose_name="Training Name")
    training_month = models.CharField(max_length=50, verbose_name="Training Month")

    def __str__(self):
        return self.train_name

    class Meta:
        verbose_name = "HSE Training"
        verbose_name_plural = "HSE Trainings"


class annual_drill(models.Model):
    id = models.AutoField(primary_key=True)
    drill_name = models.CharField(max_length=255, verbose_name="Drill Name")
    drilling_month = models.CharField(max_length=50, verbose_name="Dril Month")

    def __str__(self):
        return self.drill_name

    class Meta:
        verbose_name = "Drill Training"
        verbose_name_plural = "Drill Trainings"


class annual_drill_driver(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="User")
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
        verbose_name = "Dril Driver"
        verbose_name_plural = "Drill Drivers"


class annual_training_driver(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="User")

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


class Violations(models.Model):
    id = models.AutoField(primary_key=True)
    violation_type = models.CharField(max_length=255, verbose_name="Violation Type")

    def __str__(self):
        return self.violation_type

    class Meta:
        verbose_name = "Violation"
        verbose_name_plural = "Violations"


class Driver_Violation(models.Model):
    id = models.AutoField(primary_key=True)
    violation = models.ForeignKey(Violations, on_delete=models.CASCADE,
                                  verbose_name="Violation", null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               verbose_name="Driver", null=True)
    violation_date = models.DateField(verbose_name="Violation Date", null=True)
    violation_notes = models.TextField(null=True)

    def __str__(self):
        return f"{self.driver} - {self.violation} - {self.violation_date}"

    class Meta:
        verbose_name = "Driver Violation"
        verbose_name_plural = "Driver Violations"


class tool_box_meeting_topics(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_topic = models.CharField(max_length=255, verbose_name="Tool Box Meeting Topic")

    def __str__(self):
        return self.meeting_topic

    class Meta:
        verbose_name = "Tool Box Meeting"
        verbose_name_plural = "Tool Box Meetings"


class driver_tool_box_meeting_attended(models.Model):
    id = models.AutoField(primary_key=True)

    # This is topic of the meeting
    meetings_attended = models.ForeignKey(tool_box_meeting_topics, on_delete=models.CASCADE, null=True)

    # This is the Driver ID who has attended the meeting
    meeting_attended_by = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)

    # This is the no of times a single meeting is attended by the driver
    no_of_times_meeting_attended = models.IntegerField()
