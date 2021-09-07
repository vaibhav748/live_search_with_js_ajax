from django.shortcuts import render
from django.http import JsonResponse
from .models import Game

# Create your views here.

def main_view(request):
	return render(request, 'games/main.html')

def game_detail_view(request, pk):
	pass

def search_results(request):
	if request.is_ajax():
		res = None
		game = request.POST.get('game')
		qs = Game.objects.filter(name__icontains=game)
		if len(qs) > 0 and len(game) > 0:
			data = []
			for pos in qs:
				item = {

					'pk': pos.pk,
					'name': pos.name,
					'stdio': pos.stdio,
					'image': str(pos.image.url)

				}
				data.append(item)
			res = data
		else:
			res = 'No Games Found.....'
		return JsonResponse({'data': res})
	return JsonResponse({})