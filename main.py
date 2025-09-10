from application.services.person_service import PersonService
from presentation.console_app import ConsoleApp

def main():
    """Application entry point."""
    # Initialize services
    person_service = PersonService()
    
    # Initialize and run console application
    app = ConsoleApp(person_service)
    app.run()

if __name__ == "__main__":
    main()