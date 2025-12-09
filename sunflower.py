def plant_twobysix():

  for i in range(6):
    if get_ground_type() != Grounds.Soil:
      till()
    plant(Entities.Sunflower)
    if i < 5:
      move(North)
  
  move(East)

  for i in range(6):
    if get_ground_type() != Grounds.Soil:
      till()
    plant(Entities.Sunflower)
    if i < 5:
      move(South)

def measure_twobysix():

  biggest_sunflower = (-1, -1, -1)

  for i in range(6):

    size = measure()
    if size > biggest_sunflower[0]:
      biggest_sunflower = (size, get_pos_x(), get_pos_y())
      
    if i < 5:
      move(North)
  
  move(East)

  for i in range(6):
    sunflowers.append((measure(), get_pos_x(), get_pos_y()))
    if i < 5:
      move(South)

  return sunflowers

def harvest_biggest_sunflower(sunflowers):
  

