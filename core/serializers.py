from rest_framework import serializers

from .models import Post, Upvote


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "text")

    read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["request"].user
        post = Post.objects.create(author=user, **validated_data)
        return post


class EmptySerializer(serializers.Serializer):
    ...
