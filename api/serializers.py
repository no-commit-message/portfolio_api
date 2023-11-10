from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "skill_level", "created_at", "updated_at")