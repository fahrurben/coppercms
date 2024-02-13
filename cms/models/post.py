from django.db import models

from cms.models import CustomUser, PostType, Taxonomy

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    post_type = models.ForeignKey(PostType, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    excerpt = models.TextField()
    content = models.TextField()

    DRAFT = 0
    PUBLISHED = 1
    POST_STATUS = {
        DRAFT: 'DRAFT',
        PUBLISHED: 'PUBLISHED',
    }

    status = models.IntegerField(choices=POST_STATUS, default=DRAFT)
    lang = models.CharField(max_length=2)
    taxonomy = models.ManyToManyField(Taxonomy, blank=True)
    main_post = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, related_name='translate_set')
    parent_post = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, related_name='child_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)