import inquirer
from enum import Enum
from controllers.tournament_controller import get_all_tournaments_as_list, get_tournament_from_id, deserialize_tournament
from constants.common_constants import ANSWER_KEY
from views.tournament.single_tournament_view import single_tournament_prompt


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK = 0


answers_list = {
    Answer.BACK: "Back",
}


def show_tournament_prompt():
    """Show tournaments in the console."""

    continue_prompt = True

    while continue_prompt:
        tournaments_list = get_all_tournaments_as_list()
        questions = [
            inquirer.List(
                ANSWER_KEY,
                message="All saved tournaments",
                choices=tournaments_list,
                carousel=True,
            ),
        ]

        answers = inquirer.prompt(questions)

        if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False
        else:
            tournament_data = get_tournament_from_id(answers[ANSWER_KEY])
            tournament = deserialize_tournament(tournament_data)
            show_single_tournament(tournament)
            single_tournament_prompt(tournament)


def show_single_tournament(tournament):
    """Format & display a single tournament to the console."""

    print("------")
    print(
        f"• Name: {tournament.name}\n• Location: {tournament.location}\n• Start date: {tournament.start_date}\n• End date: {tournament.end_date}\n• Number of turns: {tournament.number_of_turns}\n• Number of players: {len(tournament.players)}\n• Current turn: {len(tournament.turns)}"
    )
    print("------")
    print("")


def not_player(tournament):
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message="Back",
            choices=[

                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
