import React, { Component } from 'react';
import '../stylesheets/Question.css';
import { type } from 'os';

class Question extends Component {
  constructor(){
    super();
    this.state = {
      visibleAnswer: false
    }
  }

  flipVisibility() {
    this.setState({visibleAnswer: !this.state.visibleAnswer});
  }

  render() {
    // Changed below const to let to be able to change the category variable YA
    let { question, answer, category, difficulty } = this.props; 
    
    // added this switch to be able to get the images to show YA
    switch (category)
{
    case 1:
        category = "Science";
        break;

    case 2:
        category = "Art";
        break;

    case 3:
        category = "Geography";
        break;

    case 4:
        category = "History";
        break;

    case 5:
        category = "Entertainment";
        break;

    case 6:
        category = "Sports";
        break;

    default:
        category = "Science";
        break;

}
    return (
      <div className="Question-holder">
        <div className="Question">{question}</div>
        <div className="Question-status">
          <img className="category" src={`${category}.svg`}/>
          <div className="difficulty">Difficulty: {difficulty}</div>
          <img src="delete.png" className="delete" onClick={() => this.props.questionAction('DELETE')}/>
          
        </div>
        <div className="show-answer button"
            onClick={() => this.flipVisibility()}>
            {this.state.visibleAnswer ? 'Hide' : 'Show'} Answer
          </div>
        <div className="answer-holder">
          <span style={{"visibility": this.state.visibleAnswer ? 'visible' : 'hidden'}}>Answer: {answer}</span>
        </div>
      </div>
    );
  }
}

export default Question;
