from django.shortcuts import render

from image_carousel.models import ImageCarousel
import website.views


class IndexView(website.views.TemplateView):
    template_name = 'about/about.html'

    def get(self, request, **kwargs):
        models = self.fetch_view_models()

        context = {'models': models}
        context.update(self.get_context_data())

        return render(request, self.template_name, context)

    def fetch_view_models(self):
        models = {}
        models['image_carousel_image_models'] = self.fetch_image_carousel_image_models()
        return models

    def fetch_image_carousel_image_models(self):
        image_carousel_models = self.fetch_image_carousel_models()
        return image_carousel_models.images.all()

    def fetch_image_carousel_models(self):
        try:
            image_carousels = ImageCarousel.objects.get(view='about')
        except ImageCarousel.DoesNotExist as error:
            image_carousels = ImageCarousel.objects.none()
        return image_carousels
