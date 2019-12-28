from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm


def home_page(request):
    home_title = 'This is home page'
    topic= 'Home Sweet Home'
    context = {"title": home_title, "topic": topic}
    if request.user.is_authenticated:
        mess = 'This is for authenticated user only'
        context = {"title": home_title, "topic": topic, "mess": mess,"my_list":[i for i in range(0,10,2)]}
    return render(request, "home.html", context)


def about_page(request):
    about_title = 'This is about page'
    topic = 'this is a little history about us'
    dic = {"title": about_title, "topic": topic }
    return render(request,"about.html", dic)


def contact_page_raw_form(request):
    print(request.POST)
    context = {"title": "contact_page_raw_form"}
    return render(request,"contact_raw_form.html", context)


def contact_page_django_form(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "contact_page_django_form", "form": form}
    return render(request, "contact_django_form.html", context)


def example(request):
    context = {"title": "Example", "topic": "This is an example"}
    template_name = "home.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))