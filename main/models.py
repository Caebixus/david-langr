from django.db import models

from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, StreamFieldPanel


class FirstSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Jméno a příjmení"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=80, required=False)
    bg_image = ImageChooserBlock(label="Úvodní obrázek jako pozadí", required=False)

    class Meta:
        template = "blocks/first_section_module.html"
        label = "Úvodní modul s fotografií"
        icon = "list-ul"


class AboutSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Nadpis"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=160, required=False)

    image = ImageChooserBlock(required=True, label=_("profilová fotka"))

    position_name = blocks.CharBlock(label=_("Název pozice"), max_length=80, required=False)

    birthday = blocks.CharBlock(label=_("datum narození"), max_length=80, required=False)
    address = blocks.CharBlock(label=_("adresa"), max_length=80, required=False)
    email = blocks.CharBlock(label=_("email"), max_length=80, required=False)
    freelance_status = blocks.CharBlock(label=_("status"), max_length=80, required=False)

    text = blocks.TextBlock(label=_("text k o mě sekci"), help_text="zobrazí se pod základníma údajema", required=False)

    class Meta:
        template = "blocks/about_section_module.html"
        label = "O mě sekce"
        icon = "list-ul"


class FactsSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Nadpis"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=256, required=False)

    facts_list = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("number", blocks.CharBlock(label="Počet objektů", max_length=10, required=False)),
                ("objects_name", blocks.CharBlock(label="Název objektů", max_length=20, required=False)),
                ("objects_text", blocks.CharBlock(label="Zbytek textace", max_length=40, required=False)),
            ],
            max_num=4,
        ),
    )

    class Meta:
        template = "blocks/facts_section_module.html"
        label = "Sekce Fakta"
        icon = "list-ul"


class SkillsSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Nadpis"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=256, required=False)

    skills_list_left = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("skill_name", blocks.CharBlock(label="Název dovednosti", max_length=60, required=False)),
                ("skill_value", blocks.CharBlock(label="Textová hodnota dovednosti", max_length=60, required=False)),
                ("number_progress_bar", blocks.CharBlock(label="Číselná hodnota progress baru", max_length=60, required=False)),
            ],
        ),
    )

    skills_list_right = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("skill_name", blocks.CharBlock(label="Název dovednosti", max_length=60, required=False)),
                ("skill_value", blocks.CharBlock(label="Textová hodnota dovednosti", max_length=60, required=False)),
                ("number_progress_bar", blocks.CharBlock(label="Číselná hodnota progress baru", max_length=60, required=False)),
            ],
        ),
    )

    class Meta:
        template = "blocks/skills_section_module.html"
        label = "Sekce dovedností"
        icon = "list-ul"


class PortfolioSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Nadpis"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=256, required=False)

    portfolio_list = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(label=_("Obrázek webu, nebo klientovy výpomoci"), required=False)),
                ("portfolio_name", blocks.CharBlock(label="Název klienta či webu", max_length=40, required=False)),
                ("portfolio_url", blocks.URLBlock(label="URL klienta či webu", max_length=80, required=False)),
                ("portfolio_tag", blocks.ChoiceBlock(choices=[
                    ('web', 'Webová stránka'),
                    ('mkt', 'Online Marketing'),
                    ('bth', 'Marketing + Web'),
                ], icon='cup', required=False)),
            ],
        ),
    )

    class Meta:
        template = "blocks/portfolio_section_module.html"
        label = "Sekce Portfolio"
        icon = "list-ul"


class HomePage(Page):
    template = 'pages/index.html'
    max_count = 1
    parent_page_types = ['wagtailcore.Page']

    search_keywords = models.CharField(_('SEO keywords'), max_length=512, blank=True, null=True)
    bg_image = models.ForeignKey(Image, on_delete=models.SET_NULL, related_name="+", null=True, blank=True, verbose_name="Úvodní obrázek jako pozadí")

    content = StreamField([
        ('first_section', FirstSection()),
        ('about_section', AboutSection()),
        ('facts_section', FactsSection()),
        ('skills_section', SkillsSection()),
        ('portfolio_section', PortfolioSection()),
    ], blank=True, null=True)

    content_panels = [
        StreamFieldPanel('content'),
    ]

    page_settings = Page.content_panels + [
        FieldPanel('search_keywords'),
        ImageChooserPanel('bg_image'),
    ]

    promote_panels = Page.promote_panels + [
    ]

    edit_handler = TabbedInterface([
        ObjectList(page_settings, heading='Nastavení stránky'),
        ObjectList(content_panels, heading='Obsah'),
        ObjectList(promote_panels, heading='Propagovat'),
    ])

    class Meta:
        verbose_name = "Index stránka"
        verbose_name_plural = "Index stránky"
