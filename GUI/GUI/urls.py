"""GUI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from views import index,landset7,landset8,ndvi_7,ndwi_7,ndbi_7,ndvi_8,ndwi_8,ndbi_8
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^landset7/$', views.landset7),
    url(r'^landset8/$', views.landset8),
    url(r'^ndvi_7/$', views.ndvi_7),
    url(r'^ndwi_7/$', views.ndwi_7),
    url(r'^ndbi_7/$', views.ndbi_7),
    url(r'^ndvi_8/$', views.ndvi_8),
    url(r'^ndwi_8/$', views.ndwi_8),
    url(r'^ndbi_8/$', views.ndbi_8),
]
urlpatterns += staticfiles_urlpatterns()
