# Generated by Django 3.0.6 on 2020-06-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sorter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_by', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='boast',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='private_url',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='public_url',
            field=models.CharField(max_length=30, null=True),
        ),
    ]