from flask import Flask, request, jsonify
from dotenv import load_dotenv
from cloudant.client import Cloudant
import os

load_dotenv()

app = Flask(__name__)

CLOUDANT_USERNAME = os.getenv("CLOUDANT_USERNAME")
CLOUDANT_API_KEY = os.getenv("CLOUDANT_API_KEY")
CLOUDANT_URL = os.getenv("CLOUDANT_URL")
DATABASE_NAME = "todo_db"

client = Cloudant.iam(CLOUDANT_USERNAME, CLOUDANT_API_KEY, connect=True)
db = client.create_database(DATABASE_NAME, throw_on_exists=False)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running"})

# Add task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {"task": data["task"], "done": False}
    new_task = db.create_document(task)
    return jsonify({"id": new_task["_id"], "task": new_task["task"]})


# Get tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = [{"id": doc["_id"], "task": doc["task"], "done": doc["done"]} for doc in db]
    return jsonify(tasks)


# Update task
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    task = db[task_id]
    data = request.get_json()
    task["task"] = data.get("task", task["task"])
    task["done"] = data.get("done", task["done"])
    task.save()
    return jsonify({"message": "Task updated succesfully"})


# Delete task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    db[task_id].delete()
    return jsonify({"message": "Task deleted succesfully"})


if __name__ == '__main__':
    app.run(debug=True)
