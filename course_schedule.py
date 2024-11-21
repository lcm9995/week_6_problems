class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        numOfPreqs = [0]*numCourses
        graph = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[p].append(c)
            numOfPreqs[c]+=1
        queue = []
        for i in range(numCourses):
            if numOfPreqs[i]==0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                numOfPreqs[neighbor] -=1
                if numOfPreqs[neighbor] ==0:
                    queue.append(neighbor)
        if len(order) == numCourses:
            return order
        else:
            return []