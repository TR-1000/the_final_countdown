# Generated by Django 2.2.5 on 2019-09-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.CharField(default='https://ih0.redbubble.net/image.587670080.3877/flat,550x550,075,f.u1.jpg', max_length=200),
            preserve_default=False,
        ),
    ]