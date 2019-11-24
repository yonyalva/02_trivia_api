import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # questions endpoint tests 
    def test_questions(self):
        """Test _____________ """
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)

    def test_405_questions(self):
        """Test _____________ """
        res = self.client().get('/questions/1')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Method Not Allowed')
        self.assertEqual(res.status_code, 405)

    # categories endpoint tests 
    def test_categories(self):
        """Test _____________ """
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 200)

    def test_404_categories(self):
        """Test _____________ """
        res = self.client().get('/categories/1')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Not found')
        self.assertEqual(res.status_code, 404)

    # question delete endpoint tests 
    def test_delete_question(self):
        """Test _____________ """
        res = self.client().delete('/questions/2')
        self.assertEqual(res.status_code, 200)

    def test_422_categories(self):
        """Test _____________ """
        res = self.client().delete('/questions/1000000')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertEqual(res.status_code, 422)

    # create new question bad endpoint test
    def test_404_new_question(self):
        """Test _____________ """
        res = self.client().post('/questions_new/100000')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Not found')
        self.assertEqual(res.status_code, 404)

    # search questions bad endpoint test

    def test_405_search_question(self):
        """Test _____________ """
        res = self.client().post('/questions/1')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Method Not Allowed')
        self.assertEqual(res.status_code, 405)

    # categories side bar endpoint tests 
    def test_categories_sidebar(self):
        """Test _____________ """
        res = self.client().get('/categories/5/questions')
        self.assertEqual(res.status_code, 200)

    def test_404_categories_sidebar(self):
        """Test _____________ """
        res = self.client().get('/categories/1000000/questions')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Not found')
        self.assertEqual(res.status_code, 404)

    # play quizzes bad endpoint test
    def test_404_quizzes_play(self):
        """Test _____________ """
        res = self.client().post('/quizzes/1')
        data = json.loads(res.data)
        self.assertEqual(data['message'], 'Not found')
        self.assertEqual(res.status_code, 404)
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()