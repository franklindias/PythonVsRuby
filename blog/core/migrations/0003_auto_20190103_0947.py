# Generated by Django 2.1.4 on 2019-01-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190103_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=1024, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]