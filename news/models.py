from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"

    def get_absolute_url(self):
        return reverse("detail-news", kwargs={"id": self.id})
