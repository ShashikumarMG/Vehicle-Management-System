from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = "vms"


urlpatterns = [
    path('', views.VehicleDataList.as_view(), name='vihicle'),
    path('vehicle_update/<pk>', views.UserUpdate.as_view(),name='vehicle_update'),
    path('delete/<pk>', views.DeleteUser.as_view(),name='delete'),
]