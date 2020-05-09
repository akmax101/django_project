from django.db import models

# Create your models here.
class contest_detail(models.Model):
    registered_user_website_name=models.CharField(max_length=20)
    registered_user_website_handler_link=models.URLField(max_length=200)
    registered_user_website_image=models.ImageField(upload_to='contest')
    registerd_user_website_best_rating=models.IntegerField()
    registered_user_password=models.CharField(max_length=20,default="please enter the password")
    registerd_user_website_userHandler=models.CharField(max_length=20,default="please enter user handle")
