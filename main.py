import copy
from collections import deque

# Definición de estados objetivo
goal_state = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

def apply_moves(state, moves):
    current_state = state
    for move in moves:
        if move == 'UP':
            current_state = move_up(current_state)
        elif move == 'DOWN':
            current_state = move_down(current_state)
        elif move == 'LEFT':
            current_state = move_left(current_state)
        elif move == 'RIGHT':
            current_state = move_right(current_state)
    return current_state

# Función para imprimir el estado del tablero
def print_state(state):
    for row in state:
        print(row)

# Función para encontrar la posición del 0 en el tablero
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Función para mover el espacio en blanco hacia arriba
def move_up(state):
    i, j = find_blank(state)
    if i > 0:
        new_state = copy.deepcopy(state)
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        return new_state
    else:
        return None

# Función para mover el espacio en blanco hacia abajo
def move_down(state):
    i, j = find_blank(state)
    if i < 2:
        new_state = copy.deepcopy(state)
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        return new_state
    else:
        return None

# Función para mover el espacio en blanco hacia la izquierda
def move_left(state):
    i, j = find_blank(state)
    if j > 0:
        new_state = copy.deepcopy(state)
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        return new_state
    else:
        return None

# Función para mover el espacio en blanco hacia la derecha
def move_right(state):
    i, j = find_blank(state)
    if j < 2:
        new_state = copy.deepcopy(state)
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        return new_state
    else:
        return None

# Función para comprobar si el estado actual es igual al estado objetivo
def is_goal(state):
    return state == goal_state

# Búsqueda en amplitud (BFS)
def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        visited.add(str(state))

        if is_goal(state):
            return path

        for move_func, move_name in [(move_up, "UP"), (move_down, "DOWN"), (move_left, "LEFT"), (move_right, "RIGHT")]:
            new_state = move_func(state)
            if new_state is not None and str(new_state) not in visited:
                queue.append((new_state, path + [move_name]))

    return None

# Búsqueda en profundidad (DFS)
def dfs(initial_state, max_depth=90):
    visited = set()
    stack = [(initial_state, [])]

    while stack:
        state, path = stack.pop()
        visited.add(str(state))

        if is_goal(state):
            return path

        if len(path) < max_depth:
            for move_func, move_name in [(move_up, "UP"), (move_down, "DOWN"), (move_left, "LEFT"), (move_right, "RIGHT")]:
                new_state = move_func(state)
                if new_state is not None and str(new_state) not in visited:
                    stack.append((new_state, path + [move_name]))

    return None
    
if __name__ == "__main__":
    import random

    # Genera un estado inicial aleatorio
    initial_state = goal_state.copy()
    for _ in range(100):
        move_functions = [move_up, move_down, move_left, move_right]
        random.shuffle(move_functions)
        for move_func in move_functions:
            new_state = move_func(initial_state)
            if new_state is not None:
                initial_state = new_state
                break

    print("Estado inicial:")
    print_state(initial_state)

    print("\nResolviendo con BFS:")
    bfs_solution = bfs(initial_state)
    if bfs_solution is not None:
        print("Solución encontrada en {} movimientos:".format(len(bfs_solution)))
        print(bfs_solution)
        final_state = apply_moves(initial_state, bfs_solution)
        print("Estado final:")
        print_state(final_state)
    else:
        print("No se encontró solución con BFS.")

    print("\nResolviendo con DFS:")
    dfs_solution = dfs(initial_state)
    if dfs_solution is not None:
        print("Solución encontrada en {} movimientos:".format(len(dfs_solution)))
        print(dfs_solution)
        final_state = apply_moves(initial_state, dfs_solution)
        print("Estado final:")
        print_state(final_state)
    else:
        print("No se encontró solución con DFS.")
