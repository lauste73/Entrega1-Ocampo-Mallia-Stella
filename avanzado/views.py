from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from avanzado.models import Publicacion
from avanzado.forms import BusquedaPublicacion

class ListaPublicacion(ListView):
    model = Publicacion
    template_name = 'avanzado/ver_publicaciones.html'
    
    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaPublicacion()
        return context
    

class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    success_url = '/avanzado/ver-publicaciones/'
    template_name = 'avanzado/crear_publicacion.html'
    fields = ['titulo', 'subtitulo','linea_texto', 'imagen','fecha_creacion',]

class EditarPublicaion(LoginRequiredMixin, UpdateView):
    model = Publicacion
    success_url = '/avanzado/ver-publicaciones/'
    template_name = 'avanzado/editar_publicacion.html'
    fields = ['titulo', 'subtitulo', 'linea_texto', 'imagen','fecha_creacion']
    

class EliminarPublicacion(LoginRequiredMixin, DeleteView):
    model = Publicacion
    success_url = '/avanzado/ver-publicaciones/'
    template_name = 'avanzado/eliminar_publicacion.html'
    

class DescPublicacion(LoginRequiredMixin,DetailView):
    model = Publicacion
    template_name = 'avanzado/descripcion_publicacion.html'


 





