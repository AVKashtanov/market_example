# Generated by Django 2.2.7 on 2020-03-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postavschik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogrn', models.PositiveIntegerField(unique=True, verbose_name='ОГРН')),
                ('name', models.CharField(max_length=100, verbose_name='Организация')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True, verbose_name='Код товара')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Sklad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='marketapp.Tovar', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склад',
            },
        ),
        migrations.CreateModel(
            name='Postavka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('count_post', models.CharField(max_length=100, verbose_name='Количество товара')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketapp.Tovar', verbose_name='Товар')),
                ('postavschik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketapp.Postavschik', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставка',
                'verbose_name_plural': 'Поставки',
            },
        ),
    ]
