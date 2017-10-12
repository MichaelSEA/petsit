from django.db.models import Avg
from django.shortcuts import render
from sitters.models import Sitter


def build_view_list():
    sitters = Sitter.objects.all().order_by('-overall_sitter_rank')
    view_list = []
    for sitter in sitters:
        entry = dict()
        entry['name'] = sitter.name
        entry['image'] = sitter.image
        entry['rating_avg'] = round(sitter.stay_set.aggregate(Avg('rating'))['rating__avg'],2)
        view_list.append(entry)

    return view_list


def home_page(request):
    view_list = build_view_list()
    return render(request, 'home.html', {'sitters': view_list})

