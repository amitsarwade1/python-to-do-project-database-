import uuid
import json

from datetime import datetime

from storage.user_storage import UserStorage
from helper.input_helper import InputHelper
from mysql.connector import Error

class TaskService:
    
    def __init__(self) -> None:
        self.userStorage = UserStorage()
    
    # This function is for view tasks of particular user.
    def viewTasks(self,userId):
        cursor = self.userStorage.connection.cursor()
        query = "SELECT id, task_name, task_status, task_created_date FROM tasks WHERE user_id = %s"
        cursor.execute(query, (userId,))
        tasks = cursor.fetchall()
        cursor.close()
        
        if tasks:
            print('Your tasks:')
            for task in tasks:
                print(f'ID: {task[0]}, Name: {task[1]}, Status: {task[2]}, Created: {task[3]}')
            return True
        else:
            return False   
        
    # This function is for add tasks of particular user.
    def addTask(self, userId):
        taskName = InputHelper.getTaskNameInputValue()
        taskCreatedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor = self.userStorage.connection.cursor()
        query = "INSERT INTO tasks (user_id, task_name, task_status, task_created_date) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (userId, taskName, 'new', taskCreatedDate))  # Removed the ID from the insert
            self.userStorage.connection.commit()
            print('Task Created.')
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


    # This function is for edit task of particular task id of user.
    def editTask(self, userId):
        tasksFound = self.viewTasks(userId)  
    
        if not tasksFound:
            print('No tasks found.')
            return
            
        taskId = InputHelper.getTaskIdInputValue()

        cursor = self.userStorage.connection.cursor()
        
        query = "SELECT task_name, task_status FROM tasks WHERE id = %s AND user_id = %s"
        cursor.execute(query, (taskId, userId))
        task = cursor.fetchone()
        
        if not task:
            print("Task not found or not owned by you.")
            cursor.close()
            return

        currentTaskName, currentStatus = task
        
        newTaskName = InputHelper.getNewTaskNameInputValue()
        newStatus = InputHelper.getNewStatusInputValue()

        if newTaskName.strip() == "":
            newTaskName = currentTaskName

        query = "UPDATE tasks SET task_name = %s, task_status = %s WHERE id = %s AND user_id = %s"
        try:
            cursor.execute(query, (newTaskName, newStatus, taskId, userId))
            if cursor.rowcount > 0:
                self.userStorage.connection.commit()
                print('Task updated successfully!')
            else:
                print('Task not found or not owned by you.')
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
    
     # This function is for delete tasks of particular user.
    def deleteTask(self,userId):
        tasksFound = self.viewTasks(userId)  
    
        if not tasksFound:
            print('No tasks found.')
            return
        
        taskId = InputHelper.getTaskIdInputValue()

        cursor = self.userStorage.connection.cursor()
        query = "DELETE FROM tasks WHERE id = %s AND user_id = %s"
        try:
            cursor.execute(query, (taskId, userId))
            self.userStorage.connection.commit()
            print('Task deleted successfully!')
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()