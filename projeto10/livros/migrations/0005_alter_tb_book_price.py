# Generated by Django 4.1.1 on 2022-09-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_tb_book_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_book',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]
