class Solution(object):

    def percorrer(self, equations, values, previous, query):
        if query[0] == query[1]:
            return 1
        print(query)
        
        for i, eq in enumerate(equations):
            print("eq", eq)
            if eq[0] in previous:
                continue
            previous.update([eq[0]])
            print(query[0], eq[0])
            if query[0] == eq[0]:
                res = self.percorrer(equations, values, set([eq[0]]), [eq[1], query[1]])
                if res != -1:
                    return values[i] * res
            #print("if2", query[0], eq[1])
            if query[0] == eq[1]:
                #print("b")
                res = self.percorrer(equations, values, set([eq[0]]), [eq[0], query[1]])
                if res != -1:
                    return 1/values[i] * res
        return -1

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        results = []

        nodes = set()
        for eq in equations:
            nodes.update(eq)

        for query in queries:
            print('-------------------')
            if query[0] not in nodes or query[1] not in nodes:
                results.append(-1)
                continue
            previous = set()
            results.append(self.percorrer(equations, values, previous, query))
        
        return results
            
        