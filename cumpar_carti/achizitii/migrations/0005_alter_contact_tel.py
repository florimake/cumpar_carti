# Generated by Django 4.2.5 on 2023-11-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achizitii', '0004_alter_paragraf_poza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tel',
            field=models.CharField(max_length=50),
        ),
    ]
