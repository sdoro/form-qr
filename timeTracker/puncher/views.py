from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse

from puncher.models import clocking

# Create your views here.

def index(request):
    context = {'dummy': " - Let's go! - "}
    return render(request, 'puncher/index.html', context)

def punch(request, checkpoint_id):
    c = get_object_or_404(clocking, pk=checkpoint_id)
    print c.checkPoint_id
    return HttpResponseRedirect(reverse('puncher:accepted', args=(c.punch_id,)))

def accepted(request, checkpoint_id):
    context = {'dummy': " Checkpoint # "+str(checkpoint_id)+" - Well done! -"}
    return render(request, 'puncher/accepted.html', context)
