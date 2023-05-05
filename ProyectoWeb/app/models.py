from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Perfiles(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaul_profile.png')
    bio = models.TextField(blank=True, null=True, max_length=200)

    def __str__(self):
        return f'User: {self.user.username}, Bio: {self.bio}'

    def following(self):
        user_ids = Relationships.objects.filter(from_user=self.user)\
                                        .values_list('to_user', flat=True)
        return User.objects.filter(id__in=user_ids)

    def follower(self):
        user_ids = Relationships.objects.filter(to_user=self.user)\
                                        .values_list('to_user', flat=True)
        return User.objects.filter(id__in=user_ids)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.image}, {self.content}'

class Relationships(models.Model):
    from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user']),
        ]
