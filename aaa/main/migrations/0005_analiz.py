# Generated by Django 3.2.9 on 2022-04-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_message_onlineorder_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('des', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Анализы',
                'verbose_name_plural': 'Анализы',
            },
        ),
    ]