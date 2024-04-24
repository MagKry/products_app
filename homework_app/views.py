from urllib import request

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, FormView
from django.db.models import Q

from .forms import AddCategoryForm, EditCategoryForm, SearchForm, LoginForm
from .models import Category, Product


# Create your views here.

class CategoriesView(View):

    def get(self, request):
        categories = Category.objects.all().order_by('category_name')
        user = request.user
        user.has_perm('change_category')
        return render(request, 'category_list.html', {"categories": categories, 'user': user})



class CategoryDetails(View):

    def get(self, request, slug):
        products = Product.objects.filter(categories__category_name__icontains=slug).order_by('name')
        for product in products:
            product.price = product.price + product.vat

        return render(request, 'products_per_category.html', {'products': products})


class ProductDetails(View):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        return render(request, 'product_details.html', {"product": product})


class AddCategoryView(PermissionRequiredMixin, View):
    template_name = 'homework_form.html'
    form_class = AddCategoryForm
    permission_required = 'add_category'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category_name']
            category = Category.objects.create(category_name=category, slug=category)
            return redirect('categories')


class EditCategoryView(PermissionRequiredMixin, View):
    template_name = 'homework_form.html'
    form_class = EditCategoryForm
    permission_required = 'change_category'

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        form = self.form_class(instance=category)
        return render(request, self.template_name,{'form': form})

    def post(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_category = form.cleaned_data['category_name']
            category = Category.objects.get(slug=slug)
            category.category_name=new_category
            category.slug=new_category
            category.save()
            return redirect('categories')


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'


class EditProductView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product_update_form.html'
    # template_name_suffix = '_update_form' #z tego można skorzystać, gdy ma się już szablon product?#lepiej podawać pelne nazwy szablonow jest to mniej mylace
    success_url = reverse_lazy('products')
    permission_required = 'change_product'


class AddProductView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = '/products'
    permission_required = 'add_product'


class SearchView(View):
    template_name = 'search.html'
    form_class = SearchForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            result = form.cleaned_data['search']
            products = Product.objects.filter(Q(name__icontains=result) | Q(categories__category_name__icontains=result))
            return render(request, 'search_results.html', {"products": products})


class Login3View(FormView):
    template_name = 'homework_login_form.html'
    form_class = LoginForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return render(self.request, self.template_name, {'form': form, 'error_message': 'Błąd logowania.'})