def current_beat():
    while True:
        yield from (1, 2, 3, 4)
    # curr = 0
    # beats = [1, 2, 3, 4]
    # while True:
    #     yield beats[curr]
    #     curr = curr + 1 if not curr == 3 else 0


beat = current_beat()
for _ in range(10):
    print(next(beat))
