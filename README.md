# XML Serialize Project

A Python implementation for XML serialization and deserialization of Person objects following SOLID principles and layered architecture.

## Project Structure

```
.
├── domain/
│   └── entities/
│       └── person.py
├── data/
│   └── serializers/
│       ├── base_serializer.py
│       └── xml_serializer.py
├── application/
│   └── services/
│       └── person_service.py
├── presentation/
│   └── console_app.py
├── main.py
├── .gitignore
└── LICENSE
```

## Core Components

### Domain Layer
- **Person Class**: Represents a person with first name, last name, and age properties
- Includes data validation for all properties

### Data Layer
- **BaseSerializer**: Abstract base class defining serialization interface
- **XmlSerializer**: Implementation for XML serialization/deserialization using Python's xml.etree.ElementTree

### Application Layer
- **PersonService**: Handles business logic for person operations including validation

### Presentation Layer
- **ConsoleApp**: Console interface demonstrating the serialization functionality

## Usage

### Running the Application

Execute the main script to run the complete demonstration:

```bash
python main.py
```

The application will:
1. Create a Person object
2. Serialize it to an XML file (xmlPerson.xml)
3. Deserialize the XML file back to a Person object
4. Display the Person information

### Reading Data Only from File

To modify the application to only read data from an existing XML file without creating a new one, comment out the following sections in `presentation/console_app.py`:

```python
# Comment these lines in the run() method:

# Create a Person object
# person = Person(f_name="Mohammad Mahdi", l_name="Abbasi", age=17)

# Serialize to file
# self.person_service.save_person(person, "xmlPerson.xml")
# print("Person saved to xmlPerson.xml")
```

This modification will skip the creation and serialization steps, proceeding directly to deserialize from an existing XML file.

## Technical Details

- Built entirely with Python Standard Library modules
- No external dependencies required
- Implements proper type hinting throughout
- Comprehensive error handling and validation
- Follows SOLID design principles

## License

MIT License

Copyright (c) 2025 azxmahdi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.