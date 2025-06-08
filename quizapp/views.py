from django.shortcuts import render, redirect
from .models import Category, Question

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories' : categories})

def quiz(request, category_id):
    category = Category.objects.get(id = category_id)
    questions = Question.objects.filter(category = category)
    return render(request, 'quiz.html', {'category': category, 'questions' : questions})

def submit(request):
    if request.method == 'POST':
        score = 0 
        total = int(request.POST['total_questions'])
        for key in request.POST:
            if key.startswith('question_'):
                qid = int(key.split('_')[1])
                selected = request.POST[key]
                question = Question.objects.get(id= qid)
                if question.correct_option == selected:
                    score += 1
        return render(request, 'result.html', {'score' : score, 'total' : total})
    return redirect('home')