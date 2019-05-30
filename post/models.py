from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    BUY = 'B'
    SELL = 'S'
    TYPE_CHOICES = (
        (BUY, 'Buy'),
        (SELL, 'Sell')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=BUY)
    title = models.CharField(max_length=124)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_trade_finished = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return '{} - {}'.format(self.author.username, self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    nickname = models.CharField(max_length=16)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)