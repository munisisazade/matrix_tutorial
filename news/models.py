from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from news.options.tool import GENDER, get_avatar_path

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField(choices=GENDER, default=True)
    image = models.ImageField(upload_to=get_avatar_path, null=True)

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width:200px' src='{}' alt=''>".format(self.image.url))
        else:
            return mark_safe("<img src='{}' alt=''>".format("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"))


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
