from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Store, Staff
from django.shortcuts import render, get_object_or_404


# class IndexView(LoginRequiredMixin, TemplateView):
#     template_name = "app/index.html"
#     login_url = '/accounts/login/'

class StoreView(View):
    def get(self, request, *args, **kwargs):
        store_data = Store.objects.all()

        return render(request, 'app/store.html', {
            'store_data': store_data,
        })

class StaffView(View):
    def get(self, request, *args, **kwargs):
        store_data = get_object_or_404(Store, id=self.kwargs['pk'])
        satff_data = Staff.objects.filter(store=store_data).select_related('user')