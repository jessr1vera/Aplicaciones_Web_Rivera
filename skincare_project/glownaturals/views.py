from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Producto
from glownaturals.forms import ProductoForm

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_producto.html'
    success_url = '/productos/'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'editar_producto.html'
    success_url = '/productos/'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = '/productos/'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'ver_producto.html'


class IndexView(TemplateView):
    template_name = 'index.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home') 