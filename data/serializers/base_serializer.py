from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type

T = TypeVar('T')

class BaseSerializer(ABC, Generic[T]):
    """Abstract base class defining serialization interface."""
    
    @abstractmethod
    def serialize(self, obj: T, file_path: str) -> None:
        """Serializes object to file."""
        pass
    
    @abstractmethod
    def deserialize(self, file_path: str, obj_type: Type[T]) -> T:
        """Deserializes object from file."""
        pass