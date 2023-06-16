from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Notes

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        file_type = request.POST.get('file_type')
        title = request.POST.get('title')
        content = ''

        if file_type != 'text':
            file = request.FILES['file']
            content = file.read()
        else:
            content = request.POST.get('notes')

        Notes.objects.create(title=title, content=content, note_type=file_type)
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def note_detail(request, note_id):
    try:
        note = Notes.objects.get(id=note_id)
        print(note.id)
        data = [{'id': note.id, 'title': note.title, 'type': note.note_type, 'content': note.content}]
        return HttpResponse(data)
    except Notes.DoesNotExist:
        return HttpResponse({'error': 'Note not found'}, status=404)