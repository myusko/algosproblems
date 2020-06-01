import pytest

from algos.arrays.launch_sequence_checker import launch_sequence_checker


@pytest.mark.parametrize(
    'data, second_data, expected',
    [
        (
            ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"],
            [1, 10, 11, 2, 12, 111],
            True
        ),
        (
            ["stage_1", "stage_1", "stage_2", "dragon"],
            [2, 1, 12, 111],
            False
        ),
        (
            ["Falcon 9", "Falcon 9", "Falcon 9", "Falcon 9", "Falcon 9", "Falcon 9"],
            [1, 3, 5, 7, 7, 9],
            False
        )
    ]
)
def test_launch_sequence_checker(data, second_data, expected):
    assert launch_sequence_checker(data, second_data) == expected
