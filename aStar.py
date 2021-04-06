import Graph as graf
import fungsi as f
from queue import PriorityQueue
import file_input as fi

def h(p1,p2):
    return f.euclideanDistance(p1,p2)

def reconstructPath(cameFrom, current):
    # current sebelum while loop adalah end Of path/goal
    # akan dilakukan backtracking
    totalPath = [current]
    while current in cameFrom:
        current = cameFrom[current]
        totalPath = [current] + totalPath
    return totalPath

def aStar(g, start, goal):
    numOfNode = g.getNumOfNode()

    count = 0

    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}

    gScore = [float("inf") for j in range(numOfNode)]
    gScore[start] = 0

    fScore = [float("inf") for j in range(numOfNode)]
    fScore[start] = h(g.getNodeCoordinate(start),g.getNodeCoordinate(goal))

    openSetHash = {start} # nantinya untuk mengetahui apakah suatu node/neighbor sudah ada di openList

    while (not openSet.empty()):
        current = openSet.get()[2]
        openSetHash.remove(current)
        
        if(current == goal):
            return reconstructPath(cameFrom, current)
        
        for neighbor in g.getNeighbors(current):
            temp_gScore = gScore[current] + f.euclideanDistance(g.getNodeCoordinate(current), g.getNodeCoordinate(neighbor))
            if(temp_gScore < gScore[neighbor]):
                cameFrom[neighbor] = current
                gScore[neighbor] = temp_gScore
                fScore[neighbor] = temp_gScore + h(g.getNodeCoordinate(neighbor), g.getNodeCoordinate(goal))
                if (neighbor not in openSetHash):
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    
    return -1


