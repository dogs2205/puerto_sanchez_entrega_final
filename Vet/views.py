from django.shortcuts import render
from Vet.models import Animal, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "Vet/index.html")

def about (request):
    return render(request, "Vet/about.html")

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
        animal_id =  self.kwargs.get("pk")
        return Animal.objects.filter(propietario=user_id, id=animal_id).exists()


class AnimalDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Animal
    context_object_name= "animal"
    success_url = reverse_lazy("animal-list")

    def test_func(self):
        user_id = self.request.user.id
        animal_id =  self.kwargs.get("pk")
        return Animal.objects.filter(propietario=user_id, id=animal_id).exists()


class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    success_url = reverse_lazy("animal-list")
    fields = [ 'nombre_animal' ,'tipo_animal', 'edad_animal' ,'precio_tratamiento','pre_diagnostico', 'imagen','propietario' ]

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)

class AnimalDetail(DetailView):
    model = Animal
    context_object_name = "animal"

class AnimalSearch(ListView):
    model = Animal
    context_object_name = "animals"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Animal.objects.filter(nombre=criterio).all()
        return result

class Login(LoginView):
    template_name = 'registration/login.html'
    next_page = reverse_lazy("animal-list")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('animal-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("animal-list")
    fields = ['avatar',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("animal-list")
    fields = ['avatar',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()

class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()



# Create your views here.
