# Generated by Django 4.1.7 on 2023-04-01 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_is_active_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='booked_till',
            new_name='end_at',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='updated',
            new_name='start_from',
        ),
    ]
