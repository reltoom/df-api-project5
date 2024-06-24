# Generated by Django 3.2.4 on 2024-06-24 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('measurement', models.CharField(choices=[('milliliter - ml', 'milliliter - ml'), ('deciliter - dl', 'deciliter - dl'), ('litre - l', 'litre - l'), ('teaspoon - tsp', 'teaspoon - tsp'), ('tablespoon - tbsp', 'tablespoon - tbsp'), ('fluid ounce - fl oz', 'fluid ounce - fl oz'), ('cup - c', 'cup - c'), ('pint - pt', 'pint - pt'), ('quart - qt', 'quart - qt'), ('gallon - gal', 'gallon - gal'), ('milligram - mg', 'milligram - mg'), ('gram - g', 'gram - g'), ('kilogram - kg', 'kilogram - kg'), ('pound - lb', 'pound - lb'), ('ounce - oz', 'ounce - oz')], default='gram - g', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_post_kk2xpx', upload_to='images/')),
                ('ingredients', models.ManyToManyField(related_name='posts', to='posts.Ingredient')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
