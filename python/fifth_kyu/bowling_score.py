def bowling_score(rolls):
    """" Compute the total score for a player's game of bowling."""
    scores = [0] * 10
    frame = 0
    ball = 1
    for b, score in enumerate(rolls):
        if frame == 10:
            break
        scores[frame] += score

        if scores[frame] == 10:
            scores[frame] += rolls[b+1]
            if ball == 1:
                scores[frame] += rolls[b + 2]
                ball = 2

        if ball == 2:
            frame += 1
            ball = 1
        else:
            ball = 2
    return sum(scores[:10])
