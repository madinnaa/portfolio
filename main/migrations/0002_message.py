# Generated by Django 4.1.5 on 2023-01-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('text', models.TextField(verbose_name='сообщение')),
            ],
        ),
    ]
