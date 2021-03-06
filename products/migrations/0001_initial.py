# Generated by Django 4.0 on 2021-12-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagem')),
                ('price', models.PositiveIntegerField(verbose_name='Preço')),
            ],
        ),
    ]
