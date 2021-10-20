from django.urls import path
from .import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App.urls')),
    path('',views.psave),
    path('index',views.padd, name='padd')

]