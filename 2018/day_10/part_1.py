from re import findall

data = [map(int, findall(r'-?\d+', i)) for i in open('data.txt').readlines()]

data = []
with open('data.txt', "r") as df:
    lines = df.readlines()
    for line in lines:
        a = list(map(int, findall(r'-?\d+', line)))
        data.append(a)

boxes = []
for sec in range(20000):
    minx, maxx, miny, maxy = 10000, 0, 10000, 0
    for x, y, vx, vy in data:
        minx = min(minx, x + sec * vx)
        maxx = max(maxx, x + sec * vx)
        miny = min(miny, y + sec * vy)
        maxy = max(maxy, y + sec * vy)
    boxes.append([maxx, minx, maxy, miny])

box = min(maxx - minx + maxy - miny for maxx, minx, maxy, miny in boxes)
for sec, (maxx, minx, maxy , miny) in enumerate(boxes):
    if box == maxx - minx + maxy - miny:
        break

grid = [[' ']*(maxx - minx + 1) for j in range(miny, maxy + 1)]
for (x, y, vx, vy) in data:
    grid[y + sec * vy - miny][x + sec * vx - minx] = '#'

for row in grid:
    print (''.join(row))

print(sec)