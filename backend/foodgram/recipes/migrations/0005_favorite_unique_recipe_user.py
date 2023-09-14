# Generated by Django 3.2 on 2023-04-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_merge_20230426_2306'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('recipe', 'user'), name='unique_recipe_user'),
        ),
    ]