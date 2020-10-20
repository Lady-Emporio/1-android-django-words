

from django.contrib import admin
from django.urls import path
from Sub1C import views
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('u/', views.update_Word, name="form_main"),
]   
