# Generated by Django 4.1.7 on 2023-03-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('front_image', models.ImageField(upload_to='images/')),
                ('back_image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
                ('author_name', models.CharField(max_length=50)),
                ('publisher_name', models.CharField(max_length=20)),
                ('book_language', models.CharField(max_length=10)),
                ('book_page', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
