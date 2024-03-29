from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Editors

# Creating views
class EditorChartView(TemplateView):
    template_name = 'editors/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editors.objects.all()
        print(context["qs"])
        return context