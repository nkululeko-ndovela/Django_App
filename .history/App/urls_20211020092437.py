from django.urls import path
from .import views,include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App.urls')),
    path('',views.show),
    path('index',views.add, name='add')
    path('edit',views.add, name='add')


]