from django.shortcuts import render, get_object_or_404
from .models import Exhibit

def exhibit_list(request):
    exhibits = Exhibit.objects.all()
    return render(request, "exhibits/exhibit_list.html", {
        "exhibits": exhibits
    })

def exhibit_detail(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    quizzes = exhibit.quiz_set.all()
    return render(request, "exhibits/exhibit_detail.html", {
        "exhibit": exhibit,
        "quizzes": quizzes
    })
