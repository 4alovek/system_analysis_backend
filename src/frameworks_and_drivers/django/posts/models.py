from django.db import models
from users.models import User


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    generated_by_gpt = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.DRAFT)


class PostReaction(models.Model):
    class ReactionTypes(models.TextChoices):
        LIKE = 'like', 'Like'
        DISLIKE = 'dislike', 'Dislike'

    reaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    created_at = models.DateTimeField(auto_now_add=True)
    reaction_type = models.CharField(max_length=7, choices=ReactionTypes.choices)

    class Meta:
        unique_together = ('user', 'post')  # 1 реакция на пост от пользователя
