from django.urls import path
from create_todo.views import (
    CategoryListView,
    CategoryView,
    TodoListView,
    TodoView,
    CategoriesTodosList,
)

urlpatterns = [
    path("<str:account_id>/categories/", CategoryListView.as_view(), name="categories-list"),
    path("<str:account_id>/categories/<slug:slug>/", CategoryView.as_view(), name="category"),
    path("<str:account_id>/todos/", TodoListView.as_view(), name="todos-list"),
    path("<str:account_id>/todos/<slug:slug>/", TodoView.as_view(), name="todo"),
    path("<str:account_id>/categories/<slug:slug>/todos/", CategoriesTodosList.as_view(), name="categories-todos-list"),
]