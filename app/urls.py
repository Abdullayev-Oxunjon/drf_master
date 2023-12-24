from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import BlogModelViewSet, ContactListCreateAPIView, CommentCreateView, CommentsGetByBlogId

router = DefaultRouter()
router.register('blog', BlogModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact', ContactListCreateAPIView.as_view(), name='contact'),
    path('create-comment/<int:pk>/', CommentCreateView.as_view(), name='create-comment'),
    path('comments-list/<int:pk>/', CommentsGetByBlogId.as_view(), name='comments-list'),
]
