# Generated by Django 5.0.4 on 2024-04-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipename', models.CharField(max_length=100)),
                ('receipedesc', models.TextField()),
                ('receipeimg', models.FileField(upload_to='receipes/')),
            ],
        ),
    ]
