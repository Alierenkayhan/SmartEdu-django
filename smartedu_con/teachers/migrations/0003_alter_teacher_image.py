# Generated by Django 4.2.13 on 2024-06-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='teachers/default_user_photo.png', upload_to='teachers/%Y/%m/%d/'),
        ),
    ]
