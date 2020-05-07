from django.db import models

# Create your models here.
class REGISTERED_USER_DETAIL(models.Model):
    registered_uesr_name=models.CharField(primary_key=True,max_length=50)
    registered_uesr_password=models.CharField(max_length=50)
        
