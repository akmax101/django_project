from django.db import models

# Create your models here.
class REGISTERED_USER_DETAIL(models.Model):
    registered_uesr_name=models.CharField(primary_key=False,max_length=50)
    registered_uesr_password=models.CharField(primary_key=True,max_length=50)
    registered_uesr_bio=models.CharField(max_length=200,default="You haven't entered any detail ")
    registered_uesr_email= models.EmailField(max_length=254,default="You_Haven't_entered_mail@pleaseDo.com" )
