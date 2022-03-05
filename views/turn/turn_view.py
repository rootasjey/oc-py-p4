import inquirer
from views.turn.create_turn_view import generate_next_turn_prompt
from views.turn.show_turn_view import show_turn_prompt
from constants.player_view_constants import Answer, answers_list
from constants.common_constants import ANSWER_KEY, SOMETHING_UNEXPECTED_STR
from controllers.turn_controller import create_turn
from controllers.tournament_controller import get_tournament_from_id


def turn_prompt():
    """Display player prompt"""
    continue_prompt = True

    while (continue_prompt):
        answer = main_question()

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.CREATE]):
            generate_next_turn_prompt()

            tournament = get_tournament_from_id
            turn = tournament.turns
            create_turn(turn, tournament)

        elif (answer[ANSWER_KEY] == answers_list[Answer.VIEW]):
            show_turn_prompt()

        else:
            print(SOMETHING_UNEXPECTED_STR)


def main_question():
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message="Turn: What do you want to do?",
            choices=[
                answers_list[Answer.CREATE],
                answers_list[Answer.VIEW],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
