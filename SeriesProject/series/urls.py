from django.urls import path
from . import views

app_name = "series"

urlpatterns = [
    path("add/series", views.add_series, name="Add series"),
    path("add/review", views.add_review, name="Add review"),
    path("add/suggestions", views.add_suggestions, name="Add suggestions"),
    path("list/series", views.list_series, name="list_series"),
    path("list/review", views.list_review, name="list_review"),
    path("list/suggestions", views.list_suggestions, name="list_suggestions"),
    path("update/series/<series_id>", views.update_series, name="update_series"),
    path("update/review/<review_id>", views.update_review, name="update_review"),
    path("update/suggestions/<suggestions_id>", views.update_suggestions, name="update_suggestions"),
    path("delete/series/<series_id>/", views.delete_series, name="delete_series"),
    path("delete/review/<review_id>/", views.delete_review, name="delete_review"),
    path("delete/suggestions/<suggestions_id>/", views.delete_suggestions, name="delete_suggestions"),

]
