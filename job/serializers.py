from rest_framework import serializers
from .models import Job, Category, Apply


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


class ApplyJobSerializer(serializers.ModelSerializer):
    # cv = serializers.FileField()  # Ensure this is a FileField
    class Meta:
        model = Apply
        exclude = ['job']

    def create(self, validated_data):
        # Retrieve the job object from context
        job = self.context.get('job')
        if not job:
            raise serializers.ValidationError("Job context is missing.")

        # Set the job and create the ApplyJob instance
        validated_data['job'] = job
        return super().create(validated_data)
