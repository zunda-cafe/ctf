from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from challenge.models import Question
from challenge.models import Winner
from challenge.forms import QuestionForm

def index(request):
    #print(request.META.get('REMOTE_ADDR'))
    questions = Question.objects.filter(status="public").order_by('disp_no')
    # print(questions.query)
    return render(request,
                  'challenge/index.html',
                  {'questions': questions})

def ranking(request):
    rankings = Winner.objects.values('name').annotate(point = Sum('point')).order_by('-point')
    #print(rankings)
    return render(request,
                  'challenge/ranking.html',
                  {'rankings': rankings})


def show(request, question_id):
    question = Question.objects.get(pk=question_id)

    print(request.method)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            flag = form.cleaned_data['flag']
            if flag == question.flag:
                nn = request.COOKIES.get('NickName')
                if nn != None:
                    print("### {} {} ###".format(nn, question.valid_point()))
                    winner, created = Winner.objects.get_or_create(name=nn,
                                point=question.valid_point(),
                                question=question)
                url = 'question.good'
            else:
                url = 'question.mistake'
            return redirect(url, question_id=question_id)
    form = QuestionForm(instance=None)
    winners = Winner.objects.filter(question=question)
    return render(request,
                  'challenge/show.html',
                  {'form': form, 'question': question, 'winners': winners})

def good(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'challenge/good.html',
                  {'question': question})

def mistake(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'challenge/mistake.html',
                  {'question': question})

