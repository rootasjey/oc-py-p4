import inquirer
from enum import Enum
from controllers.tournament_controller import delete_tournament
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR
#from views.tournament.create_tournament_view import create_tournament_prompt
from views.tournament.add_player import add_player_tournament_prompt
from views.tournament.show_players_tournament import show_players_tournament_prompt
from views.tournament.show_turns_tournament import show_turns_tournament_prompt
#from views.tournament.add_turn import add_turn_tournament_prompt
#from views.turn.create_turn_view import create_turn_prompt
from views.turn.generate_next_turn import generate_next_turn_prompt
from controllers.turn_controller import sorte_players_by_score,sorte_players_by_alphabet




class Answer(Enum):
    """Possible answers for this prompt"""
    SHOW_PLAYERS = 0
    REPORT_BY_SCORE = 7
    REPORT_BY_ALPHAB = 8
    GENERATE_NEXT_TURN = 1
    SHOW_TURNS = 2
    ADD_PLAYER = 3
    DELETE = 5
    BACK = 6


answers_list = {
    Answer.SHOW_PLAYERS: "Show tournament's players",
    Answer.REPORT_BY_SCORE: "Report by score",
    Answer.REPORT_BY_ALPHAB: "Report by alphabet",
    Answer.GENERATE_NEXT_TURN: "Generate next turn",
    Answer.SHOW_TURNS: "Show tournament's turns",
    Answer.ADD_PLAYER: "Add player to tournament",
    Answer.DELETE: "Delete",
    Answer.BACK: "Back",
}


def single_tournament_prompt(tournament):
    """Show tournaments in the console."""

    continue_prompt = True

    while (continue_prompt):
        answer = main_question(tournament)

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False

        elif (answer[ANSWER_KEY] == answers_list[Answer.ADD_PLAYER]):
            add_player_tournament_prompt(tournament)

        elif (answer[ANSWER_KEY] == answers_list[Answer.SHOW_PLAYERS]):
          show_players_tournament_prompt(tournament)

        elif (answer[ANSWER_KEY] == answers_list[Answer.REPORT_BY_SCORE]):
          sorte_players_by_score(tournament)
        elif (answer[ANSWER_KEY] == answers_list[Answer.REPORT_BY_ALPHAB]):
          sorte_players_by_alphabet(tournament)
      
        elif (answer[ANSWER_KEY] ==    answers_list[Answer.GENERATE_NEXT_TURN]):
            generate_next_turn_prompt(tournament)

        elif (answer[ANSWER_KEY] ==    answers_list[Answer.SHOW_TURNS]):
            show_turns_tournament_prompt(tournament)

        elif (answer[ANSWER_KEY] == answers_list[Answer.DELETE]):
            delete_tournament(tournament)
            continue_prompt = False

        else:
            print(SOMETHING_UNEXPECTED_STR)


def main_question(tournament):
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message=
            f"{tournament.name} {tournament.location} ({tournament.start_date}): What do you want to do?",
            choices=[
                answers_list[Answer.ADD_PLAYER],
                answers_list[Answer.GENERATE_NEXT_TURN],
                answers_list[Answer.SHOW_TURNS],
                answers_list[Answer.SHOW_PLAYERS],
                answers_list[Answer.REPORT_BY_SCORE],answers_list[Answer.REPORT_BY_ALPHAB],
                answers_list[Answer.DELETE],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])

    return answer
