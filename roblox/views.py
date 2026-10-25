from django.shortcuts import render
from .models import Game

def index(request):
    games = Game.objects.all() # Bütün oyunları bazadan çəkirik
    return render(request, 'roblox/index.html', {'games': games})