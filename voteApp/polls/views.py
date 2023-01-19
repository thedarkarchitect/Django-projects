from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse, Http404

from .models import Questions, Choices

# Create your views here.
def index(request):#Gets questions and displayes them 
    lastest_question_list = Questions.objects.order_by('-pub_date')[:5]#this contains the questions objects in the Question model
    context = {'latest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)

# show specific questions and choices
def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)#this get the questions for the db by their id 
    except Questions.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):#Gets questions and displayes the results
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):#vote for questino choices available
    #print(request.POST['choice'])--> this was ued to show the choices in the terminal that we are going to display on the page
    question = get_object_or_404(Questions, pk=question_id)#this method will get from the question model by pk but if the pk doesn't exist the method will return a 404

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message':"You didn't selete a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #after successfull dealin always return an HttpRespONSEredirect
        #with Post data. this prevents data from being posted twice if a user hit the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))

