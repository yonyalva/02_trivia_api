# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
##### Optional only if testing with the frontend app sample
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API-Getting-Started
* Base URL: At present this app can only be run locally and is not hosted as a based URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
* Authentication: This version of the application does not require authentication or API keys.

## Error Handling
Errors are returned as JSON objects in the following format:

```bash
{
  "error": 404, 
  "message": "Not found", 
  "success": false
}
```
The API will return four error types when requests fail:
* 400: bad request
* 404: Not found
* 422: unprocessable
* 500: Internal Server Error

## Endpoints
### GET /questions
* General:
  * Returns a list of categories, questios, success value, and total number of questions
  * Results are paginated in groups of 10. Includes a request argument to choose page number, starting from 1
* Sample: `curl http://127.0.0.1:5000/questions`

```bash
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
...
  ], 
  "current_category": "Science", 
  "questions": [
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
...
  ], 
  "success": true, 
  "total_questions": 26
```
### GET /categories
* General:
  * Returns a list of categories, with colums id and type
* Sample: `curl http://127.0.0.1:5000/categories`

```bash
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "success": true
}
```
### DELETE /questions/<int:question_id>
* General:
  * Deletes the question using parameter question_id
* Display results:

```bash
  "success":True,
  "deleted": question_id
```
### POST /questions_new
* General:
  * Creates a new question requesting arguments: question, answer, difficulty, and category
* Display results:

```bash
  "success":True,
  "question": question.id
```
### POST /questions
* General:
  * Searches for questions using key words
* Display results:

```bash
  "success":True,
  "questions": formatted_questions
```
### GET /categories/<int:category_id>/questions
* General:
  * Returns a list of questions only based on a particular category using parameter category_id
* Sample: `curl http://127.0.0.1:5000/categories/2/questions`

```bash
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
...
  ], 
  "questions": [
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
...
  ], 
  "success": true, 
  "total_questions": 6
}
```
### POST /quizzes
* General:
  * Generates a random question where players can pick all categories or a specific category
  * Requesting arguments: previous_questions, and quiz_category
* Display results:

```bash
  "success":True,
  "question": random_choice
```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
