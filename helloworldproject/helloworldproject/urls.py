
from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloworldView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloworldapp.urls')),
   
]
