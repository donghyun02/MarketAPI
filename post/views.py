from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post, Comment
from post.serializers import PostSerializer, CommentSerializer


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        status = 200

        return Response(serializer.data, status=status)

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        price = request.data.get('price')

        post = Post.objects.create(author=request.user, title=title, content=content, price=price)
        serializer = PostSerializer(post)
        status = 201

        return Response(serializer.data, status=status)


class PostRetrieveView(APIView):

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        status = 200

        return Response(serializer.data, status=status)


class CommentsView(APIView):

    def post(self, request):
        post_id = request.data.get('post_id')
        content = request.data.get('content')
        nickname = request.user

        comment = Comment.objects.create(post_id=post_id, nickname=nickname, content=content)
        serializer = CommentSerializer(comment)
        status = 201

        return Response(serializer.data, status=status)