from django.db.models import fields
from rest_framework import serializers
from .models import Test
# Create your serializers here.
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'text', 'author', 'date')