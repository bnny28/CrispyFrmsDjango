# Generated by Django 4.1.3 on 2022-11-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_candidate_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='situation',
            field=models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Одобрен', 'Одобрен'), ('Отклонен', 'Отклонен')], default='На рассмотрении', max_length=50, null=True, verbose_name='Согласование'),
        ),
    ]