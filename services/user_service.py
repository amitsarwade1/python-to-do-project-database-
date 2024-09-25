from storage.user_storage import UserStorage
from helper.input_helper import InputHelper
from helper.outer_helper import OuterHelper
from services.task_service import TaskService

class UserService:
    
    def __init__(self):
        self.userStorage = UserStorage()
        self.taskService = TaskService()
    
    # This function is creating new user.
    def createUser(self):
        fullName = InputHelper.getUserFullNameInputValue()
        username = InputHelper.getUserNameInputValue()
        password = InputHelper.getPasswordInputValue()
        
        if self.userStorage.loadUser(username):
            print('User already exists')
            return
    
        
        self.userStorage.saveUser(username,fullName,password)
   
    def userLogin(self):
        username = InputHelper.getUserNameInputValue()
        password = InputHelper.getPasswordInputValue()
        
        user = self.userStorage.loadUser(username)
        
        if user is None:
            print('User does not exist.')
            return
    
        userId = user[0]
        
        if user[2] == password:
            print(f'User {username} logged in successfully!')
            while True:
                OuterHelper.showUserLoggedMenu()
                choice = InputHelper.getChoiceInputValue()
                
                if choice == '1':
                    self.taskService.viewTasks(userId)
                elif choice == '2':
                    self.taskService.addTask(userId)
                elif choice == '3':
                    self.taskService.editTask(userId)
                elif choice == '4':
                    self.taskService.deleteTask(userId)
                elif choice == '5':
                    print('Logging out...')
                    break
                else:
                    print('Invalid choice, please try again.')
        else:
            print('Incorrect username or password.')