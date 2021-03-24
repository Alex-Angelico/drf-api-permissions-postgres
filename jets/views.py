from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from jets.permissions import IsOwnerOrReadOnly
from .models import Jet
from .serializers import JetSerializer

# Create your views here.

class JetListView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Jet.objects.all()
    serializer_class = JetSerializer
		
class JetDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Jet.objects.all()
    serializer_class = JetSerializer