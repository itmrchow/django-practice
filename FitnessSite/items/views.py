from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from parts.models import Part
from .models import ActionItem

# Create your views here.


class IndexView(generic.ListView):
    template_name = "items/index.html"
    context_obj_name = "part_list"
    model = Part

    def get_queryset(self):
        return Part.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        part_pk = self.kwargs.get('pk')

        if part_pk:
            part = Part.objects.get(pk=part_pk)
            item_list = part.actionitem_set.all()
            context['item_list'] = item_list

        return context


class CreateView(generic.CreateView):
    "新增"
    model = ActionItem
    template_name = 'items/edit.html'

    def get_context_data(self, **kwargs):
        part_list = Part.objects.all()

        context = {
            "action": "items:insert",
            "item": ActionItem,
            "part_list": part_list
        }

        return context


class DetailView(generic.DetailView):
    model = ActionItem
    template_name = "items/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        part_list = Part.objects.all()

        context['action'] = "items:update"
        context['part_list'] = part_list

        return context


def insert(request):
    part_pk = request.POST['part']
    # part = Part.objects.get(pk=part_pk)
    # item = ActionItem(part=part, item_name=request.POST['item_name'])
    # item.save()

    return HttpResponseRedirect(reverse('items:index_Part', args=(part_pk,)))


def update(request):
    return HttpResponseRedirect(reverse('items:index_Part', args=(part_pk,)))
