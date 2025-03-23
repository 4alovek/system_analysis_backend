from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)  # Совместимо с Django-авторизацией
    full_name = models.CharField(max_length=255)

    class Meta:
        app_label = "frameworks_and_drivers.django.users"


class UserInterest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    interest_name = models.CharField(max_length=100)
    preference_weight = models.FloatField(default=1.0)
    preference_difficulty = models.IntegerField(default=1)
    
    class Meta:
        app_label = "frameworks_and_drivers.django.users"
