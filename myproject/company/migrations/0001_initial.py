# Generated by Django 4.1.4 on 2023-04-27 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Не назначено', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ingredients', models.CharField(max_length=128)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('visibility', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='food_photos/')),
                ('mini', models.IntegerField(blank=True, default=0, null=True)),
                ('mini_gram', models.IntegerField(blank=True, default=0, null=True)),
                ('medium', models.IntegerField(default=0)),
                ('medium_gram', models.IntegerField(blank=True, default=0, null=True)),
                ('mega', models.IntegerField(blank=True, default=0, null=True)),
                ('mega_gram', models.IntegerField(blank=True, default=0, null=True)),
                ('value', models.CharField(choices=[('GL', 'Г'), ('ML', 'Мл'), ('It', 'Шт'), ('Lt', 'Литр')], default='GL', max_length=128)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.foodcategory')),
            ],
        ),
    ]
