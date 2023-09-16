def is_valid(x, y, N, M):
    return 1 <= x <= N and 1 <= y <= M


def solve(N, M, garden, queen_x, queen_y, L, musketeers):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    time_limit = L + 1

    queue = [(queen_x, queen_y, 0)]
    visited.add((queen_x, queen_y))

    total_pendants = 0

    while queue:
        x, y, time = queue.pop(0)

        if time > time_limit:
            break

        if (x, y) in musketeers:
            total_pendants += musketeers[(x, y)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y, N, M) and garden[new_x - 1][new_y - 1] == '0' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, time + 1))

    return total_pendants


def main():
    with open("input.txt", 'r') as f:
        N, M = map(int, f.readline().split())
        garden = [f.readline().strip() for _ in range(N)]
        queen_x, queen_y, L = map(int, f.readline().split())
        musketeers = {}

        for _ in range(4):
            x, y, pendants = map(int, f.readline().split())
            musketeers[(x, y)] = pendants

    result = solve(N, M, garden, queen_x, queen_y, L, musketeers)

    with open("output.txt", 'w') as f:
        f.write(str(result))


if __name__ == '__main__':
    main()
