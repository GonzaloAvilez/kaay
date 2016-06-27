from haystack.forms import SearchForm


class PostSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()