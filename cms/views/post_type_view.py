from cms.models import PostType
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from ..serializers import PostTypeSerializer

class PostTypeView(ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']