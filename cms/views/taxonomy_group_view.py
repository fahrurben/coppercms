from cms.models import TaxonomyGroup
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from cms.serializers import TaxonomyGroupSerializer

class TaxonomyGroupView(ModelViewSet):
    queryset = TaxonomyGroup.objects.all()
    serializer_class = TaxonomyGroupSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']