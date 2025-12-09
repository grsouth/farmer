
def check_pumpkin_patch():
	# starting from the bottom left corner
	
	id_1 = measure()
	for i in range(5):
		move(North)
		move(East)
	id_2 = measure()
	
	if (id_1 == id_2) and (id_2 != None):
		return True
	else:
		return False

def plant_pumpkin_patch():
	backwards = False
	for i in range(6):
		for j in range(6):
			
			if get_ground_type() != Grounds.Soil:
				till()
			
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)

			if j < 5:
				if backwards:
					move(East)
				else:
					move(West)

		backwards = not backwards
		if i < 5:
			move(South)

			