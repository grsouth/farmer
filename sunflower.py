import utils

sunflower_location = (0,0)
# bottom right corner of the 2x6 sunflower patch

def plant_twobysix():

  utils.goto(sunflower_location[0], sunflower_location[1])

  for i in range(6):
    if get_ground_type() != Grounds.Soil:
      till()
    plant(Entities.Sunflower)
    if get_water() < 1:
      use_item(Items.Water)
    if i < 5:
      move(North)
  
  move(East)

  for i in range(6):
    if get_ground_type() != Grounds.Soil:
      till()
    plant(Entities.Sunflower)
    if get_water() < 1:
      use_item(Items.Water)
    if i < 5:
      move(South)

def measure_twobysix():

  utils.goto(sunflower_location[0], sunflower_location[1])

  biggest_sunflower = (-1, -1, -1)

  for i in range(6):

    size = measure()
    if get_water() < 1:
      use_item(Items.Water)
    if size > biggest_sunflower[0]:
      biggest_sunflower = (size, get_pos_x(), get_pos_y())
      
    if i < 5:
      move(North)
  
  move(East)

  for i in range(6):

    size = measure()
    if get_water() < 1:
      use_item(Items.Water)
    if size > biggest_sunflower[0]:
      biggest_sunflower = (size, get_pos_x(), get_pos_y())
      
    if i < 5:
      move(South)

  return biggest_sunflower

def harvest_biggest():
  # Harvest and replant until power is topped off.
  while num_items(Items.Power) <= 100:
    biggest = measure_twobysix()
    utils.goto(biggest[1], biggest[2])
    if can_harvest():
      harvest()
      plant(Entities.Sunflower)
      if get_water() < 1:
        use_item(Items.Water)
