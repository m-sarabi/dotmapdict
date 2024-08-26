# dottydict

`dottydict` is a Python package that enhances the standard dictionary with dot notation access. This makes it easier to work with nested dictionaries by allowing you to access and modify their elements using attribute-style access.

## Features

- **Dot Notation Access**: Access dictionary keys as attributes.
- **Nested Dictionary Handling**: Automatically converts nested dictionaries into `DotDict` instances.
- **Merge Support**: Merge another dictionary into the existing `DotDict`.
- **Flexible Updates**: Update dictionary keys with dot notation.
- **Convert to Standard Dictionary**: Easily convert `DotDict` instances back to standard Python dictionaries.
- **Full Unit Test Coverage**: Comprehensive tests ensure the robustness of `dottydict`.

## Installation

Install `dottydict` via pip:

```bash
pip install dottydict
```

Usage
Here's a basic example of how to use dottydict:

```python
from dottydict import DotDict

# Initialize a DotDict instance with nested dictionaries
config = DotDict({"database": {"host": "localhost", "port": 5432}}, debug=True)

# Access values using dot notation
print(config.database.host)  # Output: localhost
print(config.debug)  # Output: True

# Update values using dot notation
config.database.username = "admin"
print(config.database.username)  # Output: admin

# Convert back to a standard dictionary
# Output: {'database': {'host': 'localhost', 'port': 5432, 'username': 'admin'}, 'debug': True}
print(config.to_dict())
print(type(config.to_dict()))  # Output: <class 'dict'>

# Merge another dictionary into the existing DotDict
config.merge({"database": {"password": "secret"}})
print(config.database.password)  # Output: secret

# Update the DotDict with another dictionary
config.update({"database": {"port": 5433, "ssl": False}})
print(config.database.port)  # Output: 5433
print(config.database.ssl)  # Output: False

# Delete a value using dot notation
del config.database.username
del config.database.port
print(config.database.username)  # Output: None
print(config.database)  # Output: {'host': 'localhost', 'password': 'secret', 'ssl': False}
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries or issues, please contact Mohammad Sarabi.
