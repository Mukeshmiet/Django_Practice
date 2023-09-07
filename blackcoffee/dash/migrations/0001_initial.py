# Generated by Django 4.2.4 on 2023-09-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('sector', models.TextField(blank=True, null=True)),
                ('topic', models.TextField(blank=True, null=True)),
                ('insight', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('region', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('added', models.DateTimeField(blank=True, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('likelihood', models.IntegerField(blank=True, null=True)),
                ('pestle', models.TextField(blank=True, null=True)),
                ('impact', models.TextField(blank=True, null=True)),
                ('start_year', models.IntegerField(blank=True, null=True)),
                ('end_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]