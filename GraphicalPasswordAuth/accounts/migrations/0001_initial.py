# Generated by Django 3.2.12 on 2022-03-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_accounts',
            fields=[
                ('email', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('unique_image', models.CharField(max_length=250)),
                ('user_pass', models.CharField(max_length=200)),
            ],
        ),
    ]