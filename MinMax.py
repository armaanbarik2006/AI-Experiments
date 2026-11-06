def minimax(depth, node_index ,is_max,score,height):
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
             minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

scores = [3,5,2,9,69,5,23,63]
height =3

best_value = minimax(0, 0, True, scores, height)

print("The optimal value is:", best_value)
