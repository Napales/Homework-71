from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class CreateUpdateAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Post(CreateUpdateAbstractModel):
    image = models.ImageField(upload_to="posts", verbose_name='Картинка')
    content = models.TextField(max_length=2000, verbose_name="Контент")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts", verbose_name="Автор")
    like_users = models.ManyToManyField(get_user_model(), related_name='like_posts', verbose_name="Лайки")

    def __str__(self):
        return f"{self.pk} {self.author}"

    def get_absolute_url(self):
        return reverse("webapp:post_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
