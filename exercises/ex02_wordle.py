"""The goal of this program is to allow my friends to play a fun game of Wordle!"""

__author__ = "730578934"


def contains_char(secret: str, character: str) -> bool:
    """Searches the secret word to see if guessed letter is in that word"""
    assert len(character) == 1, f"len('{character}') is not 1"

    idx = 0
    while idx < len(secret):
        if secret[idx] == character:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emojis to color-code the result of the guess with Wordles color logic"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"

    result = ""
    idx = 0
    while idx < len(secret):
        if secret[idx] == guess[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompts player to guess a word that is the expected length of the guess"""

    guess = str(input(f"Enter a {expected_length} character word:"))
    while len(guess) != expected_length:
        guess = str(input(f"That wasn't {expected_length} chars! Try again:"))
    else:
        return guess


def main(secret: str) -> None:
    """Entrypoint of the program and main game loop"""

    turn = 1
    won = False

    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turn += 1

    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
