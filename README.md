# Inventory-System
# Inventory Management System (Flask + CLI + External API)

 Author
Metrine Mongare

---

Project Overview

This is a Flask-based Inventory Management System that allows users to manage inventory items through a REST API.  
It integrates with the OpenFoodFacts API to enrich product data and includes a CLI tool for interaction.

The system demonstrates:
- REST API development (CRUD operations)
- External API integration
- CLI-based interface
- Unit testing with pytest
- Git branching workflow

---

 Features

 REST API (Flask)
- GET /inventory → Fetch all items  
- GET /inventory/<id> → Fetch a single item  
- POST /inventory → Add new item  
- PATCH /inventory/<id> → Update item  
- DELETE /inventory/<id> → Remove item  

---
 Project Structure
Inventory-System/
│
├── app.py                # Flask REST API (CRUD routes)
├── cli.py               # Command Line Interface for users
├── external_api.py      # OpenFoodFacts API integration
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
│
└── tests/               # Unit testing suite
    ├── test_api.py      # Tests for Flask API endpoints
    ├── test_cli.py      # Tests for CLI functionality
    └── test_external.py # Tests for external API (mocked)

 External API Integration
Uses OpenFoodFacts API to fetch product details using barcode.

Fetched data includes:
- Product name
- Brand
- Ingredients
- Category

---
 CLI Interface
A command-line tool to interact with the API.

Features:
- View inventory items
- Add items using barcode lookup
- Update stock and price
- Delete items

Run CLI:
```bash
python cli.py