from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import View

from category.models import Category, Subcategory


def home(request):
    return redirect('admin/')


def get_subcategories(request):
    catgory_id = request.GET.get('category_id')

    if catgory_id:
        subcategories = Subcategory.objects.filter(category_id=catgory_id)
        subcategories_data = [
            {'id': sub.id, 'name': sub.name} for sub in subcategories
        ]
    else:
        subcategories_data = []

    return JsonResponse({'subcategories': subcategories_data})
