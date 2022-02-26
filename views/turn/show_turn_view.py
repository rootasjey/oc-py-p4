import inquirer
from enum import Enum
from controllers.turn_controller import get_all_turns_as_list, get_turn_from_id
from constants.common_constants import ANSWER_KEY
from views.turn.single_player_view import single_turn_prompt


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK = 0


answers_list = {
    Answer.BACK: "Back",
}


def show_turn_prompt():
    """Show players in the console."""

    continue_prompt = True

    while continue_prompt:
        turns_list = get_all_turns_as_list()

        questions = [
            inquirer.List(
                ANSWER_KEY,
                message="All saved turns",
                choices=turns_list,
                carousel=True,
            ),
        ]

        answers = inquirer.prompt(questions)

        if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False
        else:
            turn = get_turn_from_id(answers[ANSWER_KEY])
            #player = deserialize_player(player_data)
            show_single_turn(turn)
            single_turn_prompt(turn)


def show_single_turn(turn):
    """Format & display a single turn to the console."""
    
    print("------")
    print(
        f"• First name: {turn.name}\n• \n• Start time: {turn.start_time}\n• End time: {turn.end_time}"
    )
    print("------")
    print("")
