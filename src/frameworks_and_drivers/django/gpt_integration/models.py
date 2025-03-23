from django.db import models
from frameworks_and_drivers.django.posts.models import Post
from frameworks_and_drivers.django.users.models import User


class GPTRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gpt_requests')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gpt_requests')
    got_response = models.BooleanField(default=False)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "frameworks_and_drivers.django.gpt_integration"