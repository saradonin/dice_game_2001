import random

size_list = [3, 4, 6, 8, 10, 12, 20, 100]


def get_player_input():
    """
    Prompts player to input a dice side. Validated that input.
    If dice size is valid: D3, D4, D6, D8, D10, D12, D20, D100 returns the size.
    Else returns input message again until the conditions are met.
    :return: int - size of the dice
    """
    print("Press enter to roll or choose a dice:")

    while True:
        input_str = input().lower()

        # test for empty
        if input_str == '':
            size = 6
            return size

            # test for d
        if 'd' not in input_str:
            print("Invalid input. Try again.")
            continue

        try:
            size = int(input_str.replace('d', ''))
            if size in size_list:
                return size
            else:
                print("Invalid dice size. Try again.")

        except ValueError:
            print("Invalid input. Try again.")


def dice_roll(size=6):
    """
    Takes size of the dice to be rolled and returns the result of the roll.
    :param size: int - size of the dice
    :return: int - rolled value
    """
    return random.randint(1, size)


def calculate_score(score, roll):
    """
    Takes current score and roll, returns total score after current roll has been calculated and added.
    :param score: int - score before the current roll
    :param roll: int - current roll value
    :return:
    """
    if sum(roll) == 7:
        score = score // 7
    elif sum(roll) == 11:
        score = score * 11
    else:
        score += sum(roll)

    return score


def game_2001(num=2):
    """
    Takes number of dices to roll. Utilizes other functions to perform the roll action until win conditions are met.
    :param num: int - number of dices
    :return: string - win message
    """
    player_score = 0
    comp_score = 0
    modifier = 1

    print("""Press enter or enter a dice manually. 
Possible dice sizes: D3, D4, D6, D8, D10, D12, D20, D100.
Whoever reaches 2001 points first wins.
  """)

    while True:
        # print("Press enter to roll:")

        # while True:
        #   start = input()

        #   if start != '':
        #     print("Invalid input")
        #     continue
        player_size = get_player_input()
        comp_size = size_list[random.randint(0, 7)]

        player_roll = [dice_roll(player_size) for i in range(num)]
        comp_roll = [dice_roll(comp_size) for i in range(num)]

        player_score = calculate_score(player_score, player_roll)
        comp_score = calculate_score(comp_score, comp_roll)

        print(f"Player: {player_size} {player_roll}, {player_score},\nComputer: {comp_size} {comp_roll}, {comp_score}")
        # win conditions
        if player_score > 2001 and comp_score <= 2001:
            return "\nPlayer wins! \n"
        elif player_score <= 2001 and comp_score > 2001:
            return "\nComputer wins! \n"


##### TESTS
# print(score([2, 6]))
# print(get_player_input())

print(game_2001(8))

