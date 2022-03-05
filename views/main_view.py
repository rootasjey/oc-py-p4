import inquirer
from enum import Enum
from views.player.player_view import player_prompt
from views.tournament.tournament_view import tournament_prompt
from constants.common_constants import ANSWER_KEY, SOMETHING_UNEXPECTED_STR


class Answer(Enum):
    """Possible answers for this prompt"""
    EXIT = 0
    PLAYER = 1
    TOURNAMENT = 2


answers_list = {
    Answer.EXIT: "Exit",
    Answer.PLAYER: "Manage players",
    Answer.TOURNAMENT: "Manage tournaments"
}


def prompt():
    """Show the main prompt."""
    continue_prompt = True

    while (continue_prompt):
        answer = main_question()

        if (answer[ANSWER_KEY] == answers_list[Answer.EXIT]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.PLAYER]):
            player_prompt()

        elif (answer[ANSWER_KEY] == answers_list[Answer.TOURNAMENT]):
            tournament_prompt()

        else:
            print(SOMETHING_UNEXPECTED_STR)


def main_question():
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message="General: What do you want to do?",
            choices=[
                answers_list[Answer.TOURNAMENT],
                answers_list[Answer.PLAYER],
                answers_list[Answer.EXIT]
            ],
            carousel=True,
        )
    ])

    return answer
