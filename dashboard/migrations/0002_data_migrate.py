# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations

def forwards(apps, schema_editor):
    # === Insert Django default tables data (except migrations) ===

    # -- auth_permission --
    AuthPermission = apps.get_model('auth', 'Permission')
    auth_permissions = [
        (1, 'Can add log entry', 1, 'add_logentry'),
        (2, 'Can change log entry', 1, 'change_logentry'),
        (3, 'Can delete log entry', 1, 'delete_logentry'),
        (4, 'Can view log entry', 1, 'view_logentry'),
        (5, 'Can add permission', 2, 'add_permission'),
        (6, 'Can change permission', 2, 'change_permission'),
        (7, 'Can delete permission', 2, 'delete_permission'),
        (8, 'Can view permission', 2, 'view_permission'),
        (9, 'Can add group', 3, 'add_group'),
        (10, 'Can change group', 3, 'change_group'),
        (11, 'Can delete group', 3, 'delete_group'),
        (12, 'Can view group', 3, 'view_group'),
        (13, 'Can add user', 4, 'add_user'),
        (14, 'Can change user', 4, 'change_user'),
        (15, 'Can delete user', 4, 'delete_user'),
        (16, 'Can view user', 4, 'view_user'),
        (17, 'Can add content type', 5, 'add_contenttype'),
        (18, 'Can change content type', 5, 'change_contenttype'),
        (19, 'Can delete content type', 5, 'delete_contenttype'),
        (20, 'Can view content type', 5, 'view_contenttype'),
        (25, 'Can add company', 7, 'add_company'),
        (26, 'Can change company', 7, 'change_company'),
        (27, 'Can delete company', 7, 'delete_company'),
        (28, 'Can view company', 7, 'view_company'),
        (29, 'Can add location', 8, 'add_location'),
        (30, 'Can change location', 8, 'change_location'),
        (31, 'Can delete location', 8, 'delete_location'),
        (32, 'Can view location', 8, 'view_location'),
        (33, 'Can add product', 9, 'add_product'),
        (34, 'Can change product', 9, 'change_product'),
        (35, 'Can delete product', 9, 'delete_product'),
        (36, 'Can view product', 9, 'view_product'),
        (37, 'Can add vehicle maker', 10, 'add_vehiclemaker'),
        (38, 'Can change vehicle maker', 10, 'change_vehiclemaker'),
        (39, 'Can delete vehicle maker', 10, 'delete_vehiclemaker'),
        (40, 'Can view vehicle maker', 10, 'view_vehiclemaker'),
        (41, 'Can add vehicle owner', 11, 'add_vehicleowner'),
        (42, 'Can change vehicle owner', 11, 'change_vehicleowner'),
        (43, 'Can delete vehicle owner', 11, 'delete_vehicleowner'),
        (44, 'Can view vehicle owner', 11, 'view_vehicleowner'),
        (45, 'Can add vehicle', 12, 'add_vehicle'),
        (46, 'Can change vehicle', 12, 'change_vehicle'),
        (47, 'Can delete vehicle', 12, 'delete_vehicle'),
        (48, 'Can view vehicle', 12, 'view_vehicle'),
        (49, 'Can add driver', 13, 'add_driver'),
        (50, 'Can change driver', 13, 'change_driver'),
        (51, 'Can delete driver', 13, 'delete_driver'),
        (52, 'Can view driver', 13, 'view_driver'),
        (53, 'Can add user_ image', 14, 'add_user_image'),
        (54, 'Can change user_ image', 14, 'change_user_image'),
        (55, 'Can delete user_ image', 14, 'delete_user_image'),
        (56, 'Can view user_ image', 14, 'view_user_image'),
        (57, 'Can add HSE Training', 15, 'add_hse_training'),
        (58, 'Can change HSE Training', 15, 'change_hse_training'),
        (59, 'Can delete HSE Training', 15, 'delete_hse_training'),
        (60, 'Can view HSE Training', 15, 'view_hse_training'),
        (61, 'Can add Violation', 16, 'add_violations'),
        (62, 'Can change Violation', 16, 'change_violations'),
        (63, 'Can delete Violation', 16, 'delete_violations'),
        (64, 'Can view Violation', 16, 'view_violations'),
        (65, 'Can add Driver Violation', 17, 'add_driver_violation'),
        (66, 'Can change Driver Violation', 17, 'change_driver_violation'),
        (67, 'Can delete Driver Violation', 17, 'delete_driver_violation'),
        (68, 'Can view Driver Violation', 17, 'view_driver_violation'),
        (69, 'Can add HSE Training', 15, 'add_annual_training'),
        (70, 'Can change HSE Training', 15, 'change_annual_training'),
        (71, 'Can delete HSE Training', 15, 'delete_annual_training'),
        (72, 'Can view HSE Training', 15, 'view_annual_training'),
        (73, 'Can add HSE Training Driver', 18, 'add_annual_training_driver'),
        (74, 'Can change HSE Training Driver', 18, 'change_annual_training_driver'),
        (75, 'Can delete HSE Training Driver', 18, 'delete_annual_training_driver'),
        (76, 'Can view HSE Training Driver', 18, 'view_annual_training_driver'),
        (77, 'Can add Drill Training', 19, 'add_annual_drill'),
        (78, 'Can change Drill Training', 19, 'change_annual_drill'),
        (79, 'Can delete Drill Training', 19, 'delete_annual_drill'),
        (80, 'Can view Drill Training', 19, 'view_annual_drill'),
        (81, 'Can add Dril Driver', 20, 'add_annual_drill_driver'),
        (82, 'Can change Dril Driver', 20, 'change_annual_drill_driver'),
        (83, 'Can delete Dril Driver', 20, 'delete_annual_drill_driver'),
        (84, 'Can view Dril Driver', 20, 'view_annual_drill_driver'),
        (85, 'Can add Tool Box Meeting', 21, 'add_tool_box_meeting_topics'),
        (86, 'Can change Tool Box Meeting', 21, 'change_tool_box_meeting_topics'),
        (87, 'Can delete Tool Box Meeting', 21, 'delete_tool_box_meeting_topics'),
        (88, 'Can view Tool Box Meeting', 21, 'view_tool_box_meeting_topics'),
        (89, 'Can add driver_tool_box_meeting_attended', 22, 'add_driver_tool_box_meeting_attended'),
        (90, 'Can change driver_tool_box_meeting_attended', 22, 'change_driver_tool_box_meeting_attended'),
        (91, 'Can delete driver_tool_box_meeting_attended', 22, 'delete_driver_tool_box_meeting_attended'),
        (92, 'Can view driver_tool_box_meeting_attended', 22, 'view_driver_tool_box_meeting_attended'),
    ]
    for id_val, name, content_type_id, codename in auth_permissions:
        AuthPermission.objects.create(
            id=id_val,
            name=name,
            content_type_id=content_type_id,
            codename=codename
        )

    # -- auth_user --
    AuthUser = apps.get_model('auth', 'User')
    auth_users = [
        (1, 'pbkdf2_sha256$600000$K0DY6Mqts9lQ0tGgfyzxUw$MdVJbDhePrGFs0JyNwEhpZSpDR07R5rRSQ2DhaU6tkc=', '2023-10-25 18:17:41.078755', 1, 'awb', 'Abdul Wahab', 'Butt', 'leo.awb@gmail.com', 1, 1, '2023-10-15 09:09:12.618367'),
        (10, 'pbkdf2_sha256$600000$1WtIliSCNb1O0vFa0BEML9$Jdhz7msJgitDIpp8sNjOtSlhfV7ndTFs6b1HAZSN00A=', None, 0, 'HE', 'MEMME', 'NONEE', '', 0, 1, '2023-10-22 09:20:17.316443'),
        (12, 'pbkdf2_sha256$600000$UMINXFvI6FzPcWheC4SK2k$SjLKFTQ0FBaF7bSxeR1zUeCtJOHs/l48V6EB2yGUMN8=', None, 1, 'maria', 'FROSS', 'MARIA', '', 0, 0, '2023-10-22 09:47:52.035274'),
        (15, 'pbkdf2_sha256$600000$4ZBOSTNyBjP27VPVXMPBKP$yHabkNHtzyvqp2xHjMH1XKwpSN7iu7Py5rBHtmrQx3E=', None, 0, 'awbbb', 'Abdul Wahab', 'Butt', '', 0, 1, '2023-10-22 10:56:46.281376'),
        (20, 'pbkdf2_sha256$600000$iHCQ70fKrR6zzKi0Mr8jWp$SZHM4LYMCEZ30sDPJG1Ir9pBc4qBsVc8ioVIhc/ApaA=', None, 0, 'a', 'MEMME', 'NONEE', '', 0, 1, '2023-10-25 18:22:07.890519'),
        (21, 'pbkdf2_sha256$600000$5aHVBhXUOqpWk3iZ6Dd9Jd$VDm6KHnQpb5INl3mnGvGsdD4SL8OhFg0LkHZ06ijIfc=', None, 0, '1', 'a', 'a', '', 0, 1, '2023-10-25 18:26:23.735621'),
        (24, 'pbkdf2_sha256$600000$3dXaUvZXcG3Jn8zPkrhsjX$Lxjf9hHCmKRLzgWWhfQRrFHbrju2c2bR+D+l2Tk43Z4=', None, 0, 'b', 'a', 'a', '', 0, 1, '2023-10-25 18:29:59.702214'),
    ]
    for id_val, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined in auth_users:
        AuthUser.objects.create(
            id=id_val,
            password=password,
            last_login=last_login,
            is_superuser=is_superuser,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            date_joined=date_joined
        )

    # -- django_admin_log --
    AdminLog = apps.get_model('admin', 'LogEntry')
    admin_logs = [
        (1, '2023-10-15 09:10:08.112098', '2', 'hello', 1, '[{"added": {}}]', 4, 1),
        (2, '2023-10-15 09:10:29.968843', '2', 'hello', 2, '[]', 4, 1),
        (3, '2023-10-15 09:10:43.936645', '2', 'test_user', 2, '[{"changed": {"fields": ["Username"]}}]', 4, 1),
    ]
    for id_val, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id in admin_logs:
        AdminLog.objects.create(
            id=id_val,
            action_time=action_time,
            object_id=object_id,
            object_repr=object_repr,
            action_flag=action_flag,
            change_message=change_message,
            content_type_id=content_type_id,
            user_id=user_id,
        )

    # -- django_content_type --
    ContentType = apps.get_model('contenttypes', 'ContentType')
    content_types = [
        (1, 'admin', 'logentry'),
        (3, 'auth', 'group'),
        (2, 'auth', 'permission'),
        (4, 'auth', 'user'),
        (5, 'contenttypes', 'contenttype'),
        (19, 'dashboard', 'annual_drill'),
        (20, 'dashboard', 'annual_drill_driver'),
        (15, 'dashboard', 'annual_training'),
        (18, 'dashboard', 'annual_training_driver'),
        (7, 'dashboard', 'company'),
        (13, 'dashboard', 'driver'),
        (22, 'dashboard', 'driver_tool_box_meeting_attended'),
        (17, 'dashboard', 'driver_violation'),
        (8, 'dashboard', 'location'),
        (9, 'dashboard', 'product'),
        (21, 'dashboard', 'tool_box_meeting_topics'),
        (14, 'dashboard', 'user_image'),
        (12, 'dashboard', 'vehicle'),
        (10, 'dashboard', 'vehiclemaker'),
        (11, 'dashboard', 'vehicleowner'),
        (16, 'dashboard', 'violations'),
    ]
    for id_val, app_label, model in content_types:
        ContentType.objects.create(
            id=id_val,
            app_label=app_label,
            model=model
        )

    # === Insert Dashboard (app "dashboard") independent data ===

    # -- AnnualDrill --
    AnnualDrill = apps.get_model('dashboard', 'annual_drill')
    drills = [
        (1, 'First Aid', 'Jan'),
        (2, 'Fire Drill', 'Feb'),
        (3, 'Law & Order Situation', 'Mar'),
        (4, 'Breakdown Maintenance', 'Apr'),
        (5, 'Fire Evacuation', 'May'),
        (6, 'Road Accident', 'Jun'),
        (7, 'Heat Stroke', 'Jul'),
        (8, 'Spill', 'Aug'),
        (9, 'Heart Attack', 'Sep'),
        (10, 'Tyre Burst', 'Oct'),
        (11, 'Bomb Threat', 'Nov'),
        (12, 'Mega Drill', 'Dec'),
    ]
    for id_val, name, month in drills:
        AnnualDrill.objects.create(id=id_val, drill_name=name, drilling_month=month)

    # -- AnnualTraining --
    AnnualTraining = apps.get_model('dashboard', 'annual_training')
    trainings = [
        (1, 'Company Policies', 'Jan'),
        (2, 'Product Knowledge/Handling & associated Hazards', 'Feb'),
        (3, 'Vehicle Inspection', 'Mar'),
        (4, 'Journey Management ', 'Apr'),
        (5, 'Emergency Response', 'May'),
        (6, 'Internal DDC ', 'Jun'),
        (7, 'Vehicle Roll over Prevention', 'Jul'),
        (8, 'ABS Brake System', 'Aug'),
        (9, 'Loading and Un-Loading', 'Sep'),
        (10, 'First Aid Induction', 'Oct'),
        (11, 'Fatigue Management', 'Nov'),
        (12, 'Fire Extinguisher Use', 'Dec'),
    ]
    for id_val, name, month in trainings:
        AnnualTraining.objects.create(id=id_val, train_name=name, training_month=month)

    # -- Company --
    Company = apps.get_model('dashboard', 'Company')
    companies = [
        (1, 'TPPL', 'Total Parco Pakistan Limited'),
        (2, 'TPPL MHK', 'Total Parco Pakistan Limited MHK'),
        (3, 'TPPL MCH', 'Total Parco Pakistan Limited MCH'),
    ]
    for cid, cabb, cname in companies:
        Company.objects.create(cid=cid, cabb=cabb, cname=cname)

    # -- Location --
    Location = apps.get_model('dashboard', 'location')
    locations = [
        (1, 'Peshawar'),
        (2, 'Lakki Marwat'),
        (3, 'Muzaaffargarh'),
        (4, 'Tank'),
        (5, 'Charsadda'),
        (6, 'Karachi'),
        (7, 'Mir Pur Khaas'),
        (8, 'Kohistan'),
        (9, 'Sheikhupura'),
        (10, 'Islamabad'),
        (11, 'Nowshera'),
    ]
    for LID, Lname in locations:
        Location.objects.create(LID=LID, Lname=Lname)

    # -- ToolBoxMeetingTopics --
    ToolBoxMeetingTopics = apps.get_model('dashboard', 'tool_box_meeting_topics')
    topics = [
        (1, 'Syndicate Sessions'),
        (2, 'Heat stress management'),
        (3, 'Pre-load inspection'),
        (4, 'Safe decantation at Retail Site'),
        (5, 'Roll over prevention'),
        (6, 'Fatigue management'),
        (7, 'Defensive driving'),
        (8, 'Unauthorized passenger'),
        (9, 'Loading & Unloading'),
        (10, '360 walkabout process'),
        (11, 'Vehicle fitness'),
        (12, 'Emergency response'),
        (13, "PPE's compliance"),
        (14, 'Duty & driving hours'),
        (15, 'On-Road distraction'),
        (16, 'Security awareness'),
        (17, 'Manual Handling'),
        (18, 'Working at height'),
        (19, 'Adverse weather condition'),
        (20, 'Static charge'),
        (21, 'Driver behaviour on road'),
        (22, 'Foggy weather'),
        (23, 'Sugarcane Trolleys Hazards and Controls'),
        (24, 'NMPI Reporting'),
        (25, 'Black spots'),
        (26, 'Stop Work Policy'),
        (27, 'Driver Handbook'),
        (28, 'Vehicle Documents Checking'),
        (29, 'Hot Work (PTW)'),
        (30, 'Journey management compliance'),
        (31, 'Company policies'),
        (32, 'Seat belt Advantages'),
        (33, 'Pre-Trip Briefing'),
        (34, 'MSDS'),
        (35, 'Mobile phone Risks'),
        (36, 'Slip-trip & fall'),
        (37, 'Distraction on road'),
        (38, 'Safe Distance'),
        (39, 'D&A Policy'),
        (40, 'Use Slow Lane'),
        (41, 'Route Hazards'),
        (42, 'Depot Rules & Regulations'),
        (43, 'Safe Parking'),
        (44, 'Reverse Precautions'),
        (45, 'Product Knowledge'),
        (46, 'TPPL Policies'),
    ]
    for id_val, topic in topics:
        ToolBoxMeetingTopics.objects.create(id=id_val, meeting_topic=topic)

    # -- UserImage --
    UserImage = apps.get_model('dashboard', 'user_image')
    user_images = [
        (4, 'user_images/app_icon.png', 10),
        (5, 'user_images/avialdo.jpeg', 12),
        (10, 'user_images/Me_bNfcXRq.jpg', 1),
        (32, 'user_images/download_Dmydryk.png', 21),
        (33, 'user_images/splash_background_tVC6Ym4.png', 20),
        (34, 'user_images/70-703425_png-1024-x-1024-logo.png', 15),
        (35, 'user_images/download_jO5fhkK.png', 24),
    ]
    for id_val, img, user_id in user_images:
        UserImage.objects.create(id=id_val, img=img, user_id=user_id)

    # -- VehicleMaker --
    VehicleMaker = apps.get_model('dashboard', 'vehiclemaker')
    makers = [
        (1, 'DAEWOO'),
        (2, 'FAW'),
        (3, 'NISSAN'),
        (4, 'ISUZU'),
    ]
    for VMid, VMNAME in makers:
        VehicleMaker.objects.create(VMid=VMid, VMNAME=VMNAME)

    # -- VehicleOwner --
    VehicleOwner = apps.get_model('dashboard', 'vehicleowner')
    owners = [
        (1, 'BANK OF PUNJAB'),
        (2, 'BILAL TRADERS'),
        (3, 'ORIX LEASING '),
        (4, 'BANK AL HABIB SWL'),
        (5, 'HAJI GUL ENT'),
        (6, 'STANDERD CHARTED'),
        (7, 'SITARA P/S'),
        (8, 'BANK AL HABIB'),
        (9, 'ALLIED BANK SWL'),
        (10, 'BURJ BANK'),
        (11, 'ALLIED BANK SWL'),
        (12, 'BANK AL HABIB KARACHI'),
        (13, 'HABIB BANK KARACHI'),
        (14, 'MEEZAN BANK'),
        (15, 'Salman'),
    ]
    for VO_id, VO_name in owners:
        VehicleOwner.objects.create(VO_id=VO_id, VO_name=VO_name)

    # -- Violations --
    Violations = apps.get_model('dashboard', 'violations')
    violations = [
        (1, 'Speed '),
        (2, 'Night Time Driving '),
        (3, 'Continuous driving '),
        (4, ' Maximum work hour in day '),
        (5, ' Sitting or driving without seatbelt.'),
        (6, 'Smoking in the vehicle'),
        (7, ' Drinking alcohol '),
        (8, ' Taking drugs or Cannabinoids etc.  '),
        (9, 'Did not fill the trip log'),
        (10, 'Did not fill the vehicle daily checklist '),
        (11, 'Working without PPE'),
        (12, 'Leaved the vehicle inattentive '),
        (13, 'Involve in Product theft'),
        (14, 'Bully with customer '),
        (15, 'Other'),
    ]
    for id_val, violation_type in violations:
        Violations.objects.create(id=id_val, violation_type=violation_type)

    # === Insert Dashboard Drivers and Vehicles (only 5 each) ===

    # -- Drivers --
    Driver = apps.get_model('dashboard', 'driver')
    drivers_data = [
        (1, 'DV-186', None, 'SHAMSHAD ALI', 'JAN AFZAL', '2120384290117', '2025-04-20',
         '03442020257', '1983-12-10', 'HTV', 'Simulator-YES', '2022-06-16',
         'SULTAN KHEL, KHYBER AGENCY', '100000203080', '2018-11-26', '2023-11-26',
         '2024-06-16', 'Primary', 1, '2022-11-20', 'Noor Clinical Lab', '2023-11-20',
         'A+VE', 'Fit', '2014-01-01', '2015-01-01', 7, '2022-04-04', '2022-05-11',
         22, '', 'Absent', 1, 1),
        (2, 'DV-540', None, 'NASRULLAH KHAN', 'SAIFAIL KHAN', '1120170580853', '2025-10-06',
         '03453523977', '1985-03-24', 'HTV', 'Simulator-YES', '2022-11-24',
         'AGHFAR KHEL, LAKKI MARWAT', '121000000651', '2018-03-21', '2023-03-20',
         '2024-11-24', 'Primary', 1, '2021-03-15', 'Noor Clinical Lab', '2022-03-15',
         'A-VE', 'Fit', '2019-03-01', '2020-02-29', 6, '2019-03-20', '2020-05-26',
         27, '', 'Absent', 2, 1),
        (3, 'DV-58', 'driver_images/DV-58.jpg', 'WAQAS KHAN', 'RAZA SHAH', '2120360390427', '2024-06-05',
         '03059169926', '1996-01-01', 'HTV', 'Simulator-YES', '2022-11-24',
         'SHINWARI, KHYBER AGENCY', '100000219969', '2019-02-14', '2024-02-13',
         '2024-11-24', 'Primary', 1, '2022-11-19', 'Noor Clinical Lab', '2023-11-19',
         'AB+VE', 'Fit', '2017-09-12', '2018-09-12', 1, '2021-12-06', '2022-01-08',
         20, '', 'Absent', 1, 1),
        (4, 'DV-91', 'driver_images/DV-91.jpg', 'FARHAD ULLAH', 'TILA MOHAMMAD', '2120362783091', '2025-11-12',
         '03034293029', '1989-01-01', 'HTV', 'Simulator-YES', '2022-11-24',
         'PERO KHEL, SHINWARI', '121000007886', '2013-09-07', '2027-01-13',
         '2024-11-24', 'Primary', 1, '2022-11-19', 'Noor Clinical Lab', '2023-11-19',
         'O+VE', 'Fit', '2017-12-19', '2018-12-19', 3, '2022-04-20', '2022-05-14',
         25, '', 'Absent', 2, 1),
        (5, 'DV-72', 'driver_images/DV-72.jpg', 'SAMI ULLAH', 'KHAIR KHAN', '2120373366259', '2030-02-17',
         '03009172949', '1985-01-01', 'HTV', 'Simulator-YES', '2022-11-28',
         'NIKI KHEL, KHYBER AGENCY', '100000209096', '2018-04-24', '2023-04-23',
         '2024-11-28', 'Primary', 1, '2022-12-02', 'Noor Clinical Lab', '2023-12-02',
         'A+VE', 'Fit', '2014-01-01', '2015-01-01', 6, '2022-01-01', '2022-01-30',
         22, '', 'Absent', 1, 1),
    ]
    for d in drivers_data:
        Driver.objects.create(
            D_ID=d[0],
            D_Number=d[1],
            D_Image=d[2],
            D_Name=d[3],
            Father_Name=d[4],
            CNIC=d[5],
            CNIC_Validity=d[6],
            Cell_Phone_Num=d[7],
            DOB=d[8],
            DL_Status=d[9],
            Motorway_Trained=d[10],
            DDC_Issue_Date=d[11],
            Address=d[12],
            License_No=d[13],
            HTV_License_Issue_Date=d[14],
            HTV_License_Expiry_Date=d[15],
            DDC_Expiry_Date=d[16],
            Education=d[17],
            Medical=d[18],
            Report_Date=d[19],
            Lab_Name=d[20],
            Expiry_Date=d[21],
            Blood_Group=d[22],
            Medical_Health=d[23],
            Joining_Date=d[24],
            Salary_Increment_Date=d[25],
            Experience=d[26],
            Leave_Date=d[27],
            Leave_Resume=d[28],
            Driving_Age=d[29],
            Previous_Company=d[30],
            Tank_Lorry=d[31],
            HTV_License_Authority_id=d[32],
            Oil_Marketing_Company_id=d[33],
        )

    # -- Vehicles --
    Vehicle = apps.get_model('dashboard', 'vehicle')
    vehicles_data = [
        (1, 'JP-7799', '2011', 'DE08TIS906541CA', 'M2TBEDP00018', 21000, '2023-06-30', '2023-09-02', '2024-03-03', '2023-12-31', 1, 1),
        (2, 'JP-9899', '2011', 'DE08TIS906539CA', 'M2TBEDP00016', 28000, '2023-06-30', '2023-09-02', '2024-03-03', '2023-12-31', 1, 1),
        (3, 'TLE-099', '2010', '01758864', 'AAD-13859', 50000, '2023-06-30', '2023-09-02', '2024-03-03', '2023-12-31', 2, 2),
        (4, 'TLE-399', '2010', '01758872', 'AAD-13858', 50000, '2023-06-30', '2023-09-02', '2024-03-03', '2023-12-31', 2, 2),
        (5, 'TLF-099', '2009', 'DE12TI-606495 CL', 'M2T6FDP-00085', 48000, '2023-06-30', '2023-09-02', '2024-03-03', '2023-12-31', 3, 1),
    ]
    for v in vehicles_data:
        Vehicle.objects.create(
            TL_Number=v[1],  # VH_number
            Capacity=v[5],  # VH_Capacity
            Chambers=v[2],  # VH_model (assuming it's being stored as Chambers)
            Engine_Number=v[3],  # VH_Engine_no
            Chassis_Number=v[4],  # VH_Chasis_No
            OMC_id=v[10],  # VH_Owner_name_id (assuming it's a Company FK)
            Make_id=v[11],  # VH_make_id (assuming it's a VehicleMaker FK)
            Model=v[2],  # VH_model (mapped to Model)
            LEASE_COMPANY_id=v[10],  # VH_Owner_name_id (VehicleOwner FK)
            LEASE_BANK_id=v[10],  # VH_Owner_name_id (VehicleOwner FK, assuming the same as above)
            Status="Active",  # Default value for Status (you can adjust accordingly)
            Type="Standard",  # Default Type (adjust as needed)
            Trailer_ID="N/A",  # Default Trailer_ID (adjust as needed)
            Brand="BrandName",  # Default Brand (adjust as needed)
            NHA_Configuration_Class="ClassA",  # Default NHA_Configuration_Class (adjust as needed)
            Gross_Empty_Trailer_Weight="N/A",  # Default value for weight
            DIP_CHART_Date=None,  # You can adjust this based on your data
            INSURANCE_Date=None,  # Adjust based on your data
            TAX_PAID_Date=None,  # Adjust based on your data
            FITNISSE_Date=None,  # Adjust based on your data
            Q_FOM_Date=None,  # Adjust based on your data
            Route_Permit_Date=None,  # Adjust based on your data
        )


