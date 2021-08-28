from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'test'

router = DefaultRouter()

urlpatterns = [
    path('test/',views.TestView.as_view())
]

urlpatterns += router.urls
