"""
The master launch sequence consists of several independent sequences for different systems.
Your goal is to verify that all the individual system sequences are in strictly increasing order.
In other words, for any two elements i and j (i < j) of the master launch sequence
that belong to the same system (having systemNames[i] = systemNames[j]), their values should be in
strictly increasing order (i.e. stepNumbers[i] < stepNumbers[j]).

Examples:
     Input: ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"], [1, 10, 11, 2, 12, 111],
     Output: true
"""
from collections import defaultdict


def launch_sequence_checker(system_names, step_numbers):
    pairs = defaultdict(int)

    for i in range(len(system_names)):
        if pairs[system_names[i]] < step_numbers[i]:
            pairs[system_names[i]] = step_numbers[i]
        else:
            return False
    return True
