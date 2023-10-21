counter = 1
rows = 0
while rows < 8:
    if rows % 2 == 0:
        if counter % 2 == 0 and counter % 8 != 0:
            print('O', end='')
            counter += 1
        elif counter % 2 != 0:
            print('X', end='')
            counter +=1
        elif counter % 8 == 0:
            print('O')
            counter = 1
            rows += 1
    else:
        if counter % 2 == 0 and counter % 8 != 0:
            print('X', end='')
            counter += 1
        elif counter % 2 != 0:
            print('O', end='')
            counter +=1
        elif counter % 8 == 0:
            print('X')
            counter = 1
            rows += 1

# version codio liked:
for row in range(8):
  if row % 2 == 0:
    for column in range(8):
      if column % 2 == 0:
        print("X", end='')
      else:
        print("O", end='')
    print()
  else:
    for column in range(8):
      if column % 2 == 0:
        print("O", end='')
      else:
        print("X", end='')
    print()