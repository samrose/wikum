# Generated by Django 2.1.1 on 2020-03-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0066_auto_20200226_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='drag_locked',
            field=models.BooleanField(default=False),
        ),
    ]
