from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from snippets.models import Snippet
from django.contrib.auth.decorators import login_required
from snippets.forms import SnippetForm


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)


def snippet_new(request):
    return HttpResponse('スニペットの登録')


def snippet_edit(request):
    return HttpResponse('スニペットの編集')


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})


@login_required
def snippet_edit(request, snippet_id):


def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
        else:
            form = SnippetForm()
            return render(request, "snippets/snippet_new.html", {'form': form})


# Create your views here.
