from django.http import HttpResponse # <-- Won't need this once all the methods use render() instead of HttpResponse()
from django.http import HttpResponse, HttpResponseRedirect # <-- added this for vote view from part 4
from django.template import loader # <-- ¿Might not need this once all the methods use render() instead of HttpResponse()?
# from django.http import Http404 # used this first to create 404 exceptions, but now we're using get_objeft_or_404()
# from django.shortcuts import render # used for revised index view; getting rid of this bc I think it's baked into get_object_or_404, render below
from django.shortcuts import get_object_or_404, render
from django.urls import reverse # <-- added this for vote view from part 4

from .models import Question # for NEW index view
from .models import Choice, Question # <-- does this need to be in a separate line from the line before? or are these lines redundant? added this for vote view from part 4. 

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
  question = get_object_or_404(Question, pk=question_id)
  # try:            <<<   # the try & except here is all baked into the get_object_or_404 now
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist.")
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    
  return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
