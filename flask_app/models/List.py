from flask_app.config.dbconnection import connectToMySQL

class List:
    db = 'to_do_app'
    def __init__(self, data):
        self._id = data['id']
        self._title = data['title']
        self._owner_id = data['owner_id']
        self._tasks = []

    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def get_owner(self):
        return self._owner
    
    def get_tasks(self):
        return self._tasks
    
    @classmethod
    def get_all_lists(cls):
        query = "SELECT * FROM lists;"
        results = connectToMySQL(cls.db).query_db(query)
        all_lists = []
        for list in results:
            all_lists.append(list)
        return all_lists
    
    @classmethod
    def get_all_lists_by_user(cls, data):
        query = "SELECT * FROM lists WHERE owner_id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        user_lists = []
        for list in results:
            user_lists.append(list)
        return user_lists
    
    @classmethod
    def get_list_by_id(cls, data):
        query = "SELECT * FROM lists WHERE id = %(list_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]
    
    @classmethod
    def create_list(cls, data):
        query = "INSERT INTO users (title, owner_id) VALUES (%(title)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_list(cls, data):
        query = "DELETE FROM lists WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)