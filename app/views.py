from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from app.models import Blog, Comment, Contact
from app.serializers import BlogModelSerializer, CommentModelSerializer, ContactModelSerializer


# Create your views here.


class BlogModelViewSet(ModelViewSet):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    parser_classes = [MultiPartParser]


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

    def perform_create(self, serializer):
        blog_id = self.kwargs.get('pk')
        blog = get_object_or_404(Blog, id=blog_id)
        serializer.save(user=self.request.user, blog=blog)


class CommentsGetByBlogId(ListAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        blog_id = self.kwargs.get('pk')
        return self.queryset.filter(blog_id=blog_id)


class ContactListCreateAPIView(ListCreateAPIView):
    serializer_class = ContactModelSerializer
    queryset = Contact.objects.all()
