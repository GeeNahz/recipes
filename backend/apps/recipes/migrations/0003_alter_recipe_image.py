# Generated by Django 4.2 on 2024-10-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='<function file_upload_path at 0x7408b48ce5f0>'),
        ),
    ]
