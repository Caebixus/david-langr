from django.contrib import messages
from django.db import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, StreamFieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel


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


class ServicesSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Nadpis"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=256, required=False)

    services_list = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("services_name", blocks.CharBlock(label="Typ služby", max_length=40, required=False)),
                ("services_text", blocks.TextBlock(label="Textace", max_length=200, required=False)),
            ],
        ),
    )

    class Meta:
        template = "blocks/services_section_module.html"
        label = "Sekce služby"
        icon = "list-ul"


class ContactSection(blocks.StructBlock):
    heading = blocks.CharBlock(label=_("Nadpis"), max_length=60, required=False)
    sub_heading = blocks.CharBlock(label=_("Podnadpis"), max_length=256, required=False)

    class Meta:
        template = "blocks/contact_section_module.html"
        label = "Sekce kontakt"
        icon = "list-ul"


class HomePage(Page):
    template = 'pages/index.html'
    parent_page_types = ['wagtailcore.Page']
    max_count = 2

    search_keywords = models.CharField(_('SEO keywords'), max_length=512, blank=True, null=True)
    bg_image = models.ForeignKey(Image, on_delete=models.SET_NULL, related_name="+", null=True, blank=True, verbose_name="Úvodní obrázek jako pozadí")

    content = StreamField([
        ('first_section', FirstSection()),
        ('about_section', AboutSection()),
        ('facts_section', FactsSection()),
        ('skills_section', SkillsSection()),
        ('portfolio_section', PortfolioSection()),
        ('services_section', ServicesSection()),
        ('contact_section', ContactSection()),
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


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactBlock',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactBlock(AbstractEmailForm):
    template = "pages/contact_page.html"
    max_count = 2
    parent_page_types = ['Homepage']
    subpage_types = []

    intro = RichTextField(blank=True, verbose_name="Úvodní text")
    thank_you_text = RichTextField(blank=True, verbose_name="Text pro děkovací stránku")

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro", classname="full"),
        InlinePanel("form_fields", label="Pole formuláře"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Nastavení emailů",
        ),
    ]

    def send_mail(self, form):
        pass

    def serve(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.get_form(
                request.POST, request.FILES, page=self, user=request.user
            )

            if form.is_valid():
                self.process_form_submission(form)
                return HttpResponse('')
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context["form"] = form
        return TemplateResponse(request, self.get_template(request), context)


class BlogListingPage(Page):
    template = "pages/blog_list.html"
    max_count = 2
    parent_page_types = ['Homepage']

    custom_title = models.CharField(max_length=100, blank=False, null=False)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["blog_list"] = BlogDetailPage.objects.live().public().order_by('first_published_at')
        return context

    content_panels = [
    ]

    page_settings = Page.content_panels + [
        FieldPanel('custom_title'),
    ]

    promote_panels = Page.promote_panels + [
    ]

    edit_handler = TabbedInterface([
        ObjectList(page_settings, heading='Nastavení stránky'),
        ObjectList(content_panels, heading='Obsah'),
        ObjectList(promote_panels, heading='Propagovat'),
    ])

    class Meta:
        verbose_name = "Stránka blogu"
        verbose_name_plural = "Stránky blogu"


class BlogDetailPage(Page):
    template = "pages/blog_detail.html"
    subpage_types = []

    custom_title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, related_name="+", null=True, blank=True, verbose_name="Obrázek článku")
    text = RichTextField(blank=True, verbose_name="Text článku")

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]

    page_settings = Page.content_panels + [
        FieldPanel('custom_title'),
        ImageChooserPanel('image'),
    ]

    promote_panels = Page.promote_panels + [
    ]

    edit_handler = TabbedInterface([
        ObjectList(page_settings, heading='Nastavení stránky'),
        ObjectList(content_panels, heading='Obsah'),
        ObjectList(promote_panels, heading='Propagovat'),
    ])

    class Meta:
        verbose_name = "Detailní stránka článku"
        verbose_name_plural = "Detailní stránky článků"