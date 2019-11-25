# Trivia API

## Table of Contents

* [Download-Clone](#download-clone)
* [Instructions](#instructions)
* [API-Getting-Started](#api-getting-started)

## Download-Clone

* download-clone from:

 https://github.com/yonyalva/02_trivia_api.git
 
 ## Instructions

To get started:

* for the backend api server follow instructions in the the backend readme file: 
 * [`./backend/`](./backend/README.md)
* for the sample frontend app, follow instructions in the frontend readme file:
  * [`./frontend/`](./frontend/README.md)

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
