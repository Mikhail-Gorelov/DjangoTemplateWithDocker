import logging
from typing import Generic
from django.db import reset_queries
from django.db.models import query
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test
from . import services
from . import serializers

logger = logging.getLogger(__name__)

# Create your views here.
class TestView(GenericAPIView):
    serializer_class = serializers.TestSerializer
    queryset = Test.objects.all()
    def get(self, request):
        print(request)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
