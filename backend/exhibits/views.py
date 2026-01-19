from django.shortcuts import render, get_object_or_404
from .models import Exhibit

def exhibit_list(request):
    exhibits = Exhibit.objects.all()
    return render(request, "exhibit_list.html", {"exhibits": exhibits})

def exhibit_detail(request, exhibit_id):
    exhibit = get_object_or_404(Exhibit, id=exhibit_id)
    quizzes = exhibit.quizzes.all()
    return render(request, "exhibit_detail.html", {"exhibit": exhibit, "quizzes": quizzes})
