# Generated by Django 3.0.7 on 2020-06-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]