from django.conf.urls import url
from app_one import views


app_name = 'app_one'


urlpatterns = [
    url(r'^rel$', views.view_two, name='alert'),
]


