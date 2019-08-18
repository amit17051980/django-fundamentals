from django.db import models
from django.db.models import Q


class EmployeeQuerySet(models.QuerySet):

    def zero_manager(self):
        return self.filter(Q(emp_id='002') | Q(lm_id='001'))
    

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=50)
    lm_id = models.CharField(max_length=100, default='000')
    
    objects = EmployeeQuerySet.as_manager()

    
