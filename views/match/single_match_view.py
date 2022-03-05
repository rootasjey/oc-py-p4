import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR
#from controllers.tournament_controller import get_all_tournaments_as_list
from views.match.enter_score_player import enter_score_player_prompt
#from controllers.turn_controller import update_turn


class Answer(Enum):
    """Possible answers for this prompt"""

    UPDATE = 0
    BACK = 1


answers_list = {

    Answer.UPDATE: "Update",
    Answer.BACK: "Back",
}


def single_match_prompt(turn, match):
    """Show match in the console."""
    # print(main_question(turn,match))
    # main_question(turn,match)

    continue_prompt = True
    #match = turn.matchs[index_match]
    while (continue_prompt):
        answer = main_question(turn, match)

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.UPDATE]):
            enter_score_player_prompt(turn, match)
            continue_prompt = True

        else:
            print(SOMETHING_UNEXPECTED_STR)


def main_question(turn, match):
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message=f"({match}): What do you want to do?",
            choices=[
                answers_list
                [Answer.UPDATE],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
