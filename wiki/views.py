from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from wiki.models import Page
from wiki.forms import PageForm

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

def newPage(request):
  """Makes a new wiki page """
  
  if request.method == 'POST':
    form = PageForm(request.POST)
    if form.is_valid():
      page = form.save(commit = False)
      page.author = request.user

      page.save()
      return redirect('wiki-list-page')
      
  form = PageForm()
  context ={'form' : form}
  return render(request, 'page_new.html', context)


