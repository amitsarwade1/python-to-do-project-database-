from helper.outer_helper import OuterHelper
from helper.input_helper import InputHelper
from services.user_service import UserService

class MenuService:
    
    def __init__(self) -> None:
        self.userService = UserService()
    
    def welcomeMenu(self):
        print('Welcome to To-Do Application')
        while True:
            OuterHelper.showMainMenu()
            choice = InputHelper.getChoiceInputValue()
            
            if choice == '1':
                self.userService.userLogin()
            elif choice == '2':
                self.userService.createUser()
            elif choice == '3':
                print('Exiting Application...\n')
                break
            else:
                print('Invalid choice, please try again.')