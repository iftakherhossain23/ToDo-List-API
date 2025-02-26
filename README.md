# To-Do List API 📝
This is a task management API that allows users to perform CRUD operations (Create, Read, Update, Delete) on their tasks. The backend is built in Python with Flask and stores data in IBM Cloudant. It is containerized with Docker and deployed on IBM Cloud Code Engine.

## How to Use
### 1. Download or clone this repository
Unzip the files if necessary. Ensure all files are in the same folder on your device.

### 2. Ensure Python is installed on your computer
Python can be installed through the [Python website](https://www.python.org/downloads/) or as an extension in your IDE.

### 3. Install required dependencies
In a command line, run `pip install -r requirements.txt`.

### 4. Run the local API
Run the code with `python app.py`. The API will be available at: [http://127.0.0.1:5000/](url).

## API Endpoints 
| Method | Endpoint | Function |
|--------|---------|-------------|
| **GET** | `/` | Check API status |
| **POST** | `/tasks` | Add new task |
| **GET** | `/tasks` | Retrieve all tasks |
| **PUT** | `/tasks/{task_id}` | Update a task |
| **DELETE** | `/tasks/{task_id}` | Delete a task |

## Future Improvements
Some planned improvements for this program include:
- Frontend UI with React
- Task filtering and search
