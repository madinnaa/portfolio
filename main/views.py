from django.shortcuts import render
from main.models import Skill, Message , Project 
from django.http import HttpResponseRedirect
# Create your views here.
def main(request):
    skills = Skill.objects.all()
    project = Project.objects.all()
    return render(request, 'portfolio.html', {'skill': skills,'project':project})


def massage(request):
    if request.method == 'Post':
       message = Message()
       message.name = request.Post.get('name')
       message.name = request.Post.get('email')
       message.name = request.Post.get('message')
       message.save()
    return HttpResponseRedirect('/')



