from heapq import heapify, heappush, heappop

class nodeObj:

    def __init__(self, key ,nodeNum, aCost, tCost, prevObj = None):
        self.key = key
        self.nodeNum = nodeNum
        self.aCost = aCost
        self.tCost = tCost
        if prevObj is None:
            self.prevObj = []
        else:
            self.prevObj = nodeObj

    def __str__(self):
        return f'{self.nodeNum} - {self.aCost} - {self.tcost} - {self.nodeObj}'

    def __lt__(self, other):
        return self.tCost <= other.tCost



if __name__ == '__main__':

    graphNode = {
        0: "S",
        1: "A",
        2: "B",
        3: "C",
        4: "D"
    }

    x = list(graphNode.keys())


    adj = [
           [-1, 1, 4, -1, -1],
           [-1, -1, 2, 5, 12],
           [-1, -1, -1, 2, -1],
           [-1, -1, -1, -1, 3],
           [-1, -1, -1, -1, -1],
           ]
    h = [7, 6, 2, 1, 0]

    start = nodeObj(0, graphNode[0], 0, 0+h[0], None)
    end = "D"

    minQueue = []
    heapify(minQueue)

    heappush(minQueue, start)
    while minQueue:
        pop = heappop(minQueue)

        print(pop.nodeNum)


        if pop.nodeNum == end:
            print("Total cost is ", pop.aCost)
            nodes = pop.prevObj
            if(nodes == None):
               print(pop.nodeNum)

            # print(nodes.nodeNum)
            nodes = pop.prevObj


        for i in range(0, len(adj[x[pop.key]])):

            if (adj[x[pop.key]][i] > -1):
                key = i
                nodenum = graphNode[i]
                aCost = pop.aCost + adj[x[pop.key]][i]
                tCost = pop.aCost + h[i]
                new = nodeObj(key, nodenum, aCost, tCost, prevObj=pop)
                heappush(minQueue, new)
    print("there is no path ")

