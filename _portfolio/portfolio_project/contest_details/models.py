from django.db import models

# Create your models here.
class contest_details(models.Model):
    registered_uesr_password=models.CharField(max_length=20,primary_key=True)
    registered_uesr_webstie=models.CharField(max_length=20)
    registered_uesr_image=models.ImageField(upload_to="contest")
