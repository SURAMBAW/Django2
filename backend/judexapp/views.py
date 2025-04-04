from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer

# View for listing and creating tasks
class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for retrieving, updating, and deleting a specific task
class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer