from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


def index(request):
    fil = '-id'
    history = estate.objects.order_by(fil)

    data = {'history': history, }

    return render(request, 'main/index.html', data)


def index_test(request):
    history = estate.objects.order_by('-id')
    data = {'estate': history, }
    return render(request, 'main/mainpage.html', data)


class MainPage(ListView):
    model = estate
    context_object_name = 'estate'
    paginate_by = 12
    queryset = estate.objects.all()
    # queryset = estate.objects.all().filter(count_room=1) | estate.objects.all().filter(count_room=2)
    # template_name = 'main/mainpage.html'
    # def get_ordering(self):
    #     ordering = self.request.GET.get('orderby')
    #     print(ordering)
    #     print(self.request.GET.get('count_room'))
    #     return ordering
    # def get_queryset(self):
    #     queryset = estate.objects.filter(count_room=self.request.GET.getlist('count_room'))
    #     return queryset


class FilterEstateView(ListView):
    context_object_name = 'estate'

    def get_queryset(self):
        # Не выбрано ничего
        if ((len(self.request.GET.getlist('region')) == 0) and (len(self.request.GET.getlist('count_room')) == 0)):
            queryset = estate.objects.all()
            ordering = self.get_ordering()
            if ordering:
                if isinstance(ordering, str):
                    ordering = (ordering,)
                queryset = queryset.order_by(*ordering)
            return queryset
        # Выбран только колво комнат
        elif ((len(self.request.GET.getlist('region')) == 0) and (len(self.request.GET.getlist('count_room')) != 0)):
            queryset = estate.objects.filter(
                Q(count_room__in=self.request.GET.getlist('count_room'))
            )
            ordering = self.get_ordering()
            if ordering:
                if isinstance(ordering, str):
                    ordering = (ordering,)
                queryset = queryset.order_by(*ordering)
            return queryset
        #Выбран только регион
        elif ((len(self.request.GET.getlist('region')) != 0) and (len(self.request.GET.getlist('count_room')) == 0)):
            queryset = estate.objects.filter(
                Q(count_room__in=self.request.GET.getlist('region'))
            )
            ordering = self.get_ordering()
            if ordering:
                if isinstance(ordering, str):
                    ordering = (ordering,)
                queryset = queryset.order_by(*ordering)
            return queryset
        #Выбраны все гаочки
        else:
            queryset = estate.objects.filter(
                Q(count_room__in=self.request.GET.getlist('count_room')) &
                Q(region__in=self.request.GET.getlist('region'))
            )
            ordering = self.get_ordering()
            if ordering:
                if isinstance(ordering, str):
                    ordering = (ordering,)
                queryset = queryset.order_by(*ordering)
            return queryset

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        # print(f'сортировка: {ordering}')
        return ordering


class MovieEstateView(DetailView):
    model = estate
    slug_field = "url"


class IndexView(ListView):
    model = estate
    context_object_name = 'estate'
    paginate_by = 12
    queryset = estate.objects.all()
    template_name = 'main/test.html'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        print(f'сортировка: {ordering}')
        return ordering
