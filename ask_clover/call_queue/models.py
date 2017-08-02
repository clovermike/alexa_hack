from django.db import models


class Call(models.Model):
    personid = models.TextField(blank=False, null=False)
    reason = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
