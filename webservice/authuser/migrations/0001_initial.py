# Generated by Django 4.2.6 on 2023-11-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('level', models.TextField(default='user')),
            ],
        ),
    ]