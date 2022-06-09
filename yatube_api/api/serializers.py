from rest_framework import serializers
from posts.models import Post, Comment, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date')
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),
                                              required=False
                                              )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
