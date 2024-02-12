from django.utils.text import slugify
from rest_framework import serializers, validators
from rest_framework_recursive.fields import RecursiveField
from cms.models import Taxonomy, TaxonomyGroup
from cms.serializers import TaxonomyGroupSerializer


class TaxonomySerializer(serializers.ModelSerializer):
    group_id = serializers.PrimaryKeyRelatedField(source='group', queryset=TaxonomyGroup.objects.all())
    parent_id = serializers.PrimaryKeyRelatedField(source='parent', queryset=Taxonomy.objects.all(), required=False)
    main_id = serializers.PrimaryKeyRelatedField(source='main', queryset=Taxonomy.objects.all(), required=False)
    group = TaxonomyGroupSerializer(read_only=True)
    parent = RecursiveField(read_only=True, required=False)
    main = RecursiveField(read_only=True, required=False)

    class Meta:
        model = Taxonomy
        fields = ['id', 'name', 'description', 'group_id', 'group', 'parent_id', 'parent', 'lang', 'main_id', 'main', 'created_at', 'updated_at']
        extra_kwargs = {'slug': {'required': False}}
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'group_id'),
                message='Name already exists'
            )
        ]

        def save(self, *args, **kwargs):  # new
            if not 'slug' in self.validated_data:
                kwargs['slug'] = slugify(self.validated_data['name'])
            return super().save(*args, **kwargs)