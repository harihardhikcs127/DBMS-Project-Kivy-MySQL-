# Wholesale Database Management System

## Kivy GUI with MySQL Backend

This project integrates the Kivy framework for a responsive graphical user interface (GUI) with MySQL as the backend database, using the Python MySQL Connector for seamless connectivity.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Introduction
This repository demonstrates the use of Kivy for creating an interactive GUI that allows users to perform various database operations such as Create, Read, Update, and Delete (CRUD) on a MySQL database. The integration ensures real-time updates, making it ideal for applications that require up-to-date information.

## Features
- **Kivy-based GUI**: A sleek and responsive user interface.
- **MySQL Integration**: Reliable backend database operations using Python MySQL Connector.
- **CRUD Operations**: Add, update, delete, and retrieve data from MySQL.
- **Real-time Updates**: Immediate reflection of database changes in the GUI.
- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux.

## Requirements
- Python 3.x
- Kivy
- MySQL Server
- Python MySQL Connector

## Installation
1. **Clone the repository**:
    ```sh
    https://github.com/harihardhikcs127/DBMS-Project-Kivy-MySQL-.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd Wholesale_Management.py
    ```
3. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration
1. **Set up your MySQL database**:
    - Create a database and the necessary tables for your project.
    - Update the connection settings in the configuration file (e.g., `Wholesale_Management.py` or directly in the script) to match your MySQL setup.

    Example configuration in `Wholesale_Management.py`:
    ```python
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'yourusername'
    MYSQL_PASSWORD = 'yourpassword'
    MYSQL_DB = 'yourdatabase'
    ```

## Usage
1. **Run the main application script**:
    ```sh
    python Wholesale_Management.py
    ```
2. **Interact with the GUI**:
    - Use the provided interface to add, update, delete, and retrieve data from the MySQL database.
    - Observe real-time updates in the GUI reflecting database changes.
