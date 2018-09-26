from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

def index(request):
    latest_question_list = Card.objects.all()
    context = {'latest_question_list': latest_question_list}

    return render(request, 'LectioEx/index.html', context)

# def detail(request, card_id):
#     try:
#         question = Card.objects.get(pk=card_id)
#     except Card.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'LectioEx/index.html', {'question': question})

