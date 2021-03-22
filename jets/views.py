from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Jet
from .serializers import JetSerializer

# Create your views here.

class JetList(generics.ListAPIView):
    permission_classes = (Is.AuthenticatedOrReadOnly,)
    queryset - Jet.objects.all()
    serializer_class = JetSerializer
		
class JetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (Is.AuthenticatedOrReadOnly,)
    queryset = Jet.objects.all()
    serializer_class = JetSerializer