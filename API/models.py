from django.db import models
from .parser import get_announcements
from datetime import datetime


class Announcement(models.Model):
    site_id = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    started_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title

def register_all_announcements():
    announs = get_announcements()
    for announ in announs:
        Announcement(
            site_id= announ.get('id'),
            title=announ.get('title'),
            content=announ.get('content'),
            started_date=announ.get('started_date'),
            end_date=announ.get('end_date')
                    ).save()