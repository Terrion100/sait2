
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Tag
from .forms import CommentForm
from django.db.models import Q

def index(request):
    q = request.GET.get('q', '').strip()
    recipes = Recipe.objects.all().order_by('-created_at')
    if q:
        # поиск по названию и по тегам (по имени тега)
        recipes = recipes.filter(
            Q(title__icontains=q) |
            Q(tags__name__icontains=q)
        ).distinct()
    tags = Tag.objects.all()
    categories = {r.category for r in Recipe.objects.all()}
    return render(request, 'index.html', {'recipes': recipes, 'q': q, 'tags': tags})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.recipe = recipe
        comment.save()
        return redirect('recipes:recipe_detail', pk=recipe.pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'form': form})
