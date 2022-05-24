from settings.models import MySettings


def template_settings(request):
    settings = MySettings.for_request(request)

    return {'my_settings': settings}
