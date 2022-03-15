from django.urls import path, include
from shortner.views import *

urlpatterns = [
    path('', createUrl),
    path('<slug:key>/', routeUrl)
]
