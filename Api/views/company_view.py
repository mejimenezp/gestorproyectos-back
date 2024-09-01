from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from Api.serializers import CompanySerializer
from Api.models import Company
from memory_profiler import profile

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @profile
    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        company = self.get_object()
        projects = company.projects.all()
        return Response({'projects': [project.name for project in projects]})

    @profile
    def perform_create(self, serializer):
        serializer.save()

    @profile
    def perform_update(self, serializer):
        serializer.save()

    @profile
    def perform_destroy(self, instance):
        instance.delete()
