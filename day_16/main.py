from utils import open_file


def solution():
    values = open_file("16").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


class BeamState:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.location = f"{x},{y}"
        self.direction = direction
        self.location_direction_combo = f"{x},{y},{direction}"


def __solution_1(grid: list[str]):
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1
    tiles_energised = set[str]()
    previous_location_direction_combos = set[str]()
    queue: list[BeamState] = [BeamState(x=0, y=0, direction="R")]
    while len(queue):
        beam_state = queue.pop(0)
        tiles_energised.add(beam_state.location)
        previous_location_direction_combos.add(beam_state.location_direction_combo)
        queue.extend(
            _get_new_beam_states(
                beam_state,
                previous_location_direction_combos,
                x_max,
                y_max,
                current_grid_value=grid[beam_state.y][beam_state.x],
            )
        )

    return len(tiles_energised)


def _get_new_beam_states(
    current_beam_state: BeamState,
    previous_location_direction_combos: set[str],
    x_max: int,
    y_max: int,
    current_grid_value: str,
) -> list[BeamState]:
    new_directions = (
        [current_beam_state.direction]
        if current_grid_value == "."
        else _direction_mirror_lookup[current_beam_state.direction][current_grid_value]
    )
    new_coords = [
        direction_to_location(direction, (current_beam_state.y, current_beam_state.x))
        for direction in new_directions
    ]
    new_beam_states = [
        BeamState(
            x=new_coords[idx][1],
            y=new_coords[idx][0],
            direction=new_directions[idx],
        )
        for idx in range(0, len(new_coords))
    ]
    return [
        new_beam_state
        for new_beam_state in new_beam_states
        if not (
            _beam_has_left_grid((new_beam_state.y, new_beam_state.x), x_max, y_max)
            or new_beam_state.location_direction_combo
            in previous_location_direction_combos
        )
    ]


_direction_mirror_lookup = {
    "R": {
        "/": ["U"],
        "\\": ["D"],
        "|": ["U", "D"],
        "-": ["R"],
    },
    "L": {
        "/": ["D"],
        "\\": ["U"],
        "|": ["U", "D"],
        "-": ["L"],
    },
    "U": {
        "/": ["R"],
        "\\": ["L"],
        "|": ["U"],
        "-": ["L", "R"],
    },
    "D": {
        "/": ["L"],
        "\\": ["R"],
        "|": ["D"],
        "-": ["L", "R"],
    },
}


def direction_to_location(
    direction: str, current_coords: tuple[int, ...]
) -> tuple[int, ...]:
    (y, x) = current_coords
    match direction:
        case "R":
            return (y, x + 1)
        case "L":
            return (y, x - 1)
        case "U":
            return (y - 1, x)
        case "D":
            return (y + 1, x)
        case _:
            raise ValueError(f"Invalid direction: {direction}")


def _beam_has_left_grid(new_coords: tuple[int, ...], x_max: int, y_max: int) -> bool:
    (y, x) = new_coords
    return x < 0 or y < 0 or x > x_max or y > y_max


def __solution_2(values: list[str]):
    return None
