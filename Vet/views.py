from django.shortcuts import render
from Vet.models import Animal
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "Vet/index.html")


class AnimalList(ListView):
    model = Animal
    context_object_name= "animals"

class AnimalMineList(LoginRequiredMixin, AnimalList):
    
    def get_queryset(self):
        return Animal.objects.filter(propietario=self.request.user.id).all()



class AnimalUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Animal
    success_url = reverse_lazy("animal-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        platillo_id =  self.kwargs.get("pk")
        return Animal.objects.filter(propietario=user_id, id=platillo_id).exists()


class AnimalDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Animal
    context_object_name= "animal"
    success_url = reverse_lazy("animal-list")

    def test_func(self):
        user_id = self.request.user.id
        platillo_id =  self.kwargs.get("pk")
        return Animal.objects.filter(propietario=user_id, id=platillo_id).exists()


class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    success_url = reverse_lazy("animal-list")
    fields = [ 'nombre' ,'detalle', 'precio' ,'imagen']

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)



class AnimalSearch(ListView):
    model = Animal
    context_object_name = "animals"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Animal.objects.filter(nombre=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("animal-list")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('animal-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"

# Create your views here.
