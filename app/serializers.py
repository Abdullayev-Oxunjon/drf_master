from rest_framework import serializers

from app.models import Blog, Comment, Contact


class BlogModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'


class CommentModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    blog = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
