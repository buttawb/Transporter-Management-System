"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginuser', views.login_user, name='login'),
    path('', views.dashboard),
    path('allusers', views.allusers),
    path('adduser', views.adduser),
    path('check_username/', views.check_username, name='check_username'),
    path('edituser/<int:id>', views.edituser, name='edituser'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),
    path('logout/', views.logout_user, name='logout'),
    # path('print_user_data_pdf/<int:user_id>/', views.print_user_data_pdf, name='print_user_data_pdf'),



    # # Company crud URLs
    path('company', views.get_company, name='get_company'),
    path('addcompany/', views.add_company, name='add_company'),
    path('editcompany/<int:company_id>/', views.edit_company, name='edit_company'),
    path('deletecompany/<int:company_id>/', views.delete_company, name='delete_company'),

    # # Vehicle crud URLs
    path('vehicles/<str:filter>/', views.get_vehicle, name='get_vehicles'),
    path('addvehicle', views.add_vehicle, name='add_vehicle'),
    path('editvehicle/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicleview/<int:vehicle_id>/', views.vehicle_view, name='vehicleview'),
    path('get_tppl/<str:filter>/', views.get_vehicle, name='get_tppl'),
    path('get_go/<str:filter>/', views.get_vehicle, name='get_go'),
    path('get_pso/<str:filter>/', views.get_vehicle, name='get_pso'),
    path('get_apl/<str:filter>/', views.get_vehicle, name='get_apl'),

    # path('deletevehicle/<int:vehicle_id>/',
    #      delete_vehicle, name='delete_vehicle'),

    # # Vehicle Owner crud URLs
    path('owners', views.get_vehicle_owner, name='get_owners'),
    path('addowner', views.add_owner, name='add_owner'),
    path('editowner/<int:owner_id>/', views.edit_owner, name='edit_owner'),
    path('deleteowner/<int:owner_id>/',
         views.delete_owner, name='delete_owner'),

    # # Vehicle Maker crud URLs
    path('makers', views.get_vehicle_maker, name='get_makers'),
    path('addmaker', views.add_maker, name='add_maker'),
    path('editmaker/<int:maker_id>/', views.edit_maker, name='edit_maker'),
    path('deletemaker/<int:maker_id>/', views.delete_maker, name='delete_maker'),

    # # Driver
    path('drivers', views.get_driver, name='get_drivers'),
    path('driverview/<int:driver_id>/', views.driver_view, name='driverview'),
    path('adddriver', views.add_driver, name='add_driver'),
    path('editdriver/<int:driver_id>/', views.edit_driver, name='editdriver'),
    # path('deletedriver/<int:driver_id>/', delete_driver, name='delete_driver'),


    path('violations', views.get_violation, name='get_violations'),
    path('addviolation', views.add_violation, name='add_violation'),
    path('adddriverviolation/<int:D_ID>/', views.add_driver_violation, name='add_driver_violation'),
    # path('import_drivers/', views.import_drivers_from_images, name='import_drivers'),
    # path('count_uploaded_images/', views.count_uploaded_images, name='count_uploaded_images'),
    # path('remove_null_images/', views.remove_null_images, name='remove_null_images'),
    # path('match_driver_ids/', views.match_driver_ids, name='match_driver_ids'),
    # path('update_models_from_csv/', views.update_models_from_csv, name='update_models_from_csv'),

    path('addtbm/<int:D_ID>/', views.add_tbm, name='add_tbm'),
    path('addtraining/<int:D_ID>/', views.add_driver_training, name="add_driver_training"),
    # path('update_driver_ages/', views.update_driver_ages, name='update_driver_ages'),

    path('procedures', views.get_procedures),
    path('policies', views.get_policies),
    path('emergencyprocedures', views.get_emergency_procedures),
    path('hsepage', views.get_hse_page),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



  
