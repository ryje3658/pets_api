from django.db import models


class Pet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField()
    weight = models.IntegerField()
    type = models.CharField(max_length=20)
    breed = models.CharField(max_length=40)
    disposition = models.CharField(max_length=30)
    availability = models.CharField(max_length=30)
    description = models.TextField()
    picture_primary = models.ImageField(blank=False)  # Primary picture is required
    picture_second = models.ImageField(blank=True)  # Second picture not required
    picture_third = models.ImageField(blank=True)  # Third picture not required
    gender = models.CharField(max_length=1)
    owner = models.ForeignKey('auth.User', related_name='pets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
