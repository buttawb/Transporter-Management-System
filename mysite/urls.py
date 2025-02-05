from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dashboard import views
import dashboard.helpers

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Authentication & Dashboard
    path('loginuser', views.login_user, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),

    # User CRUD
    path('allusers', views.allusers, name='allusers'),
    path('adduser', views.adduser, name='adduser'),
    path('check_username/', views.check_username, name='check_username'),
    path('edituser/<int:id>/', views.edituser, name='edituser'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),

    # Company CRUD
    path('company', views.get_company, name='get_company'),
    path('addcompany/', views.add_company, name='add_company'),
    path('editcompany/<int:company_id>/', views.edit_company, name='edit_company'),
    path('deletecompany/<int:company_id>/', views.delete_company, name='delete_company'),

    # Vehicle CRUD
    path('vehicles/<str:filter>/', views.get_vehicle, name='get_vehicles'),
    path('addvehicle', views.add_vehicle, name='add_vehicle'),
    path('editvehicle/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicleview/<int:vehicle_id>/', views.vehicle_view, name='vehicleview'),
    # If you have custom routes for TPPL/GO/PSO/APL filtering,
    # you can re-use get_vehicle with different paths:
    path('get_tppl/<str:filter>/', views.get_vehicle, name='get_tppl'),
    path('get_go/<str:filter>/', views.get_vehicle, name='get_go'),
    path('get_pso/<str:filter>/', views.get_vehicle, name='get_pso'),
    path('get_apl/<str:filter>/', views.get_vehicle, name='get_apl'),
    # Example delete (if you implement it in views):
    # path('deletevehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),

    # Vehicle Owner CRUD
    path('owners', views.get_vehicle_owner, name='get_owners'),
    path('addowner', views.add_owner, name='add_owner'),
    path('editowner/<int:owner_id>/', views.edit_owner, name='edit_owner'),
    path('deleteowner/<int:owner_id>/', views.delete_owner, name='delete_owner'),

    # Vehicle Maker CRUD
    path('makers', views.get_vehicle_maker, name='get_makers'),
    path('addmaker', views.add_maker, name='add_maker'),
    path('editmaker/<int:maker_id>/', views.edit_maker, name='edit_maker'),
    path('deletemaker/<int:maker_id>/', views.delete_maker, name='delete_maker'),

    # Driver CRUD
    path('drivers', views.get_driver, name='get_drivers'),
    path('driverview/<int:driver_id>/', views.driver_view, name='driverview'),
    path('adddriver', views.add_driver, name='add_driver'),
    path('editdriver/<int:driver_id>/', views.edit_driver, name='editdriver'),
    # Example delete (if you implement it):
    # path('deletedriver/<int:driver_id>/', views.delete_driver, name='delete_driver'),

    # Violations
    # path('violations', views.get_violation, name='get_violations'),
    # path('addviolation', views.add_violation, name='add_violation'),
    path('adddriverviolation/<int:D_ID>/', views.add_driver_violation, name='add_driver_violation'),

    # Tool Box Meetings, Training & Drills
    path('addtbm/<int:driver_id>/', views.add_tbm, name='add_tbm'),
    path('addtraining/<int:driver_id>/', views.add_driver_training, name='add_driver_training'),

    # Utility / CSV / Import / Bulk Update
    path('import_drivers/', dashboard.helpers.import_drivers_from_images, name='import_drivers'),
    path('count_uploaded_images/', dashboard.helpers.count_uploaded_images, name='count_uploaded_images'),
    path('remove_null_images/', dashboard.helpers.remove_null_images, name='remove_null_images'),
    path('match_driver_ids/', dashboard.helpers.match_driver_ids, name='match_driver_ids'),
    path('update_models_from_csv/', dashboard.helpers.update_models_from_csv, name='update_models_from_csv'),
    path('update_driver_ages/', views.update_driver_ages, name='update_driver_ages'),

    # Static Content
    path('procedures', views.get_procedures, name='get_procedures'),
    path('policies', views.get_policies, name='get_policies'),
    path('emergencyprocedures', views.get_emergency_procedures, name='get_emergency_procedures'),
]

# Serving media & static in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
