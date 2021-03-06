# Generated by Django 4.0.4 on 2022-05-22 19:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('search_keywords', models.CharField(blank=True, max_length=512, null=True, verbose_name='SEO keywords')),
                ('content', wagtail.fields.StreamField([('first_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Jméno a příjmení', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=80, required=False))]))], blank=True, null=True, use_json_field=None)),
            ],
            options={
                'verbose_name': 'Index stránka',
                'verbose_name_plural': 'Index stránky',
            },
            bases=('wagtailcore.page',),
        ),
    ]
