from django.db import models

# Create your models here.
from django.db import models

class QRCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
