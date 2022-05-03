# Generated by Django 4.0.4 on 2022-05-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=11, null=True)),
                ('email', models.IntegerField(max_length=50)),
            ],
        ),
    ]
