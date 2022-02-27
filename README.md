# Routing Pichu:
Why does the program often fail to find a solution?\
This program runs good at first glance but it fails to find solution most of the time. It is because, this program has no implementation of remembering the visited node. Once the pichu goes the the wrong path and find dead end, it backtrack. But, due to lack of implementation of visited node, it doesnot remember the path which leads to the dead end or is wrong and thus it loops around that path.
  
I have implemented this program using A* algorithm and also have discarded the nodes which are visiting.\
My heuristic function is euclidean distance. And initial state is the state whaere pichu is at it's original position.

# Arrange Pichu
I have implemented this program using BFS. I have implemented this program using few pointers and loops
