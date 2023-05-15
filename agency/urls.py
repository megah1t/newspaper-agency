from django.urls import path, include

from agency.views import (
    index, TopicListView,
    NewspaperListView, RedactorListView,
    NewspaperDetailView, RedactorDetailView, TopicCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topics-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("news/", NewspaperListView.as_view(), name="news-list"),
    path("news/<int:pk>", NewspaperDetailView.as_view(), name="news-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactors-list"),
    path("redactors/<int:pk>", RedactorDetailView.as_view(), name="redactors-detail"),

]
app_name = "agency"
