# Generated by Django 2.2.5 on 2019-09-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20190920_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.URLField(blank=True, max_length=2083),
        ),
    ]
