# Generated by Django 3.0.7 on 2020-08-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200824_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='skus',
            name='code',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]