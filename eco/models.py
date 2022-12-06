from django.urls import reverse
from django.db import models

class Info(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('cards', kwargs={'card_name': self.pk})

    class Meta:
        verbose_name = 'Main card'
        verbose_name_plural = 'Main cards'
        ordering = ['id'] # сортировка объектов модели в адм панели



class Codes(models.Model):
    type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True)
    code = models.IntegerField(blank=True, null=True)
    ident = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    using = models.TextField(blank=True)
    recycle = models.BooleanField(default=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    slug = models.SlugField(max_length=50, db_index=True, verbose_name="URL")

    def __str__(self):
            return f"{self.name} | ({self.type})"

    class Meta:
        verbose_name = 'Codes card'
        verbose_name_plural = 'Codes cards'
        ordering = ['type']


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_name': self.slug})
        
    class Meta:
        verbose_name = 'Type of material'
        verbose_name_plural = 'Types of material'
        ordering = ['id']




