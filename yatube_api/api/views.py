from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from posts.models import Post, Group, User, Follow
from api.serializers import PostSerializer, GroupSerializer, FollowSerializer
from api.serializers import CommentSerializer, UserSerializer
from api.permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.following.all()

    def perform_create(self, serializer):
        author = self.kwargs.get("following")
        following = get_object_or_404(User, username=author)
        serializer.save(following=following, user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
