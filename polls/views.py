"""
CITATION
Used https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#generic_editing_views
to figure out how to use forms and the HTML for it



"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, DeepThought

from .forms import DeepThoughtForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class DeepThoughtListView(generic.ListView):
    template_name = 'polls/deep_thought.html'
    context_object_name = 'deep_thoughts_list'

    def get_queryset(self):
        """
        Displays all of the deep thoughts submitted so far
        """
        return DeepThought.objects.all()

    # latest_deep_thoughts_list = DeepThought.objects.order_by('-pub_date')
    # output = ', '.join([dt.thoughts_text for dt in latest_deep_thoughts_list])
    # return HttpResponse(output)

# class DeepThoughtSubmitView(generic.ListView):
#     template_name = 'polls/deep_thought_submit.html'
#     # used https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#generic_editing_views
#     # for learning how to make a submit form with HTML
#     model = DeepThought

#     def get_queryset(self):
#         """
#         Displays all of the deep thoughts submitted so far
#         """
#         return DeepThought.objects.filter(
#             pub_date__lte=timezone.now()
#         )

def submit_deep_thought(request):
    # thought = get_object_or_404(DeepThought)
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    # If this is a POST request then process the Form data
    
    if request.method == 'POST':
        print("hi")
        # Create a form instance and populate it with data from the request (binding):
        form = DeepThoughtForm(request.POST)
        # print("AHH")
        # # Check if the form is valid:
        if form.is_valid():
            print("YAY")
            form.save() # save to database
        context = {
            'form': form,
            'submit_alert': "submitted ;)"
        }
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        return render(request, 'polls/deep_thought_submit.html', context)
    else:     
        # If this is a GET (or any other method) create the default form.
        form = DeepThoughtForm()
        
    return render(request, 'polls/deep_thought_submit.html', {'form': form})
    

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    latest_question_list = []

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))