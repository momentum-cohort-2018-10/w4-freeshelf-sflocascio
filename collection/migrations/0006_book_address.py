# Generated by Django 2.1.3 on 2019-01-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_book_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
