# Generated by Django 4.0.4 on 2022-05-17 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_book_rent_alter_book_edition_alter_book_pages_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookSeller',
            new_name='BookRenter',
        ),
    ]