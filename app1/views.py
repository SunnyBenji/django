import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from PIL import Image

from .models import Question
from .form import QuestionForm


def index(request):
    try:
        question_list = Question.objects.all()
        context = {
            'questions': question_list,
        }
    except: 
        raise Http404("Question does not exist")
    return render(request, 'app1/index.html', context)
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question':question,
        }
    except Question.DoesNotExist:
        raise Http404("Cette question n'existe pas")
    return render(request, 'app1/detail.html', context)
def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('app1:index')
            except:
                pass
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request,'app1/create.html', context)

def edit(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Cette question n'existe pas")
    
    form = QuestionForm(instance=question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('app1:index')
            except:
                pass
    context = {
        'form': form,
        'question':question,
    }
    return render(request, 'app1/edit.html', context)
def delete(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Cette question n'existe pas")
    if request.method == "POST":
        question.delete()
        return redirect('app1:index')

    context = {
        'question': question,
    }
    return render(request, 'app1/delete.html', context)

# Create your views here.
