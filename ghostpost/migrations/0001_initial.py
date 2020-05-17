# Generated by Django 3.0.6 on 2020-05-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast', models.BooleanField(default=False)),
                ('roast', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=280, null=True)),
                ('up', models.IntegerField(default=0)),
                ('down', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]