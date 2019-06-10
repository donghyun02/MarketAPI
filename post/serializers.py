from rest_framework import serializers

from accounts.serializers import UserSerializer
from post.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'nickname', 'content', 'created_at', )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'price', 'author', 'comments', 'created_at', )