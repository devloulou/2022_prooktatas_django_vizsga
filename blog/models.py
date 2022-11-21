from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# redirect vs reverse
# redirect átirányít egy megadott url-re
# reverse visszaadja a teljes url-t stringként

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title
