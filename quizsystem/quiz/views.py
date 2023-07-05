from django.shortcuts import redirect, render
from .forms import QuestionForm
from .models import Question
# Create your views here.
def index(request):
    questions = Question.objects.all()
    if request.method == 'POST':
       return render(request,'result.html')
    else:
        questions = Question.objects.all()
    # questions = Question.objects.first()
    return render(request,'index.html',{'questions':questions})

def result(request):
    return render(request,'result.html',{'result':'/result','index':'/index'})

def ownforms(request):
    if request.method == 'POST':
        Qform=QuestionForm(request.POST)
        if Qform.is_valid():
            qname = Qform.cleaned_data['question']
            o1 = Qform.cleaned_data['option1']
            o2 = Qform.cleaned_data['option2']
            o3 = Qform.cleaned_data['option3']
            o4 = Qform.cleaned_data['option4']
            co = Qform.cleaned_data['correct_option']
            # Add more processing as needed

            # Save the form data to the model
            my_model = Question (
                question_name = qname,
                option1 = o1,
                option2 = o2,
                option3 = o3,
                option4 = o4,
                correct_option = co
            )
                # Set other model fields here
            my_model.save()

            # Redirect to a success page
            return redirect('index')
    else:

        forms=QuestionForm()
    return render(request,'questions.html',{'forms':forms})