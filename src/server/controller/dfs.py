import osmnx as ox
import sys
import GraphUtils as gu

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


def dfs(G, src, dest):
    @static_vars(min_dis = sys.maxsize, path = [])
    def dfs_util(graph, current, dis, goal, currentpath, visited):
        if current == goal:
            if dis > dfs_util.min_dis:
                return dfs_util.path
            else:
                dfs_util.min_dis = dis
                currentpath.append(current)
                dfs_util.path = currentpath
                # print ("This path length: ",dis)
                # print ("path found")
                return dfs_util.path
        if dis > dfs_util.min_dis:
            return dfs_util.path
        for u, nextnode, data in graph.edges(current, data=True):
            if nextnode in visited:
                continue
            cost_dis = dis + gu.getDistance(graph, current, nextnode)
            dfs_util(graph, nextnode, cost_dis, goal, currentpath + [current], visited + [nextnode])
        return dfs_util.path
    path = dfs_util(G, src, 0, dest,[], [])
    return path
