import uuid
from django.db import models
from .SoftDeletionManager import SoftDeletionModel


class BaseModel(SoftDeletionModel):  # base class should subclass 'django.db.models.Model'

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    deleted_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Set this model as Abstract
