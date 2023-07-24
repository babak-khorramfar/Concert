from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    class Meta:
        verbose_name = "Profile"

    # A user profile model representing additional information for each user.
    # It has a one-to-one relationship with the built-in User model from django.contrib.auth.models.
    user = models.OneToOneField(User, verbose_name=("User Profile"), on_delete=models.CASCADE, related_name="profile")

    # Choices for Gender field.
    Man = 1
    Woman = 2
    status_choices = ((Man, "Man"), (Woman, "Woman"))

    # Gender field representing the gender of the user, which can be either 'Man' or 'Woman'.
    Gender = models.IntegerField(choices=status_choices, default=1)

    # ProfileImage field for storing the user's profile image. It uses the 'profileimages/' directory for image uploads.
    ProfileImage = models.ImageField(upload_to="profileimages/", null=True)

    # Credit field representing the credit amount associated with the user's profile.
    Credit = models.FloatField(verbose_name='Credit', default=0.00)
