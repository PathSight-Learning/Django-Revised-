from django.shortcuts import render, get_object_or_404
from .models import Field, Subfield

def career_path(request):
    fields = Field.objects.prefetch_related('subfields').all()
    return render(request, 'careerpath/career_path.html', {'fields': fields})

def subfield_detail(request, subfield_id):
    subfield = get_object_or_404(Subfield, id=subfield_id)
    return render(request, 'careerpath/subfield_detail.html', {'subfield': subfield})