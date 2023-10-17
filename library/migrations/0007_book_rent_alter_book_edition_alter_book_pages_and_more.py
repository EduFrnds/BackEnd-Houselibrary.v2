# Generated by Django 4.0.4 on 2022-05-03 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_bookseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rent',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookseller',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='bookseller',
            name='phone_number',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]