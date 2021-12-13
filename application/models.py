from django.db import models

# Create your models here.

class ApplicationForm(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    logo = models.ImageField(upload_to='uploads/application', null=True, blank=True)
    team_background = models.CharField(max_length=500, null=False, blank=False)
    company_products = models.CharField(max_length=500, null=False, blank=False)
    incubation_type = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=False, blank=False, default='Applied')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name