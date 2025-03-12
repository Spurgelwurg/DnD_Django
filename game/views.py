from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from game.forms import RegisterForm

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "game/index.html"



def auth_view(request):
    return render(request, 'game/auth.html')

class LoginView(generic.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(request, 'game/login.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('game:index')
        else:
            return render(request, "game/login.html", {'error': 'Invalid username or password'})


class RegisterView(generic.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        form_submitted = False
        return render(request, 'game/register.html', {'form': form, 'form_submitted': form_submitted})

    def post(self, request: HttpRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('game:login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
        form_submitted = True
        return render(request, 'game/register.html', {'form': form, 'form_submitted': form_submitted})

def logout_view(request):
    logout(request)
    return redirect('game:login')



# View: The base class for all views. It doesn't provide any specific functionality but can be extended to create custom views.
# TemplateView: Renders a template. It is used when you need to render a template without any specific context.
# RedirectView: Redirects to a specific URL. It is used when you need to redirect users to another URL.
# DetailView: Renders a detail page for a single object. It is used when you need to display details of a single object.
# ListView: Renders a list of objects. It is used when you need to display a list of objects.
# CreateView: Displays a form for creating a new object and saves the object when the form is submitted.
# UpdateView: Displays a form for updating an existing object and saves the changes when the form is submitted.
# DeleteView: Displays a confirmation page and deletes an object when the confirmation is received.
# FormView: Displays a form and processes the form submission.
            # class ExampleView(generic.TemplateView):
            #     template_name = "game/example.html"

            #     def get_context_data(self, **kwargs):
            #         context = super().get_context_data(**kwargs)
            #         context['example_data'] = 'This is an example'
            #         return context
# ArchiveIndexView: Displays a list of objects grouped by date.
# YearArchiveView: Displays a list of objects for a specific year.
# MonthArchiveView: Displays a list of objects for a specific month.
# WeekArchiveView: Displays a list of objects for a specific week.
# DayArchiveView: Displays a list of objects for a specific day.
# TodayArchiveView: Displays a list of objects for the current day.
# DateDetailView: Displays a detail page for a single object identified by a date.