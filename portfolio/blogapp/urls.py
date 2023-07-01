from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('',views.blog,name='blog'),
    path('<int:num>',views.detail,name='detail')
]