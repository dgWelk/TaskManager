# 📋 Task Manager – Command Line Task Manager

A simple task manager that works in the command line. Allows you to add, delete, view tasks, and automatically save them to a CSV file with timestamps.

## 🚀 Features

- ✅ Add a new task (current date and time are added automatically)
- ❌ Delete a task by its number in the list
- 📋 View all current tasks with their creation date and time
- 💾 Save tasks to a CSV file on exit
- 📂 Load tasks from a CSV file on startup

## 🛠️ Technologies

- Python 3.13+
- Built-in modules: `csv`, `datetime`
- Modular class-based architecture

## 📁 Project Structure
- TaskManage/
- ├── data/
- │ ├── classes/
- │ │ ├── TaskBook.py # Task logic
- │ │ └── workCSV.py # CSV read/write
- │ ├── scripts/
- │ │ ├── bridgeCSVBOOK.py # Data converter
- │ │ └── workTime.py # Get current time
- │ └── saves/
- │ └── tasks.csv # Task storage file (auto‑created)
- ├── main.py # Entry point
- └── README.md


## 🔧 Installation & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
2. Make sure Python 3.13+ is installed

3. Run the application
On Windows, to run with a double click, create a start.bat file with

