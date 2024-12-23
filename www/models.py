from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class ModelFavorite(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    game = models.ForeignKey('ModelGame', verbose_name="Игра", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.game}'

    class Meta:
        verbose_name = "Фаворит"
        verbose_name_plural = "Фавориты"
        unique_together = ('user', 'game')


class ModelGame(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", )
    company = models.ForeignKey('ModelCompany', verbose_name="Разработчик", on_delete=models.CASCADE)
    date_published = models.DateField(verbose_name="Дата выхода", )
    slug = models.SlugField(blank=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ModelGame, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class ModelRating(models.Model):
    game = models.ForeignKey(ModelGame, verbose_name="Игра", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name="Оценка", )

    def __str__(self):
        return f'{self.game} {self.value}'

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class ModelCompany(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    country = models.CharField(verbose_name="Страна", max_length=100)
    description = models.TextField(verbose_name="Описание", )
    date_created = models.DateField(verbose_name="Дата основания", )
    slug = models.SlugField(blank=True, default='', editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ModelCompany, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"


class ModelComment(models.Model):
    game = models.ForeignKey(ModelGame, verbose_name="Игра", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Комментарий", )
    date_of_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.game} {self.user} {self.comment}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class ModelImageGame(models.Model):
    image = models.ImageField(verbose_name="Изображение", upload_to='images/')
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    game = models.ForeignKey(ModelGame, verbose_name="Игра", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image}'

    class Meta:
        verbose_name = "Изображения для игры"
        verbose_name_plural = "Изображения для игр"


class ModelImageCompany(models.Model):
    image = models.ImageField(verbose_name="Изображение", upload_to='images/')
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    company = models.ForeignKey(ModelCompany, verbose_name="Разработчик", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image}'

    class Meta:
        verbose_name = "Изображения для разработчиков"
        verbose_name_plural = "Изображения для разработчиков"


# теги к играм