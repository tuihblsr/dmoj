P = int(input())
C = int(input())
points = 0

points += (P*50) - (C*10)
if P > C:
  points += 500

print(points)
