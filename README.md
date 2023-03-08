<h1 align="center">
    <img src="resources/img/puzzle.png" alt="Digital Strategy" width="200">
    <div align="center">Eight Puzzle Solver Algorithms</div>
</h1>


This is a simple implementation of the 8-puzzle game using the A* algorithm. The A* algorithm is a best-first search algorithm that uses a heuristic function to guide the search. The heuristic function used in this implementation is the Manhattan distance.

This report also contains the implementation of the most popular Search Algorithms.

## Table of Contents

- [Main Report](./reports/00_main_report.ipynb)

- [Search Algorithms](./reports/search_agorithms.ipynb)
    - [Informed Search](./reports/informed_search_algorithms.ipynb)
        This kind of search uses a heuristic function to guide the search. The heuristic function is a function that estimates the cost of the cheapest path from the current node to the goal node. The heuristic function is used to guide the search by assigning a cost to each node. The node with the lowest cost is expanded first.
        - A* Search (A*)
        - Hill Climbing Search (HCS)
        - Greedy Best-First Search (GBFS)
        - Graph Search (GS)

    - [Uninformed Search](./reports/uninformed_search_algorithms.ipynb)
        This search is guided by the order in which the nodes are expanded.
        - Breadth First Search (BFS)
        - Depth-First Search (DFS)
            - Depth-First Limited Search (DLS)
            - Depth-First Iterative Deepening Search (IDS)
        - Uniform Cost Search (UCS)

## Setup

- First make sure you have the latest pip installed: `python -m pip install --upgrade pip`
- Use `pip install -r requirements.txt` to install the dependencies.
- Also you can use `.\.venv\Scripts\activate` to activate the virtual environment that contains all the dependencies.

Use these commands to run the project:
```python
python src/main.py  # run main.py
```

## Directory Structure

```bash
project_name/  # root directory
│   .gitignore
│   LICENSE.md  # https://choosealicense.com/
│   README.md  # this file
│   requirements.txt  # pip freeze > requirements.txt
├───resources/  # resources (images, data, etc.)
│   └───img/  # images
│   └───attritions.md  # attritions (images, data, etc.)
├───src/  # source files
│   ├───components/  # components
│   ├───config/  # config files
│   └───main.py  # main entry point
├───reports/  # jupyter notebooks (exploratory analysis, etc.)
```

## License

This project is licensed under the terms of the [MIT License](LICENSE.md).
