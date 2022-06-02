from django.db import models
import uuid
# Create your models here.

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    fecha_carga = models.DateField(auto_now=True)

