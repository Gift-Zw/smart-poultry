from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, cell, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            cell=cell

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, cell, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            cell=cell
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    cell = models.CharField(max_length=20, default='+263776149765')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cell']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class SensorData(models.Model):
    water_level = models.DecimalField(max_digits=25, decimal_places=1)
    temperature = models.DecimalField(max_digits=25, decimal_places=10)
    humidity = models.IntegerField()
    led_light1_status = models.BooleanField()
    led_light2_status = models.BooleanField()
    servo_motor_status = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)


class Alert(models.Model):
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    email = models.BooleanField(default=True)
    sensor = models.CharField(max_length=25)


class Sensor(models.Model):
    name = models.CharField(max_length=25)
    measurement = models.CharField(max_length=25)
    current_reading = models.DecimalField(decimal_places=1, max_digits=25)
    status = models.CharField(max_length=25, default='Active')
    date_added = models.DateTimeField(auto_now_add=True)


class Actuator(models.Model):
    name = models.CharField(max_length=25)
    component = models.CharField(max_length=25)
    status = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

