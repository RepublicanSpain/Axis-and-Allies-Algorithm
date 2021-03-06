import Territories
import Units as un
import Setup as stp

def find_path(start_terr, end_terr, this_path=[], shortest_path=[]):
    """
    Takes the start territory and end territory of the path you want
    We probably want to add on to this so that we can tell it to only do a land path, only do a sea path,
         or only go through friendly territories
    Returns the shortest path between them backwards, probably most useful for its length
    """
    if len(this_path) > len(shortest_path) and len(shortest_path) != 0:
        return shortest_path
    else:
        
        this_path = this_path + [end_terr]

        if start_terr in end_terr.adj_territories():
            this_path = this_path + [start_terr]
            if len(this_path) < len(shortest_path) or len(shortest_path) == 0:
                return this_path
            else:
                return shortest_path

        valid_paths = []
        for terr in end_terr.adj_territories():
            #This if statement prevents backtracking
            if not terr in this_path and (len(this_path) < len(shortest_path) or len(shortest_path) == 0):
                #recursive call
                next_path = find_path(start_terr, terr, this_path, shortest_path)
                if len(next_path) < len(shortest_path) or len(shortest_path) == 0:
                    shortest_path = next_path
                valid_paths.append(next_path)
        
        for path in valid_paths:
            if len(path) < len(shortest_path) or len(shortest_path) == 0:
                shortest_path = path
        
        return shortest_path

def noncombat_move(unit, start_terr, end_terr):
    '''
    Takes a unit, figures out if a move is valid, then executes that move
    returns the number of areas moved by the unit
    '''
    limit = unit.get_move() - unit.get_has_moved()
    path = find_path(start_terr, end_terr)
    if len(path) - 1 <= limit:
        unit.set_has_moved(len(path) - 1)
        end_terr.add_unit(unit)
        return len(path) - 1
    else:
        return 0

def retreat(unit, terr):
    '''
    move method modified to just retreat. No restrictions on movement.
    '''
    terr.add_unit(unit)
             

def main():
    powers = stp.setup()

    #print(powers[0].territories())
    #print(powers[1].territories())
    
    #Karelia and Germany
    terr1 = powers[0].territories()[0]
    terr2 = powers[1].territories()[2]
    
    path_list = find_path(terr1, terr2)

    print(path_list)

if __name__ == "__main__":
    main()
