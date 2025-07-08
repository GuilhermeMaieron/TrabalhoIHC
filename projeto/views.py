from projeto import models
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.request.GET.get('qs')  # Get the tag from the URL
        ordenar = self.request.GET.get('ordenar', 'nome')

        lugares = models.Lugar.objects.all()
        if qs:
            lugares = lugares.filter(nome__icontains=qs)


        if ordenar == 'nome':
            lugares = lugares.order_by('nome')
        elif ordenar == 'abre':
            lugares = lugares.order_by('horario_abre')
        elif ordenar == 'fecha':
            lugares = lugares.order_by('horario_fecha')

        context['lugares'] = lugares
        context['count'] = lugares.count()
        context['ordenar'] = ordenar

        return context


# class AuthorDetailView(View):
#     def get(self, request, name):
#         author = get_object_or_404(models.Author, name=name)
#         quotes = models.Quote.objects.filter(author=author)
#         context = {
#             'author': author,
#             'quotes': quotes
#         }
#         return render(request, 'author_detail.html', context)