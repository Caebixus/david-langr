from wagtail.models import Site
from main.models import ContactBlock
from settings.models import MySettings


def template_settings(request):
    settings = MySettings.for_request(request)

    return {'my_settings': settings}


def form_modal(request):
    site = Site.find_for_request(request)
    if ContactBlock.objects.in_site(site).exists():
        contact_block = ContactBlock.objects.in_site(site).first()
        form_modal = contact_block.get_form()

        return {
            "contact_block": contact_block,
            "form_modal": form_modal,
        }

    else:
        form_modal = None

        return {
            "form_modal": form_modal,
        }
