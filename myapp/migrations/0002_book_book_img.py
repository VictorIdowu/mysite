# Generated by Django 4.2.13 on 2024-06-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(default='default.jpg', upload_to='book_images/'),
        ),
    ]
