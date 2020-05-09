from django.db import models

# Create your models here.
class project_details(models.Model):
    registered_user_password=models.CharField(max_length=20)
    registered_user_project_name=models.CharField(max_length=20)
    registered_user_project_details=models.TextField()
