from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Catalog(MPTTModel):
    """
    иерархическое дерево категорий
    """
    title = models.CharField('Название', max_length=255, unique=True, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родитель",
                            related_name='children')

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    связанный с категорией каталога
    Когда вы используете классы FileField или ImageField, Django предоставляет интерфейс программирования приложений
    (API), чтобы открыть вам доступ к файлам. Этот объект – car. photo является файловым объектом, а значит имеет ряд
    атрибутов, описанных ниже.
    """
    title = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание', max_length=512, default='')
    category = models.ForeignKey('Catalog', on_delete=models.PROTECT, null=True)
    image = models.ImageField('Изображение', upload_to='image/')

    # Добавить проверку '> 0' и приписку 'р'
    price = models.IntegerField('Цена', default=99)

    def __str__(self):
        return f'{self.title}. Цена: {self.price} р.'


class Basket(models.Model):
    """
    корзина \ заказ наборов товаров, изменение статусов заказов, завершение
    """
    ...


class Promo_abstraction(models.Model):
    """
    объединения между собой товаров в “акцию”, с дополнительными условиями
    """
    ...
