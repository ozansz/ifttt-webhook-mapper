import requests

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import GetToPostRequestMapping

def make_post_request_to_webhook(request, tag):
    _MAPPER_PARAMS = {
        "v1": "value1",
        "v2": "value2",
        "v3": "value3",
    }

    try:
        intent = GetToPostRequestMapping.objects.get(tag=tag)
    except ObjectDoesNotExist:
        return render(request, "mapper/error.html", {
            "code": "tag-dne",
            "reason": "path-param::tag",
            "details": f"No mapping found with the tag '{tag}'"
        })

    post_data = dict()

    for query_param, post_param in _MAPPER_PARAMS.items():
        qpval = request.GET.get(query_param, None)

        if qpval is not None:
            post_data[post_param] = qpval

    res = requests.post(
        f"https://maker.ifttt.com/trigger/{intent.trigger_action}/with/key/{intent.trigger_key}",
        json=post_data
    )

    if res.status_code < 400:
        return render(request, "mapper/success.html")

    return render(request, "mapper/error.html", {
        "code": "request-error",
        "reason": f"status_code::{res.status_code}",
        "details": f"POST request returned with a non-200 status code",
        "extra": res.text
    })