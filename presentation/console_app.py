from application.services.person_service import PersonService
from domain.entities.person import Person

class ConsoleApp:
    """Console application demonstrating XML serialization functionality."""
    
    def __init__(self, person_service: PersonService):
        self.person_service = person_service
    
    def run(self):
        """Main application entry point."""
        # Create sample person object
        person = Person(f_name="Mohammad Mahdi", l_name="Abbasi", age=17)
        
        # Serialize to XML file
        self.person_service.save_person(person, "xmlPerson.xml")
        print("Person saved to xmlPerson.xml")
        
        # Deserialize from XML file
        loaded_person = self.person_service.load_person("xmlPerson.xml")
        
        if loaded_person:
            print("Person loaded successfully:")
            print(f"First Name: {loaded_person.f_name}")
            print(f"Last Name: {loaded_person.l_name}")
            print(f"Age: {loaded_person.age}")
        else:
            print("Failed to load person data.")
        
        # Keep console open until user input
        input("Press Enter to exit...")