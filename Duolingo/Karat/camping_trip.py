'''
You are going on a camping trip.
You and your friends are planning the hike to your campsite but there are various attractions you would like to 
see along the way. You are trying to plan a route where you can see all of your desired attractions without walking 
the same trail twice.
Trails are listed by the attractions they connect, all trails are 2-way trails and there can be multiple trails 
between 2 places.
Given a list of trails and a list of desired attractions, return whether there is a path which starts at the 
Parking Lot and ends at the Campsite which visits all of the desired attractions without using the same trail twice.
============================ ===================================
Examples:
===============================================================
Liberty Lake Frozen Ocean Eel Weir
|            |        |    |      |
Parking Lot------Beaver Dam----Campsite
trails1 = [
    ["Beaver Dam",  "Frozen Ocean"], # First trail between Beaver Dam/Frozen Ocean
    ["Beaver Dam",  "Frozen Ocean"], # Second trail between Beaver Dam/Frozen Ocean
    ["Parking Lot", "Beaver Dam"],
    ["Parking Lot", "Liberty Lake"],
    ["Beaver Dam",  "Campsite"],
    ["Eel Weir",  "Campsite"],
    ["Eel Weir",  "Campsite"],
]
attractions1_1 = ["Frozen Ocean"] => True
Path: Parking Lot->Beaver Dam->Frozen Ocean->Beaver Dam->Campsite

attractions1_2 = ["Liberty Lake", "Beaver Dam"] => False
It is not possible to return from Liberty Lake so this path is not possible.

attractions1_3 = ["Eel Weir"] => True
Path: Parking Lot->Beaver Dam->Campsite->Eel Weir->Campsite
--------------------------------------------
                Liberty Lake
                |    |    |
Jeremy's Bay--Mason's Cabin--Parking Lot
      |                        |     
    Horseshoe Falls----Mills Falls----Eel Weir--Outdoor Theater--Campsite
                                             \                   /
                                              --Hardwood Forest--
trails2 = [
    ["Mason's Cabin", "Liberty Lake"],
    ["Parking Lot", "Mill Falls"],
    ["Mason's Cabin", "Jeremy's Bay"],
    ["Eel Weir", "Hardwood Forest"],
    ["Outdoor Theater", "Campsite"],
    ["Jeremy's Bay", "Horseshoe Falls"],
    ["Mason's Cabin", "Parking Lot"],
    ["Mason's Cabin", "Liberty Lake"],
    ["Mill Falls", "Horseshoe Falls"],
    ["Mill Falls", "Eel Weir"],
    ["Hardwood Forest", "Campsite"],
    ["Eel Weir", "Outdoor Theater"],
    ["Liberty Lake", "Mason's Cabin"]
]
attractions2_1 = ["Jeremy's Bay", "Mason's Cabin", "Outdoor Theater"] #=> True
attractions2_2 = ["Outdoor Theater", "Eel Weir", "Hardwood Forest"] #=> False
attractions2_3 = ["Liberty Lake"] #=> True
attractions2_4 = ["Horseshoe Falls", "Eel Weir"] #=> True
All Test Cases:
sightseeing(trails1, attractions1_1) => True
sightseeing(trails1, attractions1_2) => False
sightseeing(trails1, attractions1_3) => True
sightseeing(trails2, attractions2_1) => True
sightseeing(trails2, attractions2_2) => False
sightseeing(trails2, attractions2_3) => True
sightseeing(trails2, attractions2_4) => True
Complexity Variable:
n = number of trails
'''

def sightseeing(trails, attractions):
    from collections import defaultdict, deque

    # Build graph with trails count to manage multiple trails between two nodes
    graph = defaultdict(lambda: defaultdict(int))
    for a, b in trails:
        graph[a][b] += 1
        graph[b][a] += 1  # because trails are 2-way

    # Helper function for DFS
    def dfs(current, visited_trails, visited_attractions):
        # If current is Campsite and all attractions are visited, return True
        if current == "Campsite" and all(attr in visited_attractions for attr in attractions):
            return True
        # Explore neighbors
        for neighbor in graph[current]:
            for _ in range(graph[current][neighbor]):
                if (current, neighbor, _) not in visited_trails:
                    visited_trails.add((current, neighbor, _))
                    visited_trails.add((neighbor, current, _))  # Since trails are bidirectional
                    visited_attractions.add(neighbor)
                    if dfs(neighbor, visited_trails, visited_attractions):
                        return True
                    visited_trails.remove((current, neighbor, _))
                    visited_trails.remove((neighbor, current, _))
                    visited_attractions.discard(neighbor)
        return False

    # Initial DFS from Parking Lot
    visited_trails = set()
    visited_attractions = set("Parking Lot")
    return dfs("Parking Lot", visited_trails, visited_attractions)

# Example usage
trails1 = [
    ["Beaver Dam", "Frozen Ocean"], ["Beaver Dam", "Frozen Ocean"],
    ["Parking Lot", "Beaver Dam"], ["Parking Lot", "Liberty Lake"],
    ["Beaver Dam", "Campsite"], ["Eel Weir", "Campsite"], ["Eel Weir", "Campsite"]
]
attractions1_1 = ["Frozen Ocean"]
attractions1_2 = ["Liberty Lake", "Beaver Dam"]
attractions1_3 = ["Eel Weir"]

print(sightseeing(trails1, attractions1_1))  # Should return True
print(sightseeing(trails1, attractions1_2))  # Should return False
print(sightseeing(trails1, attractions1_3))  # Should return True
