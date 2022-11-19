from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from create_todo.models import Category, Todo
from create_todo.permissions import IsOwnerOrReadOnly
from create_todo.serializers import CategorySerializer, TodoSerializer


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)
    ordering_fields = ("is_active",)
    filterset_fields = ("is_active",)
    ordering = ("is_active",)
    search_fields = ("name",)

    def get_queryset(self):
        return Category.objects.filter(owner__account_id=self.kwargs.get("account_id"))


class CategoryView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = "slug"

    def get_queryset(self):
        return Category.objects.filter(owner__account_id=self.kwargs.get("account_id"))


class TodoListView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    ordering_fields = ("status", "created_at")
    filterset_fields = ("status",)
    search_fields = ("todo_title", "todo_description")

    def get_queryset(self):
        return Todo.objects.filter(owner__account_id=self.kwargs.get("account_id"))


class CategoriesTodosList(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    ordering_fields = ("-created_at",)

    def get_queryset(self):
        return Todo.objects.filter(
            owner__account_id__iexact=self.kwargs.get("account_id"),
            category__slug__iexact=self.kwargs.get("slug")
        )


class TodoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = "slug"

    def get_queryset(self):
        return Todo.objects.filter(
            owner__account_id=self.kwargs.get("account_id")
        )
