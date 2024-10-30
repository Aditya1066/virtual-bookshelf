# 📚 Virtual Bookshelf

Welcome to **Virtual Bookshelf** – your personal library manager! Track your favorite reads, rate them, and keep your literary life organized, all in one place.

---

## 🚀 Project Overview

This Flask app allows users to:
- **Add** new books to their virtual library.
- **View** all stored books with details like title, author, and rating.
- **Update** book ratings to keep track of your changing tastes.
- **Delete** books when it's time to let them go.

## 🏗️ Project Structure

```plaintext
📁 project_folder/
├── 📄 main.py                # Main Flask application
├── 📁 instance/
│   └── 📄 books_collection.db  # SQLite database
├── 📁 templates/
│   ├── 📄 add.html           # Add new books
│   ├── 📄 index.html         # Main library page
│   └── 📄 edit_rating.html   # Edit ratings for existing books
└── 📁 static/               # (Optional) Static assets like CSS or images
```

## 🔧 Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/virtual-bookshelf.git
   cd virtual-bookshelf
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have a `requirements.txt` file in your project with the necessary libraries. If not, you can create one with:
   ```bash
   pip freeze > requirements.txt
   ```
   Then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   Open Python in the terminal:
   ```python
   from main import db
   db.create_all()
   ```

5. **Run the App**:
   ```bash
   flask run
   ```
   Access it in your browser at `http://127.0.0.1:5000`.

## 🌟 Features

- **Easy Book Management**: Add, view, edit, and delete books.
- **Rating System**: Rate your books to track your reading preferences.
- **User-Friendly Interface**: Simple and clean design for smooth navigation.

## 🤝 Contributions

Feel free to open issues, suggest features, or submit pull requests. Let's make this bookshelf even better!

## 📜 License

MIT License – You're free to use, modify, and distribute this project, as long as you give credit. Happy coding!

---

Enjoy your journey with **Virtual Bookshelf**! 🥳
