from cms.models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from cms.serializers import PostSerializer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'excerpt', 'content']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def get_queryset(self):

        queryset = Post.objects.all()
        author_id = self.request.query_params.get('author_id')
        post_type_name = self.request.query_params.get('post_type_name')
        status = self.request.query_params.get('status')
        lang = self.request.query_params.get('lang')
        taxonomy_ids = self.request.query_params.getlist('taxonomy_ids')
        main_post_id = self.request.query_params.get('main_post_id')

        if author_id is not None:
            queryset = queryset.filter(author=author_id)

        if post_type_name is not None:
            queryset = queryset.filter(post_type__name=post_type_name)

        if status is not None:
            queryset = queryset.filter(status=status)

        if lang is not None:
            queryset = queryset.filter(lang=lang)
        # Todo: Post view queryset, add default lang filter

        if taxonomy_ids is not None and len(taxonomy_ids) > 0:
            queryset = queryset.filter(taxonomy__in=taxonomy_ids)

        if main_post_id is not None:
            queryset = queryset.filter(main_post=main_post_id)

        return queryset