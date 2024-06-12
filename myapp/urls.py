from django.urls import path
from .views import PersonListCreateView,PersonDetailView

urlpatterns = [
    path('api/persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/persons/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]