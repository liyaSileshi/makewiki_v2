from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from wiki.models import Page
from wiki.forms import PageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page
    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page
    def get(self, request, slug):
      """ Returns a specific wiki page by slug. """
      page = self.get_queryset().get(slug__iexact=slug)
      return render(request, 'page.html', {
        'page': page
      })


# def newPage(request):
#   """Makes a new wiki page """
#   if request.method == 'POST':
#     form = PageForm(request.POST)
#     if form.is_valid():
#       page = form.save(commit = False)
#       page.author = request.user

#       page.save()
#       return redirect('wiki-details-page')
      
#   form = PageForm()
#   context ={'form' : form}
#   return render(request, 'page_new.html', context)


class PageCreateView(CreateView):
  def get(self, request, *args, **kwargs):
      context = {'form': PageForm()}
      return render(request, 'page_new.html', context)

  def post(self, request, *args, **kwargs):
      form = PageForm(request.POST)
      if form.is_valid():
          page = form.save()
          return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[page.slug]))
      return render(request, 'page_new.html', {'form': form})
