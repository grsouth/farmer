import pumpkin

clear()
do_a_flip()

while True:

	if pumpkin.check_pumpkin_patch():
		harvest()
	pumpkin.plant_pumpkin_patch()
	
	move(East)
	
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_pos_y() % 2 == 0:
			plant(Entities.Tree)
		if i < get_world_size()-1:
			move(North)
	
	move(East)
	
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_pos_y() % 2 != 0:
			plant(Entities.Tree)
		if i < get_world_size()-1:
			move(South)
		
	move(East)
		
		
	if pumpkin.check_pumpkin_patch():
		harvest()
	pumpkin.plant_pumpkin_patch()
	
	move(East)
	
	for i in range(get_world_size()):
		
		if can_harvest():
			harvest()
		elif get_water() < 1:
			use_item(Items.Water)
			
		if get_ground_type() != Grounds.Soil:
			till()
			
		plant(Entities.Carrot)
		if i < get_world_size()-1:
			move(North)
	
	move(East)
	
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		elif get_water() < 1:
			use_item(Items.Water)
			
		if i < 12:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			
		else:
			if get_pos_y() % 2 != 0:
				plant(Entities.Tree)
		
		if i < get_world_size()-1:
			move(South)
		
	move(East)
	
	if pumpkin.check_pumpkin_patch():
		harvest()
	pumpkin.plant_pumpkin_patch()
	
	move(East)
		
	
	
		
		
	
		
		
