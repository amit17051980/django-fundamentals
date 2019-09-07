from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH


class EmployeeQuerySet(models.QuerySet):

    def zero_manager(self):
        return self.filter(Q(lm_id='001') | Q(lm_id='002'))
    

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=50)
    lm_id = models.CharField(max_length=100, default='000')
    
    objects = EmployeeQuerySet.as_manager()

    
class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitation_sent", on_delete=models.PROTECT)
    to_user = models.ForeignKey(User, related_name="invitation_received", on_delete=models.PROTECT)
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    
