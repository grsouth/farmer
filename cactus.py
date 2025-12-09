import utils


def plant_cactus_patch(x, y):
    utils.goto(x, y)

    backwards = False
    for i in range(6):
        for j in range(6):

            if get_ground_type() != Grounds.Soil:
                till()

            if get_entity_type() != Entities.Cactus:
                plant(Entities.Cactus)

            if j < 5:
                if backwards:
                    move(West)
                else:
                    move(East)

        backwards = not backwards
        if i < 5:
            move(North)


def bubble_sort_cactus_patch(x, y):
    swapped = False

    # Horizontal bubble pass (serpentine rows).
    utils.goto(x, y)
    horiz = East
    for row in range(6):
        for col in range(5):
            here = measure()
            neighbor = measure(horiz)
            if (here != None) and (neighbor != None):
                if horiz == East:
                    if neighbor < here:
                        swap(horiz)
                        swapped = True
                else:  # moving West, keep west side smaller
                    if neighbor > here:
                        swap(horiz)
                        swapped = True
            move(horiz)
        if row < 5:
            move(North)
            if horiz == East:
                horiz = West
            else:
                horiz = East

    # Vertical bubble pass (serpentine columns).
    utils.goto(x, y)
    vert = North
    for col in range(6):
        for row in range(5):
            here = measure()
            neighbor = measure(vert)
            if (here != None) and (neighbor != None):
                if vert == North:
                    if neighbor < here:
                        swap(vert)
                        swapped = True
                else:  # moving South, keep south side smaller
                    if neighbor > here:
                        swap(vert)
                        swapped = True
            move(vert)
        if col < 5:
            move(East)
            if vert == North:
                vert = South
            else:
                vert = North

    # If we made no swaps, the patch was already sorted; harvest/replant if ready.
    if (not swapped) and can_harvest():
        harvest()
        plant_cactus_patch(x, y)
