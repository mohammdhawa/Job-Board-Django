from rest_framework import generics
from .serializers import JobSerializer, JobDetailsSerializer
from .models import Job
from .job_custom_pagination import CustomPagination


class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = CustomPagination


class JobDetailAPI(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailsSerializer
