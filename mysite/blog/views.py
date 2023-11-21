from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    Paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})

def post_detail(request,id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish_year=year,
                             publish_month=month,
                             publish_day = day)
    # try:
    #     post= Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    return render(request,
                  'blog/post/detail.html',
                  {'post':post})
