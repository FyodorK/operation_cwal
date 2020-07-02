from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, WebPage, AccessRecord
from . import forms


def view_one(r):
    out = "<h1>Put some text</h1>"
    return HttpResponse(out)


def view_two(r):
    out = "<script> alert('Second view')</script>"
    return HttpResponse(out)


def index(r):
    """
    wb = AccessRecord.objects.order_by('date')
    d = {'insert_me': wb}
    return render(r, 'app_one/index.html', context=d)
    """
    return render(r, 'app_one/index2.html')


def form_name_view(r):
    form = forms.FormName()
    if r.method == 'POST':
        form = forms.FormName(r.POST)
        if form.is_valid():
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"TEXT: {form.cleaned_data['text']}")
        else:
            print("0")

    return render(r, 'app_one/form_page.html', {'form': form})
