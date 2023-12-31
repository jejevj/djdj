# Generated by Django 4.2.5 on 2023-11-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDriver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('hp', models.TextField()),
                ('photo', models.TextField()),
                ('lat', models.TextField(default='-6.1661686')),
                ('lon', models.TextField(default='106.8717686')),
                ('level', models.TextField(default='driver')),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
