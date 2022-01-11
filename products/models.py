import uuid
from django.db import models
from base.BaseModel import BaseModel

class Products(BaseModel):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass
