# DATABASE MANAGEMENT SYSTEM
# Build your own database engine, using text files as low level storage method.
# You are supposed to store one single "table" with information about some topic you decide.

# As a user of your database engine, I need to be able to count, insert, update, query and remove
# information from a my database.

from datetime import datetime


class MultipleObjectsReturned(Exception):
    pass


class Database(object):
    def __init__(self, name, file_path, delimiter, fields):
        self.name = name
        self.file_path = file_path
        self.delimiter = delimiter
        self.fields = fields
        self.database = []
        self.database_refresh()

    # Checks to see if the given file contains an existing db and populates the temporary db (self.database).
    # Need to recheck if this actually gets run using another test db.
    def database_refresh(self):
        with open("{}".format(self.file_path), 'r') as f:
            if sum([1 for entry in f]) > 1:
                print("Existing data detected, setting up temporary database.")
                existing_entries = [entry for entry in f][1:] # Excludes header
                for existing_entry in existing_entries:
                    id, first_name, last_name, country = [value.strip() for value in existing_entry.split("|")]
                    data = {"first_name": first_name, "last_name": last_name, "country": country}
                    self.insert(data, int(id))
            else:
                print("A new temporary database has been created. Run migrate database after any changes.")

    def insert(self, new_data, new_id=1):
        new_entry = {}

        # Finds the lowest unused ID number.
        new_id = new_id
        for entry in self.database:
            if entry['id'] != new_id:
                break
            else:
                new_id += 1

        # Sets data into a temporary entry
        for field_item in self.fields:
            if field_item == "id":
                new_entry[field_item] = new_id

            else:
                new_entry[field_item] = new_data[field_item]

        # Inserts new entry into db.
        self.database.insert(new_id-1, new_entry)
        return "{}. {} {} was added.".format(new_entry['id'], new_entry['first_name'],
                                            new_entry['last_name'])

    def count(self):
        return "There are currently {} entries.".format(len(self.database))

    def query(self, search_criteria):
        # returns all entries given search criteria.
        query_results = []
        for entry in self.database:
            for attribute, value in search_criteria.items():
                if entry[attribute] == value:
                    query_results.append(entry)

        return query_results

    def get(self, search_criteria):
        # returns a single entry given criteria, if more than one result is given exception is thrown.
        query_results = self.query(search_criteria)
        if len(query_results) > 1:
            raise MultipleObjectsReturned("More than one entry was found using those search parameters.")
        elif len(query_results) == 1:
            return query_results
        else:
            return "No entries were found using those search parameters."

    def update(self, search_criteria, fields, multiple=False):

        query_results = self.query(search_criteria)
        first_result = query_results[0]

        if multiple and query_results:
            for result in query_results:
                print("Entry at ID number {} has been updated.".format(result['id']))
                for update_attribute, new_value in fields.items():
                    self.database[result['id']-1][update_attribute] = new_value
        elif not multiple and first_result:
            print("Entry at ID: {} has been updated.".format(first_result['id']))
            for update_attribute, new_value in fields.items():
                self.database[first_result['id']-1][update_attribute] = new_value
        else:
            return "No entries were found using those search parameters."

    def remove(self, search_criteria, multiple=False):
        search_results = self.query(search_criteria)

        if multiple and search_results:
            for entry in search_results:
                self.database.remove(entry)
                print("Entry with ID {} has been deleted.".format(entry["id"]))
        elif not multiple and search_results[0]:
            self.database.remove(search_results[0])
            print("Entry with ID {} has been deleted.".format(search_results[0]["id"]))
        else:
            return "No entries were found using those search parameters."

    @staticmethod
    def print_format(string, width=15):
        space = " " * int(width-len(string))
        return "{}{}".format(string, space)

    @staticmethod
    def migration_log(log_path):
        with open("{}".format(log_path), 'a') as f:
            f.write("A migration was made at {}.\n".format(str(datetime.now())))
        print("Log updated.")

    def migrate_database(self):
        print("Are you sure you want to reset the database? (Y/N)")
        check = input(">>> ")
        if check in "YESyesYesYEsyESyeS":
            print("Updating database now...")
            self.migration_log('log.txt')
            with open("{}".format(self.file_path), "w") as f:
                header = "{}".format(self.delimiter).join([self.print_format("ID", 5), self.print_format("FIRST NAME"),
                                                          self.print_format("LAST NAME"), self.print_format("COUNTRY")])
                f.write("{}\n".format(header))
                for entry in self.database:
                    # There has to be a cleaner way than this.
                    new_entry = "{}".format(self.delimiter).join([self.print_format(str((entry['id'])), 5),
                                                                 self.print_format(entry['first_name']),
                                                                 self.print_format(entry['last_name']),
                                                                 self.print_format(entry['country'])])
                    f.write("{}\n".format(new_entry))
            print("Updating complete. Database is located at {}".format(self.file_path))
        else:
            print("Aborting current process...")