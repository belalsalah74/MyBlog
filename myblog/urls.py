from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.welcome, name='home'),
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    path('',include('accounts.urls')),
]
