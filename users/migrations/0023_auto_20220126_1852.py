# Generated by Django 3.2.9 on 2022-01-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_factory_signal'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='star6',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
        migrations.AddField(
            model_name='factory',
            name='start1',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
        migrations.AddField(
            model_name='factory',
            name='start2',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
        migrations.AddField(
            model_name='factory',
            name='start3',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
        migrations.AddField(
            model_name='factory',
            name='start4',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
        migrations.AddField(
            model_name='factory',
            name='start5',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
        migrations.AddField(
            model_name='factory',
            name='start7',
            field=models.BooleanField(default=False, verbose_name='выполнение начато'),
        ),
    ]
