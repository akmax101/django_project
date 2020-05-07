from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('logging_in',views.logging_in,name='logging_in')
]
