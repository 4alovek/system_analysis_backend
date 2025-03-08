from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    full_name = models.CharField(_("Full name"), max_length=100)
    email = models.EmailField(_("Email address"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Interest(models.Model):
    name = models.CharField(_("Interest name"), max_length=50, unique=True)
    category = models.CharField(_("Category"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Interest")
        verbose_name_plural = _("Interests")
        unique_together = ['name', 'category']


class UserInterest(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='interests'
    )
    interest = models.ForeignKey(
        Interest, 
        on_delete=models.CASCADE,
        related_name='users'
    )
    preference_weight = models.FloatField(
        _("Preference weight"), 
        default=1.0
    )

    class Meta:
        verbose_name = _("User Interest")
        verbose_name_plural = _("User Interests")
        unique_together = ['user', 'interest']
