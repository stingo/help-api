from rest_framework import viewsets, mixins
from .models import HelpCategory, HelpArticle
from .serializers import HelpCategorySerializer, HelpArticleSerializer

class HelpCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HelpCategory.objects.all()
    serializer_class = HelpCategorySerializer

class HelpArticleViewSet(
    mixins.UpdateModelMixin,    # PUT, PATCH
    mixins.RetrieveModelMixin,  # GET /articles/:slug/
    mixins.ListModelMixin,      # GET /articles/
    mixins.DestroyModelMixin,   # 🔥 DELETE /articles/:slug/
    viewsets.GenericViewSet
):
    queryset = HelpArticle.objects.order_by('-date')  # remove `is_published=True` to allow edit/delete of drafts
    serializer_class = HelpArticleSerializer
    lookup_field = 'slug'