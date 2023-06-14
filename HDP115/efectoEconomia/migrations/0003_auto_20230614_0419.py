# Generated by Django 3.2.19 on 2023-06-14 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efectoEconomia', '0002_noticia_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='categoria',
            new_name='tipo_categoria',
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]