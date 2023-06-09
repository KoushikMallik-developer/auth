from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from api.managers.userManager import UserManager


# Custom User Model
class User(AbstractBaseUser):
    id = models.CharField(max_length=150, unique=True, primary_key=True, null=False)
    username = models.CharField(max_length=15)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        null=False
    )
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, null=False)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to='images/users/', default="images/users/defaultUserImage.png", null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._generate_username()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always

        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""

        return self.is_admin

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # All admins are staff
        return self.is_admin

    @property
    def get_phone(self):
        """Fetch registered Phone Number of the user"""
        if self.fname:
            return self.phone
        else:
            return None

    @property
    def get_name(self):
        """Fethch registered Phone Number of the user"""
        if self.fname and self.lname:
            return str(self.fname) + " " + str(self.lname)
        else:
            return None

    @property
    def get_is_active(self):
        return self.is_active
