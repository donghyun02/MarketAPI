from rest_framework import serializers

from post.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'nickname', 'content', 'created_at', )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'price', 'author', 'comments', 'created_at', 'is_trade_finished', 'type', )