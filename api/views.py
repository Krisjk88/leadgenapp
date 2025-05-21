from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
def company_form(request):
    return render(request, 'company_form.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer