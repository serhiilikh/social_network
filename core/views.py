from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Post, Upvote
from .serializers import PostSerializer, EmptySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author_id=self.request.user.id)

    @action(
        detail=True,
        methods=[
            "POST",
        ],
        serializer_class=EmptySerializer,
    )
    def upvote(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        Upvote.objects.get_or_create(post=post, user=request.user)
        return Response(status=200)

    @action(
        detail=True,
        methods=[
            "POST",
        ],
        serializer_class=EmptySerializer,
    )
    def remove_vote(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        Upvote.objects.filter(post=post, user=request.user).delete()
        return Response(status=204)
