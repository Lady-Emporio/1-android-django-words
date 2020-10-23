

from django.contrib import admin
from django.urls import path
from Sub1C import views
from Sub1C import WordViews
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('word/<int:pk>/', WordViews.WordView.as_view()),
    path('word/', WordViews.WordView_List.as_view()),
    path('u/<int:pk>/', WordViews.WordUpdate.as_view()),
    path('u/', views.update_Word, name="form_main"),
    
]   
