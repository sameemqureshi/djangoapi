import datetime
from django.db import models

# Create Company model.-
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField()
    address=models.TextField()
    Domain=models.CharField(max_length=100,choices=(('IT','IT'),
                                                    ('Production','Production'),
                                                    ('Marketing','Marketing')))
    is_active=models.BooleanField()
    def  __str__(self):
        return self.name +"  "+self.address


class Machine(models.Model):
    machine_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    installation_date = models.DateField(default=datetime.date.today)
    description = models.TextField(blank=True, null=True)
    power_consumption_per_hour = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


