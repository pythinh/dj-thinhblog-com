# Generated by Django 3.0.7 on 2020-06-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0024_auto_20200624_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='paginate',
            field=models.IntegerField(default=2, verbose_name='Phân trang'),
        ),
    ]