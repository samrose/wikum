# Generated by Django 3.0.5 on 2020-04-04 16:24

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0069_wikumuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikumuser',
            name='id',
        ),
        migrations.AddField(
            model_name='wikumuser',
            name='subscribe_edit',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='wikumuser',
            name='subscribe_replies',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='wikumuser',
            name='user',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
