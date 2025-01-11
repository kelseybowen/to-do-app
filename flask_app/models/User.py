from flask_app.config.dbconnection import connectToMySQL
import datetime

class User:
    db = 'to_do_app'
    def __init__(self, data):
        self._id = data['id']
        self._name = data['name']
        self._email = data['email']
        self._lists = []

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email
    
    def get_tasks(self):
        return self._lists
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        all_users = []
        for user in results:
            all_users.append(user)
        return all_users
    
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (name, email) VALUES (%(name)s, %(email)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    


        
