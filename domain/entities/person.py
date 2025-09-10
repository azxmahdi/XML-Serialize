from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    """Represents a person entity with validation rules."""
    f_name: Optional[str] = None
    l_name: Optional[str] = None
    age: Optional[int] = None
    
    def __post_init__(self):
        """Validates field values after initialization."""
        self.validate()
    
    def validate(self):
        """Ensures all field values meet validation criteria."""
        if self.f_name is not None and not isinstance(self.f_name, str):
            raise ValueError("f_name must be a string")
        if self.l_name is not None and not isinstance(self.l_name, str):
            raise ValueError("l_name must be a string")
        if self.age is not None:
            # Convert string age to integer if needed
            if isinstance(self.age, str):
                try:
                    self.age = int(self.age)
                except ValueError:
                    raise ValueError("age must be a valid integer")
            
            if not isinstance(self.age, int) or self.age < 0:
                raise ValueError("age must be a non-negative integer")