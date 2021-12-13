from .models import ApplicationForm
from .serializers import ApplicationFormSerializer, StatusChangeFormSerializer
from rest_framework import viewsets


class ApplicationFormDetailView(viewsets.ModelViewSet):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer


class ApplicationFormView(viewsets.ModelViewSet):
    queryset = ApplicationForm.objects.exclude(status='Accepted')
    serializer_class = ApplicationFormSerializer


class AcceptedFormView(viewsets.ModelViewSet):
    queryset = ApplicationForm.objects.filter(status='Accepted')
    serializer_class = ApplicationFormSerializer


class StatusChangeFormView(viewsets.ModelViewSet):
    queryset = ApplicationForm.objects.all()
    serializer_class = StatusChangeFormSerializer