from django.http import JsonResponse
from django.shortcuts import redirect

from category.models import Subcategory


def home(request):
    return redirect('admin/')


def get_subcategories(request):
    category_id = request.GET.get('category_id')

    if category_id:
        subcategories = Subcategory.objects.filter(category_id=category_id)
        subcategories_data = [
            {'id': sub.id, 'name': sub.name} for sub in subcategories
        ]
    else:
        subcategories_data = []

    return JsonResponse({'subcategories': subcategories_data})
