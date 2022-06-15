from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Rune(models.Model):
    title = models.CharField('Название руны', max_length=30)
    content = models.TextField('Описание руны')
    picture = models.ImageField('Графическое изображение', upload_to='photos/')
    count = models.IntegerField('Номер столбца')

    @property
    def photo_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Руна'
        verbose_name_plural = 'Руны'