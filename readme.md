### Assignment 2: Search
#### Due Friday September 30, 11:59pm. 

Note: For the programming  portions of the assignment, please provide a file called submission.py that demos your code.

For the written portions, please include a Word or PDF document in your repo containing the answers.

1. (15 points) Fill in the following table. 

| Algorithm  | Time Complexity  | Space Complexity  | Complete?  | Optimal?  |
|---|---|---|---|---|
| BFS  |   |   |   |   |
| UCS  |   |   |   |   |
| DFS   |   |   |   |   |
| DLS  |   |   |   |   |
| IDS |    |   |   |   |
|A*  |    |    |   |   |

2. (15 points) Complete the probability problems embedded in the asynchronous lesson for Wednesday, Sept 21. 


2. (15 points) Search. I've provided an example class for you for solving the Fox and Chickens problem. 
  You can run this like so:
<pre>
from FoxAndChickensState import FoxAndChickensState
from search import BFS
f = FoxAndChickensState()
g = BFS(f)
g
fox: right chicken: right grain: right boat: right
</pre>

Using the FoxAndChickensState as an example, create an WaterJugPuzzleState, with isGoal, successor, 
and any other helper functions you think are necessary. 

Recall that the problem has three jugs - one that can hold 8 liters, one that can hold 5 liters, 
and one that can hold 3 liters. We can fill any of the jugs, pour the contents of one jug into another, or dump a jug out.

You should be able to specify a start state (such as 0,0,0) and a goal state (such as (4,4,0).

 Test it with the included BFS implementation.
   
4. (10 points) Add a closed list to the BFS function.

5. (15 points) Using the BFS function as a template, implement DFS, depth-limited search,
and iterative deepening search.
   
6. (20 points) Implement A* for the FoxAndChickens problem, using the number of misplaced items as a heuristic. For example, if you had f=left, c=left, g=left, b=right, h=3, since there 
are three items on the wrong side. 

You will probably want to use the heapq module for your priority queue.

7. (10 points). I've provided a TicTacToeState class. Using this, complete the implementation of the minimax algorithm for two-player search. Add a wrapper around this that allows a person to play tic-tac-toe against the computer. 

It should alternatively prompt the player for a move and then use minimax to  find the best response.

8. (graduate students only). 
In the late 90s, Deep Blue shocked the world by becoming the first computer to beat a human grandmaster, Garry Kasparov.
   [This paper](https://pdf.sciencedirectassets.com/271585/1-s2.0-S0004370200X00847/1-s2.0-S0004370201001291/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLWVhc3QtMSJHMEUCIQCHv6f1SKION447Zy%2B%2Fjj7ZZK51qungm5kN%2F0y2yhsurAIgE%2FbNHZZ6By25D%2BImBUVaq%2BUKDf%2B7Uqa9L8a7t9nrUa4qtAMIZBADGgwwNTkwMDM1NDY4NjUiDDBGodLKiULNC6ZDmiqRAy8Ti2ThK2XwJtoOgN0IXF%2FXgLkg18X%2FaMHYsu6qjqyrg0M4y02n1A26mGFxoJwg1%2Fg0Ls5lZiD1VoyjpQlAoYpJ9tscxkeXrAqFdG1NAY%2B7B9piqse3MvUhK3syw5E%2FM60Xh%2FrBllp4OYC2%2FzLGLHXk2cmE%2BxB0eKkGn1BQ6PRQ81g1kod5w8JHqqgwETX8hJhuc68lXyyQVgTmCf5zwoU79N4ns3rK3sUxRwdCSQjOI4FDHUB4G1gFrmMcYohopvHzhNul8R9h6CzYqJpA2WWEptxr%2FSaYcwJWoO01KFmKEdRW0uGPPEvR3ZRac3wGlZGGFVSJUmOTPxd05n%2BH2oFU3hZ2Rzis0cRIP2zGn5xuRVMA%2Fr%2F22kHUZ3ufN%2FEkBVBH4UW16jMKRB8MH2k6Bj0LuLV7G%2Bdwo%2BjvSJI6H9%2FOPuOFZkQgwf2PRNqgu7fdgu5pg%2BL%2FkrpIuBKVDy6KwZmrH0r9NrkGaCjsYMU5xwgLzsLl0ie2bEphPRgs7uT0KTaaPUESztHqyHqwPPBoTXbVMKvPtYEGOusBCxNCzDJkUlyCq0Gl7RqKSM%2BZqQN9BiC4ZAIFFTRsiGlFv7ctOeI8y98SwdwP%2FDBOb1JxTOUmMG5YVrf184WvyWrIAMYO9PbIqdXMZMyR%2B%2BHXurj0q25Ze48eUc9KIQS7Yxbmkq5A5dHYXlCXN6lMhCnH6RAiyf%2Bp6%2FHLYNO7DW6th6O9GBgbV72%2Boq1nOQAEvTJL6teDz%2Fv8ppaRiYW%2B5dMmbBbeXIBGK4hLBJml71fKDSbirx6z0JAFQS1EzO56bVlbTyIvzKGG%2BgdlI1HHSypoaqOmqa4UO09yLCluDDoG4MMC%2FMaQEpusoQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210217T194502Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYTXOLMFNW%2F20210217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a1ea154dc26b7f6bf55b78d2558066ea4c89243537c19854e4c8c0264e98e017&hash=9759e9a487197b114f2285cc3be7d68f70fddd5b5be56c5c1dd01eac3bc91a77&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0004370201001291&tid=spdf-8d7dcfe8-5cff-4e07-b20e-7d7992c76c45&sid=54f296356b581744646ab6348b72ed4150ebgxrqa&type=client)
   describes how Deep Blue was constructed - it took advantage of specialized hardware, along with hand-crafted heuristics and 
   many optimizations of the alpha-beta pruning technique we've learned about.
   
20 years later, the Google team has re-revolutionized game search with the development of AlphaZero, which is described [here](https://science.sciencemag.org/content/sci/362/6419/1140.full.pdf).

AlphaZero uses a very different approach - specifically, a deep neural network is used to learn heuristic functions through self-play. (We'll look at reinforcement learning later in the semester).
This allows the program to learn to play any game, as long as it knows the state space, how to win, and the legal actions.

These articles are both pretty dense, and I don't expect you to grasp every nuance, but you should be able to read the introductions and get the gist of things.

a) What were the engineering advances that led to Deep Blue's success? Which of them can be transferred to other problems, and which are specific to chess?

b) AlphaZero is compared to a number of modern game-playing programs, such as StockFish, which work similarly to Deep Blue. The Science paper shows that AlphaZero is able to defeat StockFish even when it is given only 1/100 of the computing time. Why is that? Please frame your answer in terms of search and the number of nodes evaluated.
