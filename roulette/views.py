from django.views.generic.base import TemplateView
from roulette.models import Roulette


class RouletteHome(TemplateView):
    template_name = "roulette_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roulettes = Roulette.objects.all()
        context.update({"roulettes": roulettes})
        return context
    