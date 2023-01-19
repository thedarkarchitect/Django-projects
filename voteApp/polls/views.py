from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse

from .models import Questions, Choices

# Create your views here.
def index(request):#Gets questions and displayes them 
    lastest_question_list = Questions.objects.order_by('-pub_date')[:5]#this contains the questions objects in the Question model
    context = {'latest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)

#show specific questions and choices
# def detail(request, question_id):
#     try:
#         question = Questions.objects.get(pk=question_id)#this get the questions for the db by their id 
#     except Questions.DoesNotExist:
#         raise Http404("Question does not exit")
#     return render(request, 'polls/detail.html', {'question':question})