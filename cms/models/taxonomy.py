from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from cms.models import TaxonomyGroup

class Taxonomy(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    group = models.ForeignKey(TaxonomyGroup, on_delete=models.RESTRICT)
    parent = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, related_name='child_set')
    lang = models.CharField(max_length=2)
    main = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, related_name='translate_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                'group',
                name='unique_name',
            ),
        ]

    def __str__(self):
        return self.name
