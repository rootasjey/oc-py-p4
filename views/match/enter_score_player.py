# -*- coding: utf-8 -*-

import inquirer
from enum import Enum
from controllers.turn_controller import update_turn
from constants.common_constants import ANSWER_KEY


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK = 0
    MATCH_NUL = 1


answers_list = {
    Answer.BACK: "Back",
    Answer.MATCH_NUL: "Match nul"
}


def enter_score_player_prompt(turn, selected_match_index, player_1, player_2):
    """enter_score_player_prompt"""
    continue_prompt = True
    updated_match = False
    #print(f"selected_match_index: {selected_match_index} | player_1: {player_1} | player_2: {player_2}")

    # On veut afficher un menu de 3 éléments:
    # répondant à la question:
    # • Qui a gagné ce match ?
    # -
    # Réponses:
    # • Joueur 1: <nom du joueur>
    # • Joueur 2: <nom du joueur>
    # • Match nul
    # • Back (retour)
    # -

    match = turn.matchs[selected_match_index]

    while (continue_prompt):
        answer = main_question(match, selected_match_index, player_1, player_2)

        if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
            continue_prompt = False
        elif (answer[ANSWER_KEY] == answers_list[Answer.MATCH_NUL]):
            match[0][1] = 0.5
            match[1][1] = 0.5
            update_turn(turn)
            updated_match = True
        else:
            if (answer["answer"] == match[0][0]):
                # mettre à jour le score du jouer 1
                match[0][1] = 1
                match[1][1] = 0

            elif (answer["answer"] == match[1][0]):
                # mettre à jour le score du jouer 2
                match[0][1] = 0
                match[1][1] = 1

            update_turn(turn)
            continue_prompt = False
            updated_match = True

    return updated_match


def main_question(match, selected_match_index, player_1, player_2):
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message=f"Who won the match ?",
            choices=[
                (f"Player 1: {player_1}", player_1.id),
                (f"Player 2: {player_2}", player_2.id),
                answers_list[Answer.MATCH_NUL],
                answers_list[Answer.BACK],
            ],
            carousel=True,
        )
    ])
    return answer
