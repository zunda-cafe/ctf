from django.http import HttpResponse
from django.shortcuts import render
from challenge.models import Question

def index(request):
    #print(request.META.get('REMOTE_ADDR'))
    questions = Question.objects.filter(status="public").order_by('disp_no')
    print(questions.query)
    return render(request,
                  'challenge/index.html',
                  {'questions': questions})

def show(request, question_id):
    return HttpResponse("show: {}".format(question_id))
