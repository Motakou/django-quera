from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(User):
    pass


class Enteghad(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    creator=models.models.ForeignKey(User)


 

 