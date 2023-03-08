<h1 align="center">
    <img src="resources/img/puzzle.png" alt="Digital Strategy" width="200">
    <div align="center">Eight Puzzle </div>
</h1>


## Setup

- First make sure you have the latest pip installed: `python -m pip install --upgrade pip`
- Use `pip install -r requirements.txt` to install the dependencies. Also you can use `.\.venv\Scripts\activate` to activate the virtual environment that contains all the dependencies.

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
├───data/  # data files (not to be committed to git)
│   ├───raw/  # raw data files
│   └───processed/  # processed data files
├───src/  # source files
│   ├───config/  # config files
│   └───main.py  # main entry point
├───notebooks/  # jupyter notebooks (exploratory analysis, etc.)
├───reports/  # reports (final reports, presentations, etc.)
├───tests/  # tests (unit, functional, etc.)
```


## License

This project is licensed under the terms of the [MIT License](LICENSE.md).
