from django.http import HttpResponse # <-- Won't need this once all the methods use render() instead of HttpResponse()
from django.template import loader # <-- ¿Might not need this once all the methods use render() instead of HttpResponse()?
from django.http import Http404 # for NEW detail view
from django.shortcuts import render # for NEW index view

from .models import Question # for NEW index view

# OLD INDEX VIEW
# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = {
#       'latest_question_list': latest_question_list,
#   }
#   # output = ', '.join([q.question_text for q in latest_question_list])
#   # return HttpResponse(output)
#   return HttpResponse(template.render(context, request))

# NEW INDEX VIEW

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist.")
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
