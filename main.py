from services.menu_service import MenuService

#This is main function or entry point of application.
def main():
    menuService = MenuService()
    
    menuService.welcomeMenu()

main()