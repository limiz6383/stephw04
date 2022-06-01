from importlib.resources import path
from nturl2path import pathname2url
from tkinter import E
from collections import deque
import collections
from unittest import skip

def find_id(pages, word):
    for k, v in pages.items():
        if v == word:
            return k

def covertpath(paths, pages):
    #convert id back to page names and print the path
    for i in paths:
        for j in i:
            pages.get(j)



def dfs(graph, pages, start, target):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == target:
                return path
            if vertex not in graph:
                (vertex,path) = stack.pop()
            visited.add(vertex)
            for children in graph[vertex]:
                stack.append((children, path + [children]))

def bfs(graph, pages, start, target):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex not in visited:
            if vertex == target:
                return path
            if vertex not in graph:
                path = queue.pop(0)
                vertex = path[-1]
            visited.add(vertex)
            for children in graph[vertex]:
                queue.append(path + [children])
  
        
    

#dfs
def main():
    pages = {}
    links = {}
    with open('pages_small.txt') as f:
        for data in f.read().splitlines():
            page = data.split('\t')
        # page[0]: id, page[1]: title
            pages[page[0]] = page[1]

    with open('links_small.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
        # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}   
    
    return dfs(links, pages, find_id(pages, 'Google'), find_id(pages, 'Android'))

    

    # for k, v in pages.items():
    #     if v == 'Google':
    #         print('Google', k)

    
if __name__ == '__main__':
    main()
    

print(main())

#bfs
def main2():
    pages = {}
    links = {}
    with open('pages_small.txt') as f:
        for data in f.read().splitlines():
            page = data.split('\t')
        # page[0]: id, page[1]: title
            pages[page[0]] = page[1]

    with open('links_small.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
        # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}   
    
    return bfs(links, pages, find_id(pages, 'Google'), find_id(pages, 'Android'))

print(main2())



