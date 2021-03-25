from django.urls import path
from .views import JetListView, JetDetailView

urlpatterns = [
  path('', JetListView.as_view(), name='jet_list'),
  path('<int:pk>/', JetDetailView.as_view(), name='jet_detail'),
]