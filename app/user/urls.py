from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    url('create/', views.CreateUserView.as_view(), name='create'),

]