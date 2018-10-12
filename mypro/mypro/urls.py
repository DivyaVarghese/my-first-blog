"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import blog.views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'^about',blog.views.about1,name='about_url'),
	url(r'^home',blog.views.home,name='home_url'),
	url(r'^gallery',blog.views.gallery,name='gallery_url'),
	url(r'^contact',blog.views.contact,name='contact_url'),
    url(r'^reg',blog.views.reg,name='reg_url'),
    url(r'^login',blog.views.login1,name='log_url'),
    url(r'^logout',blog.views.signout,name='logout_url'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns +=  url(r'^$',blog.views.home),
