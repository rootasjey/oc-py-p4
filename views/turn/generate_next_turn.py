import inquirer
from enum import Enum
from models.turn import Turn
from controllers.turn_controller import save_turn, create_match, create_next_match
from views.tournament.add_turn import add_turn_to_tournament


class Answer(Enum):
    """Possible answers for this prompt"""
    NAME = 0
    START_DATE = 1
    END_DATE = 2
    MATCHS = 3


answers_list = {
    Answer.NAME: "Name",
    Answer.START_DATE: "Start date",
    Answer.END_DATE: "End date",
    Answer.MATCHS: "Matchs",
}


def generate_next_turn_prompt(tournament):
    """Generate the next turn"""
    continue_prompt = True
    question = [
        inquirer.List(
            "type",
            message="Are sure to create new turn?",
            choices=["Yes", "No"],
        ),
    ]

    answers = inquirer.prompt(question)
    if (answers['type']) == "No":
        continue_prompt = False
    elif (answers['type']) == "Yes":
        continue_prompt = True
        answers = start_questions()

        new_turn = Turn(id=id,
                        name=answers[answers_list[Answer.NAME]],
                        start_time=answers[answers_list[Answer.START_DATE]],
                        end_time=answers[answers_list[Answer.END_DATE]],
                        matchs=[],
                        )
        if (len(tournament.turns) == 0):

            new_turn = save_turn(new_turn)
            add_turn_to_tournament(tournament, new_turn)
            print("creation du premier tour")
            create_match(new_turn, tournament)

        else:
            new_turn = save_turn(new_turn)
            add_turn_to_tournament(tournament, new_turn)
            print("creation des tours supplémentaire (>1)")
            create_next_match(new_turn,  tournament)

    return new_turn


def start_questions():
    """Start a serie of question to create a new turn."""
    answers = inquirer.prompt([
        inquirer.Text(
            answers_list[Answer.NAME],
            message="What is your turn name?",
            default="B",
            show_default=True,
        ),


        inquirer.Text(
            answers_list[Answer.START_DATE],
            message="When does it start?",
            default="10/28/21",
            show_default=True,
        ),

        inquirer.Text(
            answers_list[Answer.END_DATE],
            message="When does it end?",
            default="10/30/21",
            show_default=True
        ),
    ])

    return answers
