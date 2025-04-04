API Endpoints
Get All Tasks
URL: /tasks/
Method: GET
Description: Fetches all tasks from the backend.
Usage in Code: 
axios.get('https://backend-r4nn.onrender.com/api/tasks/')

Create a New Task
URL: /tasks/
Method: POST
Description: Creates a new task.
Request Body Example:
{
  "text": "New Task",
  "completed": false
}
Usage in Code:
axios.post('https://backend-r4nn.onrender.com/api/tasks/', newTask)

Update a Task
URL: /tasks/<id>/
Method: PUT
Description: Updates an existing task (e.g., toggling completion or editing the task text).
Request Body Example:
{
  "text": "Updated Task",
  "completed": true
}
Usage in Code:
axios.put(`https://backend-r4nn.onrender.com/api/tasks/${id}/`, updatedTask)

Delete a Task
URL: /tasks/<id>/
Method: DELETE
Description: Deletes a task by its ID.
Usage in Code:
axios.delete(`https://backend-r4nn.onrender.com/api/tasks/${id}/`)
