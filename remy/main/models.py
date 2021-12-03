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
    # Про товар
    category = models.ForeignKey('Catalog', on_delete=models.PROTECT, null=True)
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', max_length=512, default='', blank=True)
    image = models.ImageField('Изображение', upload_to='image/%Y/%m/%d', blank=True)

    # Добавить проверку '> 0'
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)

    # Скидка
    # Добавить проверку '> 0'
    discount = models.DecimalField('Процент cкидки', max_digits=4, decimal_places=2, default=0)
    discount_activated = models.BooleanField('Скидка', default=False)

    # Склад
    stock = models.PositiveIntegerField('На складе', default=1)
    available = models.BooleanField('Доступно', default=True)

    # Метаданные
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

    def price_mod(self):
        self.price = abs(self.price)
        # Проверка и применение скидки
        if 0 < self.discount < 100 and self.discount_activated:
            self.price = round(self.price * (100 - self.discount) / 100, 2)
