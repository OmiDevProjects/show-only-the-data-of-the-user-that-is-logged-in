from django.shortcuts import render
from profiles.models import Profile

def index_view(request):

    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        profile = None
        print('Exception : ', e)

    context = {
        'profile': profile,
    }
    return render(request, 'home/index.html', context)