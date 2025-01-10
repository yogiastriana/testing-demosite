from django.urls import path

from .views import runs_view, save_run_view, delete_run, session_mvoh_run, save_session_run_view, run_output_view, get_single_saved_run, calculate_ticker_correlation_view, calculate_m4_ticker_correlation_view, run_detail_view, m4_run_detail_view

urlpatterns = [
    path('', runs_view, name="runs_mvoh"),
    path('save-run/', save_run_view, name="save-run"),
    path('delete-run/', delete_run, name='delete-run'),
    path('get-run-data/', get_single_saved_run, name="get-run-data"),
    path('run-detail/<int:run_id>/', run_detail_view, name="run-detail"),
    path('m4-run-detail/<int:run_id>/', m4_run_detail_view, name="m4-run-detail"),
    path('session-mvoh-run/<int:id>/', session_mvoh_run, name='session-mvoh-run'),
    path('save-session-mvoh-run/', save_session_run_view, name='save-session-mvoh-run'),
    path('mvoh-run-output/<int:id>/', run_output_view, name='mvoh-run-output'),
    path('calculate-ticker-correlation/', calculate_ticker_correlation_view, name='calculate-ticker-correlation'),
    path('calculate-m4-ticker-correlation/', calculate_m4_ticker_correlation_view, name='calculate-m4-ticker-correlation')
]

