from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.pagination import PageNumberPagination

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 25