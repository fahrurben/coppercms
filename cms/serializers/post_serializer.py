from django.utils.text import slugify
from rest_framework import serializers
from cms.models import Post, Taxonomy

class PostSerializer(serializers.ModelSerializer):
    taxonomy = serializers.PrimaryKeyRelatedField(queryset=Taxonomy.objects.all(), many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'author', 'post_type', 'title', 'slug', 'excerpt', 'content', 'status', 'lang', 'taxonomy', 'main_post', 'parent_post', 'created_at', 'updated_at']
        extra_kwargs = {'slug': {'required': False}, 'author': {'required': False}}

    def save(self, *args, **kwargs):  # new
        if not 'slug' in self.validated_data:
            kwargs['slug'] = slugify(self.validated_data['title'])
        kwargs['author'] = self.context['request'].user
        return super().save(*args, **kwargs)