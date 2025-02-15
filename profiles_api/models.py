import email
from pydoc import classname
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django work with our costum user model"""

    def create_user(self,email,name,password=None):
        """Creates a new user profile object"""
        if not email:
            raise ValueError('Users must have an email adress.')

        email=self.normalize_email(email)    

        user=self.model(email=email,name=name)

        user.set_password(password)

        user.save(using=self._db)

        return user
    def create_superuser(self,email,name,password):
        """Creates and saves a new superuser with given details"""

        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True

        user.save(using=self._db)

        return user    






class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Repesent a user profile in our system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    #second_name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Used to get a users fullname"""
        return self.name

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):
        """django uses this when needs to object convert to string"""
        return self.email    

#################################################################################

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Returns the model as a string"""
        return self.status_text

#####################################################Exception#################################################
class demofeedprofile(models.Model):
    user_pro=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    state=models.CharField(max_length=255)
    create_on=models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.state




















