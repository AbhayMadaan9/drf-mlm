
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.user.urls'))
]
