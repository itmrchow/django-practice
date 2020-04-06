from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .form import PartForm

from .models import Part
from django.forms.models import modelform_factory

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'parts/index.html'
    context_obj_name = "part_list"

    def get_queryset(self):
        return Part.objects.all()


class DetailView(generic.DetailView):
    "編輯"
    model = Part
    template_name = 'parts/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'parts:update'
        return context


class CreateView(generic.CreateView):
    "新增"
    model = Part
    fields = ['part_txt', 'part_name']
    template_name = 'parts/edit.html'

    def get_context_data(self, **kwargs):
        context = {
            "action": "parts:insert",
            "part": Part
        }

        return context


def insert(request):

    part = Part(part_name=request.POST['part_name'],
                part_txt=request.POST['part_txt'])
    part.save()

    return HttpResponsePermanentRedirect(reverse('parts:index'))


def delete(request, pk):
    part = Part.objects.get(pk=pk)
    part.delete()

    return HttpResponsePermanentRedirect(reverse('parts:index'))


def update(request):
    pk = request.POST['part_pk']
    part = Part.objects.get(pk=pk)
    partForm = modelform_factory(Part, fields=("part_txt", "part_name"))

    part.part_name = request.POST['part_name']
    part.part_txt = request.POST['part_txt']

    part.save()

    return HttpResponsePermanentRedirect(reverse('parts:index'))
