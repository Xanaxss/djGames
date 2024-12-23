from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


def index(request):
    top_games = ModelGame.objects.annotate(
        favorite_count=Count('modelfavorite')).order_by('-favorite_count')[:4]

    favorite = ModelFavorite.objects.filter(user=request.user)
    favorite_game_ids = set(fav.game.id for fav in favorite)

    context = {
        'top_games': top_games,
        'favorite': favorite_game_ids,
    }

    return render(request, 'index.html', context=context)


def detail(request, slug):
    game = ModelGame.objects.get(slug=slug)

    return render(request, 'detail.html', context={'game': game})


def detail_company(request, slug):
    company = ModelCompany.objects.get(slug=slug)
    return render(request, 'detail-comp.html', context={'company': company})


def all_games(request):
    games = ModelGame.objects.all()
    favorite = ModelFavorite.objects.filter(user=request.user)
    favorite_game_ids = set(fav.game.id for fav in favorite)

    context = {
        'games': games,
        'favorite': favorite_game_ids
    }

    return render(request, 'all-games.html', context=context)


def all_company(request):
    company = ModelCompany.objects.all()

    context = {
        'company': company
    }

    return render(request, 'all-company.html', context=context)



################################################ UTILS ###############################################

def subscribe(request):
    game = ModelGame.objects.get(id=request.POST.get('game'))

    if ModelFavorite.objects.filter(user=request.user, game=game).exists():
        ModelFavorite.objects.filter(user=request.user, game=game).delete()
    else:
        ModelFavorite(user=request.user, game=game).save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
