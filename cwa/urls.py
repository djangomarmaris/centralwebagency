"""cwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns

from mycompany import views
from mycompany.views import *
from mycompany.sitemaps import CategorySitemap , BlogSitemap , StaticSitemap
sitemaps ={
    'categorySitemap':CategorySitemap,
    'blogSitemao': BlogSitemap,
    'staticSitemap':StaticSitemap,
}

urlpatterns = [

    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('robot.txt',include('robots.urls')),
    path('',index,name='index'),
    path('cwa/',include('mycompany.urls')),
    path('reference/',views.referance,name='partner'),
    path('<str:slug>/',product_detail,name='detail'),



    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)