def backwards(apps, schema_editor):
    # Delete dashboard data
    Driver = apps.get_model('dashboard', 'driver')
    Vehicle = apps.get_model('dashboard', 'vehicle')
    AnnualDrill = apps.get_model('dashboard', 'annual_drill')
    AnnualTraining = apps.get_model('dashboard', 'annual_training')
    Company = apps.get_model('dashboard', 'Company')
    Location = apps.get_model('dashboard', 'location')
    ToolBoxMeetingTopics = apps.get_model('dashboard', 'tool_box_meeting_topics')
    UserImage = apps.get_model('dashboard', 'user_image')
    VehicleMaker = apps.get_model('dashboard', 'vehiclemaker')
    VehicleOwner = apps.get_model('dashboard', 'vehicleowner')
    Violations = apps.get_model('dashboard', 'violations')

    Driver.objects.filter(D_ID__in=[1,2,3,4,5]).delete()
    Vehicle.objects.filter(VH_id__in=[1,2,3,4,5]).delete()
    AnnualDrill.objects.all().delete()
    AnnualTraining.objects.all().delete()
    Company.objects.all().delete()
    Location.objects.all().delete()
    ToolBoxMeetingTopics.objects.all().delete()
    UserImage.objects.all().delete()
    VehicleMaker.objects.all().delete()
    VehicleOwner.objects.all().delete()
    Violations.objects.all().delete()

    # Delete Django default tables data (from auth, admin, contenttypes, sessions)
    AuthPermission = apps.get_model('auth', 'Permission')
    AuthUser = apps.get_model('auth', 'User')
    AdminLog = apps.get_model('admin', 'LogEntry')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    AuthPermission.objects.all().delete()
    AuthUser.objects.all().delete()
    AdminLog.objects.all().delete()
    ContentType.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        # Replace '0001_initial' with your app’s actual last migration.
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
