from leads.models import Leads
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer