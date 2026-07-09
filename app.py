from flask import Flask, request, render_template
import requests
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, author, publisher, pages FROM books"
    )
    rows = cursor.fetchall()
    connection.close()

    books = [
        {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "publisher": row[3],
            "pages": row[4],
        }
        for row in rows
    ]

    return render_template("index.html", books=books)

@app.route("/add_book")
def add_book():
    return render_template("add_book.html")

@app.route("/add_book", methods=["POST"])
def add_book_post():

    title = request.form["title"]
    author = request.form["author"]
    publisher = request.form["publisher"]
    pages = request.form["pages"]

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO books
        (title, author, publisher, pages)
        VALUES (?, ?, ?, ?)
        """,
        (title, author, publisher, pages)
    )

    connection.commit()
    connection.close()

    return "DONE!!!"



if __name__ == "__main__":
    app.run(debug=True)