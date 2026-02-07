from unittest import loader
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Question
from .models import Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    print("question_id %s" % question_id, flush=True)
    detail_question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": detail_question})


def result(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)