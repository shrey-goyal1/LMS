Library Management System Readme

Overview:
This library management system is a Python-based program designed to automate various tasks involved in managing a library, such as user registration, book issuance, returns, account deletion, and more. The system is built using Python and MySQL for database management.

Features:
1. User Registration: New users can register themselves by providing their details like name, date of birth, and password.
2. User Login: Registered users can log in using their credentials.
3. Update User Data: Users can update their information like name, date of birth, and password.
4. Book Issuance: Users can issue books from the library based on their preferred genre.
5. Book Returns: Users can return the issued books.
6. Account Deletion: Users can delete their accounts, provided they have returned all issued books.
7. Account Details: Users can view their account details, including issued books and return dates.
8. Logout: Users can safely log out of their accounts.

Installation:
1. Clone the Repository: Clone the repository to your local machine using the following command:
   
   """git clone <repository-url>"""
2. Database Setup: Set up a MySQL database and import the provided schema to create the necessary tables.
3. Install Dependencies: Install the required Python dependencies using pip:

   """pip install -r requirements.txt"""
  
4. Configuration: Modify the database connection details in the code to match your MySQL configuration.

Usage:
1. Start the Program: Run the main Python file to start the library management system.
   """python main.py"""
2. Follow On-Screen Instructions: The program will prompt you to choose actions like login, register, update, issue book, return book, etc.
3. Interact with the System: Based on your choice, interact with the system by providing the required inputs as prompted.
4. Logout and Exit: After completing your tasks, log out of the system when done. You can choose to exit the program or continue performing more actions.

Contributing:
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

License:
This project is licensed under the [MIT License](LICENSE).

Authors:
- SHREY GOYAL (shreygoyal73@gmail.com)

Disclaimer:
This project is developed for educational purposes only. It is not intended for use in real-world applications without proper testing and validation.
