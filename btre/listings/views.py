from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.shortcuts import get_object_or_404
from btre.choices import bedroom_choices,state_choices,price_choices
# Create your views here.

class ListingIndexView(ListView):
    model = Listing
    template_name = 'listings/listings.html'
    context_object_name ='listings'
    paginate_by = 6
    queryset = Listing.objects.order_by('-list_date').filter(is_publish=True)


class ListingDetailView(TemplateView):
    model = Listing
    template_name = 'listings/listing_detail.html'
    context_object_name = 'listing_detail'

    

    def get_context_data(self,*args, **kwargs):

        context = super(ListingDetailView,self).get_context_data(*args,**kwargs)
        print('is getting valled')
        #will check to see if the pk exists or not.If it doesn't exist then it will return 404 page.
        context['listing_detail'] = get_object_or_404(Listing,pk=self.kwargs.get('pk'))
        return context

class Search(TemplateView):
    template_name = 'listings/search.html'
    model = Listing

    def get_context_data(self,*args,**kwargs):
        context = super(Search,self).get_context_data(*args,**kwargs)
        queryset_list = Listing.objects.order_by('-list_date')

        #keywords
        if 'keywords' in self.request.GET:
            keywords = self.request.GET['keywords']

            if keywords:
                queryset_list = queryset_list.filter(description__icontains=keywords)


        #city
        if 'city' in self.request.GET:
            city = self.request.GET['city']

            if city:
                queryset_list = queryset_list.filter(city__iexact=city)


        #state
        if 'state' in self.request.GET:
            state = self.request.GET['state']

            if state:
                queryset_list = queryset_list.filter(state__iexact=state)


        #bedrooms
        if 'bedrooms' in self.request.GET:
            bedrooms = self.request.GET['bedrooms']

            if bedrooms:
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


        #price
        if 'price' in self.request.GET:
            price = self.request.GET['price']

            if price:
                queryset_list = queryset_list.filter(price__lte=price)                        


        context['state_choices'] = state_choices
        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices
        context['listings'] = queryset_list
        context['values'] = self.request.GET

        return context
