from django.utils.text import slugify
from rest_framework import serializers

from cms.models import TaxonomyGroup

class TaxonomyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomyGroup
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']
        extra_kwargs = {'slug': {'required': False}}

    def save(self, *args, **kwargs):  # new
        if not 'slug' in self.validated_data:
            kwargs['slug'] = slugify(self.validated_data['name'])
        return super().save(*args, **kwargs)