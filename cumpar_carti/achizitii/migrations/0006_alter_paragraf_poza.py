# Generated by Django 4.2.5 on 2023-11-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achizitii', '0005_alter_contact_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraf',
            name='poza',
            field=models.ImageField(null=True, upload_to='achizitii/static/images'),
        ),
    ]
