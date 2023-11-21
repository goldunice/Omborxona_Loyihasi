from django.shortcuts import render
from django.views import View


class StatsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "user": request.user.username.capitalize(),
                "nom": request.user.nom.capitalize(),
                "rasm": request.user.rasm,
                "logo": request.user.logo
            }
            return render(request, 'stats.html', content)
