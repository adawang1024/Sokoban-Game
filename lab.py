
# import json
# import typing

# NO ADDITIONAL IMPORTS!


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}

directions = ["up", "down", "left", "right"]


def new_game(level_description):
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions.
    """
    result = {}
    result["width"] = len(level_description[0])
    result["height"] = len(level_description)
    result["wall"] = set()
    result["computer"] = set()
    result["target"] = set()

    for i, value in enumerate(level_description):
        row = value
        for j, value in enumerate(row):
            if value != []:
                if "wall" in value:
                    result["wall"].add(
                        (i, j),
                    )
                if "computer" in row[j]:
                    result["computer"].add(
                        (i, j),
                    )
                if "target" in row[j]:
                    result["target"].add(
                        (i, j),
                    )
                if "player" in row[j]:
                    result["player"] = (i, j)

    return result


def victory_check(game):
    """
    Given a game representation (of the form returned from new_game), return
    a Boolean: True if the given game satisfies the victory condition, and
    False otherwise.
    """
    if len(game["target"]) == 0:
        return False
    return game["computer"] == game["target"]


def move(loc, direction):
    new_loc = tuple(x + dx for x, dx in zip(loc, direction_vector[direction]))
    return new_loc


def step_game(game, direction):
    """
    Given a game representation (of the form returned from new_game), return a
    new game representation (of that same form), representing the updated game
    after running one step of the game.  The user's input is given by
    direction, which is one of the following: {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    new_loc = move(game["player"], direction)
    new_board = {}
    for key, value in game.items():
        if isinstance(value, (int, tuple)):
            new_board[key] = value
        else:
            new_board[key] = value.copy()
    if 0 <= new_loc[0] < game["height"] and 0 <= new_loc[1] < game["width"]:
        if new_loc in game["wall"]:
            return new_board
        if new_loc in game["computer"]:
            next_computer_loc = move(new_loc, direction)
            if (next_computer_loc not in game["wall"]) and (
                next_computer_loc not in game["computer"]
            ):
                new_board["computer"].remove(new_loc)
                new_board["computer"].update((next_computer_loc,))
                new_board["player"] = new_loc
            else:
                return new_board

        new_board["player"] = new_loc

    return new_board


def dump_game(game):
    """
    Given a game representation (of the form returned from new_game), convert
    it back into a level description that would be a suitable input to new_game
    (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """

    result = [[[] for _ in range(game["width"])] for _ in range(game["height"])]
    for i, j in game["computer"]:
        result[i][j].append("computer")
    for i, j in game["target"]:
        result[i][j].append("target")
    for i, j in game["wall"]:
        result[i][j].append("wall")
    result[game["player"][0]][game["player"][1]].append("player")

    return result


def get_neighbor(state):
    """
    Given a state of game representation (of the form returned from new game),
    returns a list of games(dict) that can be obtained by movements in
    the four directions: "up", "down", "left", "right"
    """

    neighbors = []
    for direction in ["up", "down", "left", "right"]:
        # print("b",state)
        neighbor = step_game(state, direction)
        neighbors.append(neighbor)
    return neighbors


def solve_puzzle(game):
    """
    Given a game representation (of the form returned from new game), find a
    solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """

    # if victory_check(game):
    #     return []

    # agenda = [((game,),())]
    # start = from_dict_to_tuple(game)
    # visited = {start}

    # while agenda:
    #     print("agenda", agenda)
    #     current = agenda.pop(0) # current: dictionary

    #     terminal_state = current[0][-1] #index in the dictionary
    #     neighbors = get_neighbor(terminal_state) #input has to be a dictionary
    #     for i in range(4):
    #         neighbor = from_dict_to_tuple(neighbors[i])
    #         if neighbor not in visited:
    #             new_path = (current[0] + (neighbors[i],), current[1]+(directions[i],))
    #             if victory_check(neighbors[i]):

    #                 return  new_path[1]# return a list of board states

    #             visited.add(neighbor)
    #             agenda.append(new_path)

    # return None

    if victory_check(game):
        return []

    agenda = [((game,), ())]
    # ((game,),())
    # (game,)
    start = from_dict_to_tuple(game)
    visited = {start}

    while agenda:
        current = agenda.pop(0)  # current: dictionary
        terminal_state = current[0]  # index in the dictionary
        neighbors = get_neighbor(terminal_state[0])  # input has to be a dictionary
        for i in range(4):
            neighbor = from_dict_to_tuple(neighbors[i])
            if neighbor not in visited:
                new_path = ((neighbors[i],), current[1] + (directions[i],))
                if victory_check(neighbors[i]):
                    return new_path[1]  # return a list of board states

                visited.add(neighbor)
                agenda.append(new_path)

    return None


def from_dict_to_tuple(state):
    """
    Given a state of game representation (of the form returned from new game),
    transforms it to a tuple containing the positions of computer as a frozen
    set and the position of computer as a tuple.

    """
    transformed = (frozenset(state["computer"]), state["player"])
    return transformed


if __name__ == "__main__":
    # test = [
    #     [[], ["wall"], ["player"]],
    #     [["target"], ["computer"], []],
    #     [[], [], []],
    # ]
    # print(test)
    # result = new_game(test)
    # print(result)

    # neighbors = get_neighbor(result)
    # print(neighbors[0])

    # result2 = victory_check(result)
    # print (result2)

    # result3 = step_game(result, "down")
    # print(result3)

    # loc = (1,1)
    # new = move(loc, "up")
    # print(new)

    # a = dump_game(result)
    # print(len(result))
    # print(a)

    # result3 = solve_puzzle(result)
    # print(result3)

    pass
