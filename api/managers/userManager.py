from django.contrib.auth.base_user import BaseUserManager

from api.views.helpers.user_model_helper import generate_id


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, fname, lname, dob=None, phone=None, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth, first name, last name, phone number, image and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            id=generate_id(fname),
            email=self.normalize_email(email),
            dob=dob,
            fname=fname,
            lname=lname,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fname, lname, dob=None, phone=None, password=None, password2=None):
        """
        Creates and saves a superuser with the given email, date of
        birth, first name, last name, phone number, image and password.
        """
        user = self.create_user(
            email,
            password=password,
            dob=dob,
            fname=fname,
            lname=lname,
            phone=phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
