from datetime import timedelta
from django.utils import timezone
import requests
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.decorators import api_view

from core.admin import UserCreationForm
from core.models import User, Sensor, SensorData, Actuator, Alert
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SensorDataSerializer
from .emails import send_high_temperature_alert_email, send_low_temperature_alert_email

ESP32 = 'http://192.168.181.119'


# Create your views here.
@login_required
def dashboard_view(request):
    user = request.user
    context = {
        'user': user,
        'user_total': User.objects.all().count(),
        'data': SensorData.objects.latest('date')
    }
    return render(request, 'index.html', context)


@login_required
def users_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.data['email'],
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                password=form.data['password1'],
                cell=form.data['cell']
            )
            user.save()
            return redirect('users')
        else:
            messages.error(request, form.errors)
    else:
        form = UserCreationForm()
    context = {
        'users': User.objects.all(),
        'form': UserCreationForm()
    }
    return render(request, 'users.html', context)


@login_required
def alerts_view(request):
    context = {
        'alerts': Alert.objects.order_by('date')
    }
    return render(request, 'alerts.html', context)


@login_required
def sensors_view(request):
    context = {
        'sensors': Sensor.objects.order_by('date_added')
    }
    return render(request, 'sensors.html', context)


@login_required
def devices_view(request):
    context = {
        'actuators': Actuator.objects.all()
    }
    return render(request, 'devices.html', context)


@login_required
def humidity_view(request):
    context = {
        'sensor_data': SensorData.objects.order_by('-date')
    }
    return render(request, 'humidity.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard')


@api_view(['POST'])
def upload_sensor_data(request):
    if request.method == 'POST':
        data = request.data
        serializer = SensorDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            channel_layer = get_channel_layer()
            data = serializer.data
            now = timezone.now()
            ten_minutes_ago = now - timedelta(minutes=3)

            recent_alert = Alert.objects.filter(date__gte=ten_minutes_ago).first()

            if float(data['temperature']) > 24:
                response = requests.get(ESP32 + '/led1/off')
                response = requests.get(ESP32 + '/led2/off')
                if not recent_alert:
                    send_high_temperature_alert_email(data['temperature'])

            if float(data['temperature']) < 20:
                response = requests.get(ESP32 + '/led1/on')
                response = requests.get(ESP32 + '/led2/on')
                if not recent_alert:
                    send_low_temperature_alert_email(send_low_temperature_alert_email(data['temperature']))

            async_to_sync(channel_layer.group_send)(
                "sensor_data",
                {
                    "type": "send_data",
                    "data": data
                }
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def turn_led1_on(request):
    print('i have been called')
    try:
        response = requests.get(ESP32 + '/led1/on')
        response.raise_for_status()  # Raise exception for non-2xx responses
        return JsonResponse({'message': 'GET request sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def turn_led2_on(request):
    try:
        response = requests.get(ESP32 + '/led2/on')
        response.raise_for_status()  # Raise exception for non-2xx responses
        return JsonResponse({'message': 'GET request sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def turn_led1_off(request):
    try:
        response = requests.get(ESP32 + '/led1/off')
        response.raise_for_status()  # Raise exception for non-2xx responses
        return JsonResponse({'message': 'GET request sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def turn_led2_off(request):
    try:
        response = requests.get(ESP32 + '/led2/off')
        response.raise_for_status()  # Raise exception for non-2xx responses
        return JsonResponse({'message': 'GET request sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def turn_feeder_off(request):
    try:
        response = requests.get(ESP32 + '/servo/off')
        response.raise_for_status()  # Raise exception for non-2xx responses
        return JsonResponse({'message': 'GET request sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def turn_feeder_on(request):
    try:
        response = requests.get(ESP32 + '/servo/on')
        response.raise_for_status()  # Raise exception for non-2xx responses
        return JsonResponse({'message': 'GET request sent successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
