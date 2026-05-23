from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added.")
            return redirect("todos:index")
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    return render(
        request,
        "todos/index.html",
        {"form": form, "todos": todos},
    )


@require_POST
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save(update_fields=["completed"])
    messages.info(request, "Task updated.")
    return redirect("todos:index")


@require_POST
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.warning(request, "Task removed.")
    return redirect("todos:index")
