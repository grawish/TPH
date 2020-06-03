# Generated by Django 3.0.6 on 2020-05-31 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('Content', models.CharField(default='', max_length=10000)),
                ('author', models.CharField(default='', max_length=10)),
                ('Timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
