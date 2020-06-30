from django.shortcuts import render
from .models import Daily
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def home(request):
    context = {
        'dailys': Daily.objects.all()
    }
    return render(request, 'myapp/home.html', context)

class DailyListView(ListView):
    model = Daily
    template_name = 'myapp/home.html'  #
    context_object_name = 'dailys'
    ordering = ['-date_posted']
    paginate_by = 4


class UserDailyListView(ListView):
    model = Daily
    template_name = 'myapp/user_dailys.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'dailys'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Daily.objects.filter(author=user).order_by('-date_posted')


class DailyDetailView(DetailView):
    model = Daily


class DailyCreateView(LoginRequiredMixin, CreateView):
    model = Daily
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DailyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Daily
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        daily = self.get_object()
        if self.request.user == daily.author:
            return True
        return False


class DailyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Daily
    success_url = '/'

    def test_func(self):
        daily = self.get_object()
        if self.request.user == daily.author:
            return True
        return False


def about(request):
    daily =get_object_or_404(Daily,pk=1) #pk=pk
    context={'daily':daily,'title':'Details'}
    return render(request, 'myapp/about.html', context)