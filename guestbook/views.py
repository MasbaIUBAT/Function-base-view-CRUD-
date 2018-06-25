from django.shortcuts import render, redirect

from .models import Comment 
from .forms import CommentForm

def index(request):
    comments = Comment.objects.order_by('-date_added')

    context = {'comments' : comments}

    return render(request, 'guestbook/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')

    else:
        form = CommentForm()

    context = {'form' : form}
    return render(request, 'guestbook/sign.html', context)

def detail(request, id):
    comment = Comment.objects.get(id=id)
    context = {
        'comment': comment,
    }
    template = 'guestbook/detail.html'
    return render(request, template, context)

def edit(request, id):
    obj = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('detail', id=obj.id)
    
    form = CommentForm(instance=obj)
    context = {
        'form': form,
    }
    template = 'guestbook/edit.html'
    return render(request, template, context)
