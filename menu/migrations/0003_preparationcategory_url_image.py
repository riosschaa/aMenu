# Generated by Django 3.0.8 on 2020-07-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200714_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='preparationcategory',
            name='url_image',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='url imagen'),
        ),
    ]
