from flask_app.config.dbconnection import connectToMySQL
from datetime import date

class Task:
    db = 'to_do_app'
    def __init__(self, data):
        self._id = data['id']
        self._title = data['title']
        self._start_date = data['start_date']
        self._due_date = data['due_date']
        self._notes = data['notes']
        self._is_completed = False
        self._list_id = data['list_id']

    def get_task_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def get_start_date(self):
        return self._start_date
    
    def get_due_date(self):
        return self._due_date
    
    def get_notes(self):
        return self._notes
    
    def get_list_id(self):
        return self._list_id
    
    @classmethod
    def get_all_tasks(cls):
        query = "SELECT * FROM tasks;"
        results = connectToMySQL(cls.db).query_db(query)
        all_tasks = []
        for task in results:
            all_tasks.append(task)
        return all_tasks
    
    @classmethod
    def get_task_by_id(cls, data):
        query = "SELECT * FROM tasks WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]
    
    @classmethod
    def get_tasks_by_list_id(cls, data):
        query = "SELECT * FROM tasks WHERE list_id = %(list_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        user_tasks = []
        for task in results:
            user_tasks.append(task)
        return user_tasks
    
    @classmethod
    def create_task(cls, data):
        if data['start_date'] == '':
            data['start_date'] = date.today()
        query = "INSERT INTO tasks (title, start_date, due_date, notes, is_completed, list_id) VALUES (%(title)s, %(start_date)s, %(due_date)s, %(notes)s, 0, %(list_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def complete_task(cls, data):
        query = "UPDATE tasks SET is_completed = True WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def change_due_date(cls, data):
        query = "UPDATE tasks SET due_date = %(due_date)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_task(cls, data):
        query = "DELETE FROM tasks WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
