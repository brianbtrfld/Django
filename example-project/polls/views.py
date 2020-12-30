#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    # output = ', '.join([q.question_text for q in latest_question_list])

    # Loads template.
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')    
    #context = {'latest_question_list': latest_question_list,}
    #return HttpResponse(template.render(context, request))

    # Uses render https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-render
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    # Ref:  https://docs.djangoproject.com/en/3.1/intro/tutorial03/#raising-a-404-error
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist.")
    #return render(request = request, template_name = 'polls/details.html', context = {'question': question})

    # Ref:  https://docs.djangoproject.com/en/3.1/intro/tutorial03/#a-shortcut-get-object-or-404
    question = get_object_or_404(Question, pk=question_id)
    return render(request = request, template_name = 'polls/detail.html', context = {'question': question})

def results(request, question_id):
    response = "You're looking at the the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)