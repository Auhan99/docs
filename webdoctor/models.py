from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import UserManager

class UserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserProfile(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=255,unique=False)
    email=models.EmailField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD='email'
    objects = UserManager()
    def get_short_name(self):
        return self.email






class categorie(models.Model):
    category=models.CharField(max_length=100,null=True)
    def __str__(self):
        return "%s " %(self.category )

class doctor(models.Model):
    category=models.ForeignKey(categorie,null=True, blank=True, related_name='cat',on_delete=models.CASCADE)
    doctorName=models.CharField(max_length=100,null=True)
    shortinfo = models.CharField(max_length=250, null=True)
    address=models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=250, null=True)
    professionalstatement = models.CharField(max_length=250, null=True)
    education = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=250, null=True)
    def __str__(self):
        return "%s %s" %(self.doctorName, self.category )

