from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.views import generic
from .forms import ContactForm

# Create your views here

class IndexView(generic.TemplateView):
    template_name = "main/base.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonials = Testimonial.objects.filter(is_active = True)
        blogs = Blog.objects.filter(is_active = True)
        portfolio = Portfolio.objects.filter(is_active=True)
        form = ContactForm
        context["testimonials"] = testimonials
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        context['form'] = form
        return context
    

    

# class ContactView(generic.FormView):
#     template_name = "main/contact.html"
#     form_class = ContactForm
#     success_url = "/"

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, "Thank you. We will be in touch soon")
#         return super().form_valid(form)
class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"


