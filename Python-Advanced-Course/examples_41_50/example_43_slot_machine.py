# Example 43 - Slot machine

import random


def take_bet(balance):
    bet = input("How much do you want to bet: ")

    try:
        bet = float(bet)
    except Exception as e:
        print(f"Invalid amount: {e}")
        return 0

    if bet > balance:
        print("Insufficient founds")
        bet = 0
    elif bet <= 0:
        print("Bet must be greater than zero")
        bet = 0

    return bet


def spin_row():
    symbols = ('🍒', '🔔', '⭐', '🍉', '🍋')

    return [random.choice(symbols) for _ in range(3)]


def show_row(row):
    print(" | ".join(row))


def calc_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🍒':
                bet *= 3
            case '🍉':
                bet *= 4
            case '🍋':
                bet *= 5
            case '🔔':
                bet *= 10
            case '⭐':
                bet *= 20
    else:
        bet = 0

    return bet


def main():
    balance = 100
    is_playing = True

    print("********************************")
    print("          Slot Machine          ")
    print("********************************")

    while is_playing and balance > 0:
        print(f"Your balance is ${balance}")
        bet = take_bet(balance)
        if bet > 0:
            balance -= bet
            row = spin_row()
            payout = calc_payout(row, bet)
            show_row(row)

            if payout > 0:
                balance += payout
                print(f"Congratulations, you won ${payout}!")
            else:
                print("Sorry, you lost.")

        if input("Do you want to try again (Y/n): ").upper() != "Y":
            is_playing = False

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
