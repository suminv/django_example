# Generated by Django 3.2.5 on 2021-07-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0005_rename_bublicationdata_book_publication_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birth_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='personal_page',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='university',
            field=models.CharField(max_length=30, null=True),
        ),
    ]