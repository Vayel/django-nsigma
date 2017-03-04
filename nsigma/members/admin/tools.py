import urllib.parse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def redirect_add_action(obj, model, params):
    url = reverse(
        'admin:{}_{}_add'.format(
            obj._meta.app_label,
            model._meta.model_name,
        ),
    )

    return redirect(url + '?' + urllib.parse.urlencode(params))
