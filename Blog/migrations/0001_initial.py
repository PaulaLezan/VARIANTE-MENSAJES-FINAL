# Generated by Django 4.1 on 2022-08-07 00:08

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('cuerpo', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]