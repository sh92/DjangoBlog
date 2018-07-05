from django.conf.urls import url
from main import views

app_name = 'main'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^blog_form/',  views.blog_form, name='blog_form'),
    url(r'^blog_proc/',  views.blog_proc, name='blog_proc'),
]
