from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Catalog(MPTTModel):
    """
    иерархическое дерево категорий
    :Настроить передачу ссылки:
    """
    name = models.CharField('Название', max_length=255, unique=True, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родитель",
                            related_name='children')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    """
    Представление продукта
    """
    category = models.ForeignKey('Catalog', on_delete=models.PROTECT, null=True)
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', max_length=512, default='', blank=True)
    image = models.ImageField('Изображение', upload_to='image/%Y/%m/%d', blank=True)

    # Добавить проверку '> 0'
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)

    stock = models.PositiveIntegerField('На складе', default=1)
    available = models.BooleanField('Доступно', default=True)

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата редактирования', auto_now=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail',
                       args=[self.id, self.slug])
