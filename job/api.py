from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import JobSerializer, JobDetailsSerializer, ApplyJobSerializer
from .models import Job
from .job_custom_pagination import CustomPagination
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = CustomPagination


class JobDetailAPI(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]  # Accept both JSON and form-data

    def get(self, request, pk):
        try:
            job = Job.objects.get(id=pk)
            serializer = JobDetailsSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk):
        try:
            job = Job.objects.get(id=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ApplyJobSerializer(data=request.data, context={'job': job})
        if serializer.is_valid():
            serializer.save()
            job_serializer = JobDetailsSerializer(job)  # Serialize the job for the response
            return Response(job_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



