from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.




class MASSAGE (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    subject = models.CharField(null=True, max_length=200)
    massage = models.CharField(null=True, max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

