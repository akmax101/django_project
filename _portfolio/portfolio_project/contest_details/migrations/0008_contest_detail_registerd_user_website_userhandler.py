# Generated by Django 2.2.12 on 2020-05-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest_details', '0007_contest_detail_registered_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest_detail',
            name='registerd_user_website_userHandler',
            field=models.CharField(default='please enter user handle', max_length=20),
        ),
    ]
