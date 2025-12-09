import utils
import pumpkin
import cactus
import sunflower

clear()
do_a_flip()

pump_1_pos = (2,0)
pump_2_pos = (14,0)
pump_3_pos = (26,0)
cactus_1_pos = (8,0)
cactus_2_pos = (20,0)

def startup():
    sunflower.plant_twobysix()
    pumpkin.plant_pumpkin_patch(pump_1_pos[0], pump_1_pos[1])
    cactus.plant_cactus_patch(cactus_1_pos[0], cactus_1_pos[1])
    pumpkin.plant_pumpkin_patch(pump_2_pos[0], pump_2_pos[1])
    cactus.plant_cactus_patch(cactus_2_pos[0], cactus_2_pos[1])
    pumpkin.plant_pumpkin_patch(pump_3_pos[0], pump_3_pos[1])
    
startup()

while True:
    if num_items(Items.Power) < 100:
        sunflower.harvest_biggest()
        
    pumpkin.check_pumpkin_patch(pump_1_pos[0], pump_1_pos[1])
    pumpkin.plant_pumpkin_patch(pump_1_pos[0], pump_1_pos[1])

    cactus.bubble_sort_cactus_patch(cactus_1_pos[0], cactus_1_pos[1])

    pumpkin.check_pumpkin_patch(pump_2_pos[0], pump_2_pos[1])
    pumpkin.plant_pumpkin_patch(pump_2_pos[0], pump_2_pos[1])
    
    cactus.bubble_sort_cactus_patch(cactus_2_pos[0], cactus_2_pos[1])

    pumpkin.check_pumpkin_patch(pump_3_pos[0], pump_3_pos[1])
    pumpkin.plant_pumpkin_patch(pump_3_pos[0], pump_3_pos[1])
    
    utils.goto(31,6)
    for i in range(32):
        if can_harvest():
            harvest()
        if i < 31:
            move(West)

    # Carrot row just above, moving East.
    utils.goto(0,7)
    for i in range(32):
        if can_harvest():
            harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Carrot)
        if i < 31:
            move(East)
    
    # Grass/tree checkerboard row moving West.
    utils.goto(31,8)
    for i in range(32):
        is_tree = ((get_pos_x() + get_pos_y()) % 2) == 0
        if can_harvest():
            harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        current_entity = get_entity_type()
        if is_tree:
            if current_entity != Entities.Tree:
                plant(Entities.Tree)
        else:
            if current_entity != Entities.Grass:
                plant(Entities.Grass)
        if i < 31:
            move(West)

    # Alternate checkerboard row moving East.
    utils.goto(0,9)
    for i in range(32):
        is_tree = ((get_pos_x() + get_pos_y()) % 2) == 0
        if can_harvest():
            harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        current_entity = get_entity_type()
        if is_tree:
            if current_entity != Entities.Tree:
                plant(Entities.Tree)
        else:
            if current_entity != Entities.Grass:
                plant(Entities.Grass)
        if i < 31:
            move(East)

    # Grass/tree checkerboard row moving West.
    utils.goto(31,10)
    for i in range(32):
        is_tree = ((get_pos_x() + get_pos_y()) % 2) == 0
        if can_harvest():
            harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        current_entity = get_entity_type()
        if is_tree:
            if current_entity != Entities.Tree:
                plant(Entities.Tree)
        else:
            if current_entity != Entities.Grass:
                plant(Entities.Grass)
        if i < 31:
            move(West)
