# Generated by Django 4.1.7 on 2023-03-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookShop', '0003_alter_book_publisher_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=300)),
            ],
        ),
    ]