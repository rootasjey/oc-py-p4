import inquirer
from enum import Enum
from controllers.player_controller import get_all_players_as_list, get_player_from_id
from constants.common_constants import ANSWER_KEY


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK = 0


answers_list = {
    Answer.BACK: "Back",
}


def show_player_prompt():
    """Show players in the console."""

    continue_prompt = True

    while continue_prompt:
        players_list = get_all_players_as_list()

        questions = [
            inquirer.List(
                ANSWER_KEY,
                message="All saved players",
                choices=players_list,
                carousel=True,
            ),
        ]

        answers = inquirer.prompt(questions)

        if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False
        else:
            show_single_player(answers)


def show_single_player(answers):
    """Format & display a single player to the console."""
    player = get_player_from_id(answers[ANSWER_KEY])
    #pprint(player)

    print("------")
    print(f"• First name: {player['first_name']}\n• Last name: {player['last_name']}\n• Elo: {player['elo']}\n• Sex: {player['sex']}\n• Birth date: {player['birth_date']}")
    print("------")
    print("")
