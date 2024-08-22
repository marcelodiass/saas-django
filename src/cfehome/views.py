from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    context = {
        "title": "Home Page",
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent" : (page_qs.count() * 100) / qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", context)

