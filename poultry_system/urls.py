"""
URL configuration for poultry_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.dashboard_view, name="dashboard"),
    path('users/', views.users_view, name="users"),
    path('alerts/', views.alerts_view, name="alerts"),
    path('humidity/', views.humidity_view, name="humidity"),
    path('sensors/', views.sensors_view, name="sensor"),
    path('devices/', views.devices_view, name="devices"),
    path('logout/', views.logout_view, name="logout"),
    path('api/sensor-data/', views.upload_sensor_data, name='sensor-data'),
    path('turn-led1-on/', views.turn_led1_on, name='turn_led1_on'),
    path('turn-led2-on/', views.turn_led2_on, name='turn_led2_on'),
    path('turn-led1-off/', views.turn_led1_off, name='turn_led1_off'),
    path('turn-led2-off/', views.turn_led2_off, name='turn_led2_off'),
    path('turn-feeder-off/', views.turn_feeder_off, name='turn_feeder_off'),
    path('turn-feeder-on/', views.turn_feeder_on, name='turn_feeder_on'),
]
