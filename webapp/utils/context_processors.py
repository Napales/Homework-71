from webapp.forms import SearchForm


def get_search_form(request):
    return {'search_form': SearchForm(request.GET)}