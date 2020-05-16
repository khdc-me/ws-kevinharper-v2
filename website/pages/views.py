from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ExperiencePageView(TemplateView):
    template_name = 'pages/experience.html'
