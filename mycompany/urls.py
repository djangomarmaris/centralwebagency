from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'cwa'


urlpatterns =[
    path('',views.index,name ='index'),
    path('about/',views.about,name='about'),
    path('blog/list/',views.bloglist,name='blog-list'),
    path('contact/',views.contact,name='contact'),
    path('<str:slug>/',views.blog_detail,name='blog_detail'),
]


