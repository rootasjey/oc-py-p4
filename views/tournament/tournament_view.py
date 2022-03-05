import inquirer
from constants.common_constants import ANSWER_KEY, SOMETHING_UNEXPECTED_STR
from constants.tournament_view_constants import answers_list, Answer
from views.tournament.create_tournament_view import create_tournament_prompt
from views.tournament.show_tournament_view import show_tournament_prompt


def tournament_prompt():
    """Display tournament prompt"""
    continue_prompt = True

    while (continue_prompt):
        answer = main_question()

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.CREATE]):
            create_tournament_prompt()

        elif (answer[ANSWER_KEY] == answers_list[Answer.VIEW]):
            show_tournament_prompt()

        else:
            print(SOMETHING_UNEXPECTED_STR)
            print("")


def main_question():
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message="Tournament: What do you want to do?",
            choices=[
                answers_list[Answer.VIEW],
                answers_list[Answer.CREATE],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
