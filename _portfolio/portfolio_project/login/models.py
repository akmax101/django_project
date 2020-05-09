from django.db import models

# Create your models here.
class REGISTERED_USER_DETAIL(models.Model):
    registered_uesr_name=models.CharField(primary_key=False,max_length=50)
    registered_uesr_password=models.CharField(primary_key=True,max_length=50)
    registered_uesr_bio=models.CharField(max_length=200,default="You haven't entered any detail ")
    registered_uesr_email= models.EmailField(max_length=254,default="You_Haven't_entered_mail@pleaseDo.com" )
    registered_uesr_linkedin=models.URLField(max_length=254,default="You_Haven't_entered_linkedin_id@pleaseDo.com")
    registered_uesr_accomplishment=models.TextField(default="No enteries made")
    registered_uesr_profile_photo=models.ImageField(upload_to="users/profile_photo",blank=True,null=True)
    registered_uesr_resume=models.FileField(upload_to="resume",blank=True,null=True)
