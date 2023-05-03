from django.db import models
from django.utils import timezone

# Create your models here.


# class WebUser(models.Model):
#     firstName = models.CharField(max_length=100, null=True)
#     lastName = models.CharField(max_length=100, null=True)
#     phoneNumber = models.CharField(max_length=200, null=True)
#     homeAddress = models.CharField(max_length=200)
#     emailAddress = models.EmailField(max_length=254, null=True)
#     country = CountryField(blank_label='Select Country', null=True)
#     profilePicture = models.ImageField(null=True, blank=True)
#     profession = models.CharField(max_length=200, blank=True, null=True)
#     dateCreated = models.DateTimeField(auto_now_add=True, null=True)


#     def __str__(self):
#         return self.firstName + ' ' + self.lastName
    
