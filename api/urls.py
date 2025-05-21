from django.urls import path
from .views import CompanyListView, company_form

urlpatterns = [
    path('company-form/', company_form, name='company_form'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
]

