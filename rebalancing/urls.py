from django.urls import path

from .views import rebalancing_dashboard, run_rebalancing_f1_view, current_f1_result_view

urlpatterns = [
    path('', rebalancing_dashboard, name="rebalancing"),
    # path('m4-result/', output_view, name="m4-result"),
    # path('run-m4-model/', run_m4_model_view, name="run-m4-model"),
    path('current-f1-result/', current_f1_result_view, name="current-f1-result"),
    # path('fetch-m4-error/', fetch_m4_error_view, name='fetch-m4-error'),
    path('run-rebalancing-f1/', run_rebalancing_f1_view, name='run-rebalancing-f1'),
]