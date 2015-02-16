from database_example import Database

def test():
    db = Database(name="students",
                  file_path="example_db.txt",
                  delimiter="|",
                  fields=["id", "first_name", "last_name", "country"])
    print(db.insert({"first_name": "Martin", "last_name": "Zugnoni", "country": "Argentina"}))
    print(db.insert({"first_name": "Santiago", "last_name": "Basulto", "country": "Argentina"}))

    print(db.count())
    print(db.query({"country": "Argentina"}))
    print(db.get({"first_name": "Martin"}))
    # print(db.get({"country": "Argentina"})) # Raises the correct exception.

    db.update({"id": 2}, {"first_name": "Santi"}, multiple=False)
    print(db.get({"id": 2}))

    print(db.count())
    db.remove({"id": 1}, multiple=False)
    print(db.count())

    print(db.insert({"first_name": "Captain", "last_name": "Crunch", "country": "USA"}))
    print(db.insert({"first_name": "Charlie", "last_name": "Lee", "country": "USA"}))
    print(db.insert({"first_name": "Gayle", "last_name": "McDowell", "country": "USA"}))
    print(db.insert({"first_name": "John", "last_name": "Steinbeck", "country": "USA"}))
    print(db.database)

    # Be sure to migrate the db after all changed have been made.
    db.migrate_database()
test()

