# Generated by Django 4.0.4 on 2022-05-24 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysettings',
            name='dark_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image', verbose_name='Logo pro tmavé pozadí'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='favicon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image', verbose_name='Favicona'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='favicon_apple',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image', verbose_name='Favicona pro apple'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
    ]