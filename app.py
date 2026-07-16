from flask import Flask, request, render_template, redirect, url_for, abort
import sqlite3

app = Flask(__name__)

VALID_STATUSES = {"read", "reading", "waiting"}


def get_connection():
    return sqlite3.connect("library.db")


@app.route("/")
def index():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, author, publisher, pages, status FROM books"
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
            "status": row[5] or "waiting",
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
    status = request.form.get("status", "waiting")
    if status not in VALID_STATUSES:
        status = "waiting"

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO books
        (title, author, publisher, pages, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, author, publisher, pages, status)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/edit/<int:book_id>")
def edit_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, author, publisher, pages, status FROM books WHERE id = ?",
        (book_id,)
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        abort(404)

    book = {
        "id": row[0],
        "title": row[1],
        "author": row[2],
        "publisher": row[3],
        "pages": row[4],
        "status": row[5] or "waiting",
    }

    return render_template("edit_book.html", book=book)


@app.route("/edit/<int:book_id>", methods=["POST"])
def edit_book_post(book_id):
    title = request.form["title"]
    author = request.form["author"]
    publisher = request.form["publisher"]
    pages = request.form["pages"]
    status = request.form.get("status", "waiting")
    if status not in VALID_STATUSES:
        status = "waiting"

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE books
        SET title = ?, author = ?, publisher = ?, pages = ?, status = ?
        WHERE id = ?
        """,
        (title, author, publisher, pages, status, book_id)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete_book_post(book_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)