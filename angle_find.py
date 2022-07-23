import math
ab = float(input())
bc = float(input())

ac = math.sqrt(bc**2 + ab**2)

mb = ac/2
adj = bc/2

angle = int(round(math.degrees(math.acos(adj/mb))))

y = str(angle)

print(y + u'\N{DEGREE SIGN}')


