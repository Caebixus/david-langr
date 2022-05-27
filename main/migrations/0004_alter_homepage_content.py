# Generated by Django 4.0.4 on 2022-05-27 16:09

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_homepage_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('first_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Jméno a příjmení', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=80, required=False)), ('bg_image', wagtail.images.blocks.ImageChooserBlock(label='Úvodní obrázek jako pozadí', required=False))])), ('about_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Nadpis', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=160, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='profilová fotka', required=True)), ('position_name', wagtail.blocks.CharBlock(label='Název pozice', max_length=80, required=False)), ('birthday', wagtail.blocks.CharBlock(label='datum narození', max_length=80, required=False)), ('address', wagtail.blocks.CharBlock(label='adresa', max_length=80, required=False)), ('email', wagtail.blocks.CharBlock(label='email', max_length=80, required=False)), ('freelance_status', wagtail.blocks.CharBlock(label='status', max_length=80, required=False)), ('text', wagtail.blocks.TextBlock(help_text='zobrazí se pod základníma údajema', label='text k o mě sekci', required=False))])), ('facts_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Nadpis', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=256, required=False)), ('facts_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('number', wagtail.blocks.CharBlock(label='Počet objektů', max_length=10, required=False)), ('objects_name', wagtail.blocks.CharBlock(label='Název objektů', max_length=20, required=False)), ('objects_text', wagtail.blocks.CharBlock(label='Zbytek textace', max_length=40, required=False))], max_num=4)))])), ('skills_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Nadpis', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=256, required=False)), ('skills_list_left', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('skill_name', wagtail.blocks.CharBlock(label='Název dovednosti', max_length=60, required=False)), ('skill_value', wagtail.blocks.CharBlock(label='Textová hodnota dovednosti', max_length=60, required=False)), ('number_progress_bar', wagtail.blocks.CharBlock(label='Číselná hodnota progress baru', max_length=60, required=False))]))), ('skills_list_right', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('skill_name', wagtail.blocks.CharBlock(label='Název dovednosti', max_length=60, required=False)), ('skill_value', wagtail.blocks.CharBlock(label='Textová hodnota dovednosti', max_length=60, required=False)), ('number_progress_bar', wagtail.blocks.CharBlock(label='Číselná hodnota progress baru', max_length=60, required=False))])))])), ('portfolio_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Nadpis', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=256, required=False)), ('portfolio_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Obrázek webu, nebo klientovy výpomoci', required=False)), ('portfolio_name', wagtail.blocks.CharBlock(label='Název klienta či webu', max_length=40, required=False)), ('portfolio_url', wagtail.blocks.URLBlock(label='URL klienta či webu', max_length=80, required=False)), ('portfolio_tag', wagtail.blocks.ChoiceBlock(choices=[('web', 'Webová stránka'), ('mkt', 'Online Marketing'), ('bth', 'Marketing + Web')], icon='cup', required=False))])))])), ('services_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Nadpis', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=256, required=False)), ('services_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('services_name', wagtail.blocks.CharBlock(label='Typ služby', max_length=40, required=False)), ('services_text', wagtail.blocks.TextBlock(label='Textace', max_length=200, required=False))])))])), ('contact_section', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Nadpis', max_length=60, required=False)), ('sub_heading', wagtail.blocks.CharBlock(label='Podnadpis', max_length=256, required=False))]))], blank=True, null=True, use_json_field=None),
        ),
    ]