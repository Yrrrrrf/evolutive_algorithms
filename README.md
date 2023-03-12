<h1 align="center">
    <img src="resources/img/puzzle.png" alt="Digital Strategy" width="200">
    <div align="center">Evolutive Algorithms</div>
</h1>

## Abstract

This is a implementation of some of the most used [Search Algorithms](./reports/00_main_report.ipynb) to solve the Eight Puzzle Problem.

The main goal of this project is to compare the performance of the algorithms and to understand the differences between them.

NOTE: The project is still in development and the algorithms had been tested in the **eight puzzle problem** (the algorithms will be tested in other problems in the future).


## Contents

The contents are deeply explained in the [main report](/reports/00_main_report.ipynb).


## Setup

- First make sure you have the latest pip installed: `python -m pip install --upgrade pip`
- Use `pip install -r requirements.txt` to install the dependencies.
- Also you can use `.\.venv\Scripts\activate` to activate the virtual environment that contains all the dependencies.

Use these commands to run the project:
```python
py src/main.py  # run main.py
```

## Directory Structure

```bash
project_name/  # root directory
│   .gitignore
│   LICENSE.md  # https://choosealicense.com/
│   README.md  # this file
│   requirements.txt  # pip freeze > requirements.txt
├───reports/  # jupyter notebooks (exploratory analysis, etc.)
├───resources/  # resources (images, data, etc.)
│   └───img/  # images
│   └───attritions.md  # attritions (images, data, etc.)
└───src/  # source files
    ├───components/  # components
    ├───config/  # config files
    └───main.py  # main entry point
```

## License

This project is licensed under the terms of the [MIT License](LICENSE.md).
