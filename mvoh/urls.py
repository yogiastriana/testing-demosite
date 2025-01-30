from django.urls import path

from .views import permutation_dashboard_view, input_form_view, get_sector_industries_view, get_industries_view, get_mvoh_metric_data_view, run_mvoh_model_view, current_mvoh_result_view, output_view

urlpatterns = [
    path('', permutation_dashboard_view, name="permutation-mvoh"),
    path('input/', input_form_view, name="mvoh"),
    path('p1-result/', output_view, name="p1-result"),  
    path('get-sector-industries/', get_sector_industries_view, name="get-sector-industries"),
    path('get-industries/', get_industries_view, name="get-industries"),
    path('fetch-mvoh-metric-data/', get_mvoh_metric_data_view, name="fetch-mvoh-metric-data"),
    path('run-mvoh/', run_mvoh_model_view, name="run-mvoh"),
    path('current-mvoh-result/', current_mvoh_result_view, name="current-mvoh-result"),
]