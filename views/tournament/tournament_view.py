import inquirer
from constants.common_constants import ANSWER_KEY, NOT_AVAILABLE_FEATURE_STR, SOMETHING_UNEXPECTED_STR
from constants.tournament_view_constants import answers_list, Answer

def tournament_prompt():
    """Display tournament prompt"""
    continue_prompt = True

    while (continue_prompt):
        answer = main_question()

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.CREATE]):
            print(NOT_AVAILABLE_FEATURE_STR)
            print("")
            # create_tournament_prompt()

        elif (answer[ANSWER_KEY] == answers_list[Answer.UPDATE]):
            print(NOT_AVAILABLE_FEATURE_STR)
            print("")

        elif (answer[ANSWER_KEY] == answers_list[Answer.DELETE]):
            print(NOT_AVAILABLE_FEATURE_STR)
            print("")

        elif (answer[ANSWER_KEY] == answers_list[Answer.VIEW]):
            print(NOT_AVAILABLE_FEATURE_STR)
            # show_tournament_prompt()
            print("")

        else:
            print(SOMETHING_UNEXPECTED_STR)
            print("")


def main_question():
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message="Player: What do you want to do?",
            choices=[
                answers_list[Answer.CREATE],
                answers_list[Answer.VIEW],
                answers_list[Answer.UPDATE],
                answers_list[Answer.DELETE],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
