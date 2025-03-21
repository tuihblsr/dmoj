N = int(input())
pepper_names = ['Poblano', 'Mirasol', 'Serrano', 'Cayenne', 'Thai', 'Habanero']
pepper_shu = [1500, 6000, 15500, 40000, 75000, 125000]
SHU = 0

for i in range(N):
  P = input()
  SHU += pepper_shu[pepper_names.index(P)]

print(SHU)
