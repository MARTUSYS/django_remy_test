# Generated by Django 3.2.9 on 2021-11-24 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211124_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.catalog'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='image/', verbose_name='Изображение'),
        ),
    ]