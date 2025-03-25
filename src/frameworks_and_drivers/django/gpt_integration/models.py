from django.db import models
from django.utils.translation import gettext_lazy as _
from posts.models import Post
from users.models import AppUser

class GPTRequest(models.Model):
    user = models.ForeignKey(
        AppUser, 
        on_delete=models.CASCADE,
        related_name='gpt_requests'
    )
    post = models.ForeignKey(
        Post, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='gpt_requests'
    )
    prompt = models.TextField(_("User prompt"))
    gpt_response = models.TextField(_("GPT response"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("GPT Request")
        verbose_name_plural = _("GPT Requests")
