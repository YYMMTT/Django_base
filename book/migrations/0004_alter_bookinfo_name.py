# Generated by Django 4.0.5 on 2022-06-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_peopleinfo_description_peopleinfo_is_delete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]