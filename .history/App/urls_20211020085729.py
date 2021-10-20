from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App.urls'))
    path('index',views.h, name='home')
    path('',views.psave)
    path('index',views.padd, name='padd')

]