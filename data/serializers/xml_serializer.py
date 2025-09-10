import xml.etree.ElementTree as ET
from typing import Type
from data.serializers.base_serializer import BaseSerializer

class XmlSerializer(BaseSerializer):
    """XML implementation of the BaseSerializer interface."""
    
    def serialize(self, obj, file_path: str) -> None:
        """Serializes object to XML file."""
        root = ET.Element(obj.__class__.__name__)
        
        # Create XML elements from object attributes
        for attr, value in obj.__dict__.items():
            if value is not None:
                element = ET.SubElement(root, attr)
                element.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
    
    def deserialize(self, file_path: str, obj_type: Type) -> object:
        """Deserializes object from XML file."""
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Validate root element matches expected type
            if root.tag != obj_type.__name__:
                raise ValueError(f"XML root element '{root.tag}' does not match expected type '{obj_type.__name__}'")
            
            kwargs = {}
            for element in root:
                if element.text:
                    # Convert values to appropriate types based on class annotations
                    field_type = obj_type.__annotations__.get(element.tag, str)
                    
                    try:
                        if field_type == int:
                            kwargs[element.tag] = int(element.text)
                        else:
                            kwargs[element.tag] = element.text
                    except (ValueError, TypeError):
                        # Fallback to original value if conversion fails
                        kwargs[element.tag] = element.text
            
            return obj_type(**kwargs)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found")
        except ET.ParseError:
            raise ValueError(f"Invalid XML format in file '{file_path}'")