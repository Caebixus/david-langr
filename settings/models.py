from django.db import models
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class MySettings(BaseSetting):
    full_name = models.CharField(max_length=255, help_text='Celé jméno', blank=True, null=True)
    email = models.CharField(max_length=255, help_text='Email', blank=True, null=True)
    street = models.CharField("Ulice", max_length=128, blank=True, null=True)
    city = models.CharField("Město", max_length=128, blank=True, null=True)
    zip = models.CharField("PSČ", max_length=32, blank=True, null=True)
    ico = models.CharField("IČO", max_length=32, blank=True, null=True)
    basic_panels = [
        FieldPanel("full_name"),
        FieldPanel("email"),
        FieldPanel("street"),
        FieldPanel("city"),
        FieldPanel("zip"),
        FieldPanel("ico"),
    ]

    logo = models.ForeignKey("wagtailimages.Image", on_delete=models.PROTECT, null=True, blank=True, related_name="+")
    dark_logo = models.ForeignKey("wagtailimages.Image", on_delete=models.PROTECT, null=True, blank=True, related_name="+", verbose_name="Logo pro tmavé pozadí")
    favicon = models.ForeignKey("wagtailimages.Image", on_delete=models.PROTECT, null=True, blank=True, related_name="+", verbose_name="Favicona")
    favicon_apple = models.ForeignKey("wagtailimages.Image", on_delete=models.PROTECT, null=True, blank=True, related_name="+", verbose_name="Favicona pro apple")
    logo_panels = [
        ImageChooserPanel("logo"),
        ImageChooserPanel("dark_logo"),
        ImageChooserPanel("favicon"),
        ImageChooserPanel("favicon_apple"),
    ]

    facebook = models.URLField(help_text='Your Facebook page URL', blank=True, null=True)
    instagram = models.URLField(help_text='Your Instagram page URL', blank=True, null=True)
    linkedin = models.URLField(help_text='Your LinkedIn page URL', blank=True, null=True)
    twitter = models.URLField(help_text="Your Twitter page URL", blank=True, null=True)
    social_panels = [
        FieldPanel("linkedin"),
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(basic_panels, heading='Základní nastavení'),
        ObjectList(logo_panels, heading='Logo a favicony'),
        ObjectList(social_panels, heading='Sociální sítě'),
    ])

    class Meta:
        verbose_name = "Globální nastavení"
