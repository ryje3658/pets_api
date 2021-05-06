from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Pet(models.Model):
    """Model for Pet object. Owner attribute refers to the User object that created and owns the Pet."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField()
    weight = models.IntegerField()
    type = models.CharField(max_length=20)
    breed = models.CharField(max_length=40)
    disposition = models.CharField(max_length=100)
    availability = models.CharField(max_length=30)
    description = models.TextField()
    picture_primary = models.ImageField(blank=False)  # Primary picture is required
    picture_second = models.ImageField(blank=, null=True)  # Second picture not required
    picture_third = models.ImageField(blank=True, null=True)  # Third picture not required
    gender = models.CharField(max_length=1)
    owner = models.ForeignKey('auth.User', related_name='pets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Profile(models.Model):
    """
    Model for Profile object. One to one relationship with User and is created everytime a user object is created, with
    the is_shelter field being set to True or False depending on the kind of user being registered. (User or Shelter)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_shelter = models.BooleanField(default=False)
    shelter_name = models.CharField(max_length=50, null=True, blank=True)
    shelter_bio = models.TextField(default=None, null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
