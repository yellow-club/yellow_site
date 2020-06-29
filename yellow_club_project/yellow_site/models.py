from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Название')
    slug = models.SlugField(max_length = 255, verbose_name='Url', unique=True)
    author = models.CharField(max_length = 100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Описание')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

