from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

GENDER = (
    (True, "Kişi"),
    (False, "Qadın")
)

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField(choices=GENDER, default=True)

    def __str__(self):
        return "{}".format(self.user.get_full_name())


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=225)
    name = models.CharField(max_length=2, null=True)
    status = models.BooleanField(default=True)
    description = models.TextField()
    order = models.IntegerField(default=0)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ("order",)
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"

    def get_absolute_url(self):
        return reverse("detail-news", kwargs={"name": self.id})  # '/news-detail/6/'
