**README.md**

# tabqa: Natural Language to SQL Query Converter

## Overview
This Python library enables the conversion of natural language queries into SQL queries. It simplifies the process of querying databases by allowing users to express their queries in everyday language.

## Installation
You can install the package via pip:

```bash
pip install tabqa
```

## Example Usage
```python
from tabqa import sql_model, generate_schema

# Define the natural language question
question = "Count Number products"

# Path to the SQL file containing the database schema
file_path = "schema.sql"

# Initialize the SQL model
model = sql_model()

# Generate the SQL schema from the natural language question
result = generate_schema(question, file_path, model)

# Print the generated SQL query
print(result)
```

## How to Use
1. Import the necessary functions from `tabqa`.
2. Define your natural language question.
3. Provide the path to the SQL file containing your database schema.
4. Initialize the SQL model.
5. Use `generate_schema()` function to convert the natural language question into an SQL query.
6. Print or use the generated SQL query as needed.

## Contribution
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
