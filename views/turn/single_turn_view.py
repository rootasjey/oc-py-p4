import inquirer
from enum import Enum
from controllers.turn_controller import delete_turn
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR
from views.match.show_matchs_view import  show_matchs_tournament_prompt

class Answer(Enum):
    """Possible answers for this prompt"""
    SHOW_MATCHS = 0
    DELETE = 1
    BACK = 2


answers_list = {
    Answer.SHOW_MATCHS: "Show matchs",
    Answer.DELETE: "Delete",
    Answer.BACK: "Back",
}


def single_turn_prompt(turn, tournament):
    """Show tournaments in the console."""

    continue_prompt = True

    while (continue_prompt):
        answer = main_question(turn)

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.SHOW_MATCHS]):
        
        
           show_matchs_tournament_prompt(turn)

        elif (answer[ANSWER_KEY] == answers_list[Answer.DELETE]):
            delete_turn(turn)
            continue_prompt = True

        else:
            print(SOMETHING_UNEXPECTED_STR)


def main_question(turn):
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message=
            f"{turn.name} ({turn.start_time}): What do you want to do?",
            choices=[
                answers_list[Answer.SHOW_MATCHS],
                answers_list
                [Answer.DELETE],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
