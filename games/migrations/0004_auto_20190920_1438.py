# Generated by Django 2.2.5 on 2019-09-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190917_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='comment',
            field=models.TextField(default='add a comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='Your name', max_length=60),
            preserve_default=False,
        ),
    ]
