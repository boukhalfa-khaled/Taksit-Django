# Generated by Django 5.0.6 on 2024-05-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('seller', 'Seller'), ('invester', 'Invester')], default='customer', max_length=20),
        ),
    ]
