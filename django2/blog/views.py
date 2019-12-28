from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone


# Create your views here.
def blog_post_detail_page(request, slug):
    # try:
    print(request.method, request.user, request.path)
    mylist = [request.method, request.user, request.path]
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:
        raise Http404
    else:
        obj = queryset.first()
    # obj = get_object_or_404(BlogPost, slug=slug)
    # except ValueError:
    #     raise Http404
    template_name = 'blog_post_detail.html'
    context={"object": obj, "title": 'show blog posts','my': mylist}
    return render(request, template_name, context)


def blog_post_list_view(request):
    # now = timezone.now()
    #list out objects
    if request.user.is_authenticated:
        qs = BlogPost.objects.all() # qs-> a list of python objs
    else:
        qs = BlogPost.objects.published() # use a published def to use a query
    # qs = BlogPost.objects.filter(publish_data__lte=now) # one way to filter out published blog, <today
    template_name = 'blog/list.html'
    context = {'object_list': qs, "title": "list blog posts"}
    return render(request, template_name, context)

# @login_required(login_url='/admin')
@staff_member_required()
# @user_passes_test(lambda x: x.is_superuser)
def blog_post_create_view(request):
    #create object from a form
    # form = BlogPostForm(request.POST or None)
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # obj = BlogPost.objects.create(**form.cleaned_data)
        # obj = form.save(commit=False)
        obj = form.save()
        # obj.content = form.cleaned_data.get("content", "NA") + " manipulated"
        # obj.title = form.cleaned_data.get("title") + " fun"
        obj.user = request.user
        obj.save() # this is a way to manipulate the input data, if no manipulation, simply put form.save
        # form.save() # this is to use modelform
        # form = BlogPostForm()
        form = BlogPostModelForm()
    template_name = 'blog/create.html'
    context = {'form': form, "title": "create blog posts"}
    return render(request, template_name, context)


def blog_post_retrieve_view(request, slug):
    # this is the same as detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context={"object": obj, "title": "detail blog posts"}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    # grab the original obj and update
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/blog')
    template_name = 'blog/update.html'
    context={"form": form, "title": f"update {obj.title} blog posts","object": obj}
    return render(request, template_name, context)

@staff_member_required()
def blog_post_delete_view(request, slug):
    # grab the original obj and delete
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context={"object": obj, "title": "delete blog posts"}
    return render(request, template_name, context)

