from typing import Optional
from domain.entities.person import Person
from data.serializers.xml_serializer import XmlSerializer

class PersonService:
    """Service class handling business logic for Person operations."""
    
    def __init__(self, serializer: XmlSerializer = None):
        self.serializer = serializer or XmlSerializer()
    
    def save_person(self, person: Person, file_path: str) -> None:
        """Validates and serializes Person object to file."""
        try:
            person.validate()
            self.serializer.serialize(person, file_path)
        except Exception as e:
            raise ValueError(f"Error saving person: {e}")
    
    def load_person(self, file_path: str) -> Optional[Person]:
        """Deserializes and validates Person object from file."""
        try:
            person = self.serializer.deserialize(file_path, Person)
            person.validate()
            return person
        except Exception as e:
            print(f"Error loading person: {e}")
            return None