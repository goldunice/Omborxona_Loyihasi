from django.shortcuts import render
from django.views import View


class StatsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "user": request.user.username.capitalize()
            }
            return render(request, 'stats.html', content)
