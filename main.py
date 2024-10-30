from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books_collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# all_books = []


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/',methods=['GET','POST'])
def home():
    with app.app_context():
        books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
        print(books)
        for book in books:
            print(book.title, book.author, book.rating)
    return render_template('index.html', all_books=books)

@app.route("/delete/<int:book_id>",methods=['GET','POST'])
def delete(book_id):
    with app.app_context():
        book = Book.query.filter_by(id=book_id).first()
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(title=request.form['book_name'], author=request.form['book_author'], rating=request.form['book_rating'])
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit_rating/<int:book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):
    if request.method == 'GET':
        with app.app_context():
            this_book = Book.query.filter_by(id=book_id).first()
            print(this_book.rating)
        return render_template('edit_rating.html', book=this_book)
    if request.method == 'POST':
        new_rating = request.form['new_rating']
        with app.app_context():
            this_book = Book.query.filter_by(id=book_id).first()
            setattr(this_book, 'rating', float(new_rating))
            db.session.commit()
            print(this_book.rating)
        return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)

