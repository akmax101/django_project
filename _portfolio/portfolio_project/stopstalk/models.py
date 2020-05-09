from django.db import models

# Create your models here.
class stopstalk_detail (models.Model):
    registered_user_password=models.CharField(max_length=20)
    registered_user_website_image=models.ImageField(upload_to='contest')
    stopstalk_profile=models.URLField(max_length=200,default="http://please_enter_your_handler")
