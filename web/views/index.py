import pathlib

from django.shortcuts import render
import json


def index(request):
    f = pathlib.Path(
        'dados.json'
    )
    c = open(f)
    a = json.loads(c.read())

    context = {
        'a': a,
    }

    return render(request, 'index.html', context)
