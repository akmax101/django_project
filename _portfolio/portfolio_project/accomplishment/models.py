from django.db import models

# Create your models here.
class accomplishment_detail(models.Model):
    registered_user_password=models.CharField(max_length=20)
    registered_user_accomplishment_details=models.TextField()
    registered_user_languages_known=models.TextField(blank=True,null=True)
