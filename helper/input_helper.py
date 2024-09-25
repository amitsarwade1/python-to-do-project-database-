class InputHelper:
    
    @staticmethod
    def getUserFullNameInputValue():
        return input('Enter your full name: ')
        
    @staticmethod
    def getUserNameInputValue():
        return input('Enter username: ')
    
    @staticmethod
    def getPasswordInputValue():
        return input('Enter password: ')
    
    @staticmethod
    def getChoiceInputValue():
        return input('choose an option: ')
    
    @staticmethod
    def getTaskNameInputValue():
        return input('Enter the task name: ')
    
    @staticmethod
    def getNewTaskNameInputValue():
        return input('Enter the new task name (leave blank to keep the same): ')
    
    @staticmethod
    def getNewStatusInputValue():
        return input('Enter the new status (in progress/completed): ').lower()
    
    @staticmethod
    def getTaskIdInputValue():
        return input('Enter the task ID: ')
    