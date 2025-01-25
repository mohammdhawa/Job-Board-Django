from rest_framework import serializers
from .models import Job, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Job
        fields = ['id', 'title', 'city', 'job_type', 'published_at']


class JobDetailsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False, read_only=True)
    owner = serializers.StringRelatedField(many=False, read_only=True)
    city = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Job
        fields = '__all__'
