from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'keywest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
