from django.db import models
from posts.models import Post
from users.models import User
from django.utils.translation import gettext_lazy as _


class GPTRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gpt_requests')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gpt_requests')
    got_response = models.BooleanField(default=False)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
