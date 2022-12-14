# Generated by Django 4.1.3 on 2022-11-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=50, verbose_name='Эл.почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
