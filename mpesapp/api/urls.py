from django.contrib import admin
from django.urls import path, include

from mpesapp.api.views import LNMCallbackUrlAPIView

urlpatterns = [
    path('lnm/', LNMCallbackUrlAPIView.as_view(), name='lnm-callback'),
]