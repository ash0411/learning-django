# Generated by Django 2.2.4 on 2019-09-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190925_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
