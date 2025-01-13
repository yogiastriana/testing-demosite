from django.urls import path

from .views import permutation_dashboard_view, input_form_view, get_sector_industries_view, get_industries_view, get_p1_metric_data_view, run_p1_permutation_view, current_p1_result_view, output_view

urlpatterns = [
    path('', permutation_dashboard_view, name="permutation"),
    path('input/', input_form_view, name="p1-input"),
    path('p1-result/', output_view, name="p1-result"),  
    path('get-sector-industries/', get_sector_industries_view, name="get-sector-industries"),
    path('get-industries/', get_industries_view, name="get-industries"),
    path('fetch-p1-metric-data/', get_p1_metric_data_view, name="fetch-p1-metric-data"),
    path('run-p1-permutation/', run_p1_permutation_view, name="run-p1-permutation"),
    path('current-p1-result/', current_p1_result_view, name="current-p1-result"),
]