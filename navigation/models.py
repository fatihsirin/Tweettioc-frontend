from django.utils import timezone
from django.contrib.auth.models import User
from djongo import models

# Create your models here.

TYPE_CHOICES = [
    ('user', 'New User'),
    ('falsepositive', 'False Positive Data'),
    ('module', 'New Module'),
    ('other', 'Other'),
]


class Contribute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    message_type = models.CharField(choices=TYPE_CHOICES, max_length=100)
    date = models.DateField(auto_now_add=True)

    objects = models.DjongoManager()

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        db_table = "contributions"
