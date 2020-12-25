from django.shortcuts import render

from django.template import RequestContext


def main(request):
    return render(request, 'main/main.html')

