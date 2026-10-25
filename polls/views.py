from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import Question, Choice

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice_id = request.POST.get('choice')

    if not selected_choice_id:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Zəhmət olmasa bir variant seçin.",
        })

    choice = get_object_or_404(Choice, pk=selected_choice_id, question=question)
    choice.votes = F('votes') + 1
    choice.save()

    return redirect('polls:results', question_id=question.id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})