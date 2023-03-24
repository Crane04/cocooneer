from django.db import models

# Create your models here.

class Features(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField(max_length=999999)
    font_awesome_icon = models.CharField(max_length = 1000, default="")
    icon_color = models.CharField(
        choices=[
            ("1","1"),
            ("2","2"),
            ("3","3"),
        ], default="", max_length=10000
    )