from collections import deque

def water_jug(capacity1, capacity2, target):

    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:

        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

    
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]

        # Possible next states
        states = []

        # Fill Jug 1
        states.append((capacity1, jug2, "Fill Jug 1"))

        # Fill Jug 2
        states.append((jug1, capacity2, "Fill Jug 2"))

        # Empty Jug 1
        states.append((0, jug2, "Empty Jug 1"))

        # Empty Jug 2
        states.append((jug1, 0, "Empty Jug 2"))

        # Pour Jug 1 -> Jug 2
        amount = min(jug1, capacity2 - jug2)
        states.append(
            (jug1 - amount, jug2 + amount, "Pour Jug 1 -> Jug 2")
        )

        # Pour Jug 2 -> Jug 1
        amount = min(jug2, capacity1 - jug1)
        states.append(
            (jug1 + amount, jug2 - amount, "Pour Jug 2 -> Jug 1")
        )

        for next_jug1, next_jug2, action in states:

            if (next_jug1, next_jug2) not in visited:
                queue.append(
                    (
                        next_jug1,
                        next_jug2,
                        path + [(action, (next_jug1, next_jug2))]
                    )
                )

    return None


result = water_jug(4, 3, 2)

if result:
    for step in result:
        print(step)
else:
    print("No solution")
