from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine
import urllib.parse

application = Flask(__name__)

database_name = "API"
DB_URI = "mongodb+srv://<username>:<password>@atlas.wncld.mongodb.net/API?retryWrites=true&w=majority"
application.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(application)

class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()

    def to_json(self):
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author":self.author
        }

@application.route('/api/db_populate', methods=['POST'])
def db_populate():
    book1 = Book(book_id=1, name="Game of Thrones", author="George RR Martin")
    book2 = Book(book_id=2, name="Lord of the Rings", author="Kaatrey")
    book1.save()
    book2.save()
    return make_response("", 201)

@application.route('/api/books', methods=['GET','POST'])
def api_books():
    if request.method == "GET":
        books = []
        for book in Book.objects:
            books.append(book)
        return make_response(jsonify(books), 200)
    elif request.method == "POST":
        content = request.json
        book = Book(book_id=content['book_id'], name=content['name'], author=content['author'])
        book.save()
        return make_response("", 201)

@application.route('/api/books/<book_id>', methods=['GET','PUT','DELETE'])
def api_each_book(book_id):
    if request.method == "GET":
        book_obj = Book.objects(book_id=book_id).first()
        if book_obj:
            return make_response(jsonify(book_obj.to_json()), 200)
        else:
            return make_response("", 404)
    elif request.method == "PUT":
        content = request.json
        book_obj = Book.objects(book_id=book_id).first()
        book_obj.update(author=content['author'], name=content['name'])
        return make_response("", 204)
    elif request.method == "DELETE":
        book_obj = Book.objects(book_id=book_id).first()
        book_obj.delete()
        return make_response("", 204)

if __name__ == '__main__':
    application.run()
