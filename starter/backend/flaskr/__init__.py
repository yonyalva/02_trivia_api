import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from random import choices

from models import setup_db, Question, Category

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
      response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE')
      return response

  @app.route('/categories')
  # creates the categories endpoint
  def get_categories():
          categories = Category.query.all()
          formatted_categories = [category.format() for category in categories]

          if len(formatted_categories) == 0:
            abort(404)
          # display results
          return jsonify({
          'success':True,
          'categories': formatted_categories
            })
  
  @app.route('/questions')
  # creates the questions endpoint
  def get_questions():
          page = request.args.get('page', 1, type=int)
          start = (page - 1) * 10
          end = start + 10
          questions = Question.query.order_by('id').all()
          formatted_questions = [question.format() for question in questions]
          categories = Category.query.all()
          formatted_categories = [category.format() for category in categories]

          if len(formatted_questions) == 0:
            abort(404)
          
          # display results
          return jsonify({
          'success':True,
          'questions': formatted_questions[start:end],
          'total_questions': len(formatted_questions),
          'categories': formatted_categories,
          'current_category': 'Science'
            })

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  # creates the delete question endpoint
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()

      # display results
      return jsonify({
      'success':True,
      'deleted': question_id
        })
    
    except:
      abort(422)

  @app.route('/questions_new', methods=['POST'])
  # creates the create a new question endpoint
  def new_question():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_difficulty = body.get('difficulty', None)
    new_category = body.get('category', None)

    try:
      question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
      question.insert()

      # display results
      return jsonify({
      'success':True,
      'question': question.id
        }) 
    except:
      abort(422)


  @app.route('/questions', methods=['POST'])
  # search on questions with partial string search. Case-insensitive.
  def search_questions():
      data = request.get_json()
      tag = data['searchTerm']
      search = "%{}%".format(tag)
      questions = Question.query.filter(Question.question.ilike(search)).order_by('id').all()
      formatted_questions = [question.format() for question in questions]
      
      if len(formatted_questions) == 0:
        abort(404)

      # display results
      return jsonify({
      'success':True,
      'questions': formatted_questions
        })

  @app.route('/categories/<int:category_id>/questions')
  # creates the sidebar in the list page endpoint
  def get_specific_category(category_id):
          questions = Question.query.filter(Question.category == category_id).order_by('id').all()
          formatted_questions = [question.format() for question in questions]
          categories = Category.query.all()
          formatted_categories = [category.format() for category in categories]

          if len(formatted_questions) == 0:
            abort(404)

          if len(formatted_categories) == 0:
            abort(404)

          # display results
          return jsonify({
          'success':True,
          'questions': formatted_questions,
          'categories': formatted_categories,
          'total_questions': len(formatted_questions),
          'current_category': 'Science'
            })

  @app.route('/quizzes', methods=['POST'])
  # creates the play (quizzes) endpoint
  def play_quiz():
    body = request.get_json()

    previous_questions = body.get('previous_questions', None)
    quiz_category = body.get('quiz_category', None)

    try:
      if quiz_category['type'] == "click":
          questions = Question.query.all()
      else:
          questions = Question.query.filter(Question.category == quiz_category['id']).all()

      formatted_questions = [question.format() for question in questions]

      random_choices = random.choices(formatted_questions)
      random_choice = random.choice(random_choices)

      # display results
      return jsonify({
      'success':True,
      'question': random_choice
        })
    except:
      abort(422)

  # app error handlers
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "Internal Server Error"
      }), 500

  @app.errorhandler(405)
  def not_allow(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "Method Not Allowed"
      }), 405

  return app