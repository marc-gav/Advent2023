import utils
from pprint import pprint as pp
from collections import defaultdict


def merge_dicts(dicts_list):
    merged_dict = defaultdict(list)

    for d in dicts_list:
        for key, value in d.items():
            merged_dict[key].append(value)

    return dict(merged_dict)

def pre_process(day_input):
    processed_day = []
    for game in day_input:
        current_game_stats = []
        start_pos = game.find(":") + 2
        rounds = game[start_pos:].split("; ")
        for round in rounds:
            stats = {}
            rolls = round.split(", ")
            for roll in rolls:
                number, color = roll.split(" ")
                stats[color] = int(number)
            
            current_game_stats.append(stats)
        
        processed_day.append(current_game_stats)
    
    return processed_day
                
def check_roll_validity(roll_dict):
    return all([roll_val <= constraints[roll_color] for roll_color, roll_val in roll_dict.items()])

def get_game_power(rolls_dicts):
    merged_dict = merge_dicts(rolls_dicts)
    return max(merged_dict["red"]) * max(merged_dict["blue"]) * max(merged_dict["green"])

def problem1(day_input):
    return sum([game_num + 1 for game_num, rolls in enumerate(day_input) if all([check_roll_validity(roll) for roll in rolls])])

def problem2(day_input):
    return sum([get_game_power(game) for game in day_input])

if __name__ == "__main__":
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    day_input = utils.read_day("input2.txt")
    processed_game = pre_process(day_input)
    print(problem1(processed_game))
    print(problem2(processed_game))
