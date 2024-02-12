from cms.models import Taxonomy
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from cms.serializers import TaxonomySerializer

class TaxonomyView(ModelViewSet):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']