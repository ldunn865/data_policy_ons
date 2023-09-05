# cookiecutter-repo_name
 
Project contact: [*project_contact_email*](mailto:*project_contact_email*)

[![pre-commit](https://github.com/ukhsa-internal/ukhsa-project-template/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/ukhsa-internal/ukhsa-project-template/actions/workflows/pre-commit.yml)

## PURPOSE
*include a purpose for your repository*

## GUIDANCE/ GROUND RULES
1.  Store notebooks in the `notebooks` folders based on thematic labelling e.g. "Project_name", "theme_x", (...).
2.  Within a thematic folder, only notebooks should be stored and they should be named as per the convention above.
3.  Notebooks should be cleared of output before committing. This is enforced by default on Dash with checks using pre-commit and github actions. (Further details below)
4.  No data, output or blob files (.DOC, .XLS, .PDF, .HTML, .PNG, .JPEG or .SVG) should ever enter the repository.
5.  Any raw or intermediate data files created should be stored in the `data` folder. No CSV/RDS/JSON/favourite_data_format in any folder aside `data`. 
6.  All outputs (e.g images containing graphs etc) should be stored into the `outputs` folder or preferable written to *S3*.
7.  The default location for outputs or objects (images, models etc) that need to be persisted and shared is *S3*.
8.  All `.py` or `.R` files should be stored in `src`.
9.  Pytest is the preferred test framework.  All tests should be stored in the tests folder and contained in files beginning `test_XXX.py` so that they can be detected by pytest. (Further details below)
10. The folder `models` can be deleted if not required.
11. Pushing to *master* should be disabled and code reviewed by a peer before entering main.


## Project Organization

    ├── .github/workflows  <- Github actions/workflows 
    ├── config             <- local folder to store secrets etc that is not committed
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed
    │   ├── processed      <- The final, canonical data sets for modeling
    │   └── raw            <- The original, immutable data dump
    │
    ├── docs               
    │   └── pull_request_template.md <- Template for pull requests
    ├── models             <- Trained and serialized models objects
    │
    ├── notebooks
      └── how-to-guides    <- Explainations for how to use parts of the project
      └── project/theme    <- Each project/theme has a folder for related work
    │   └── NOTEBOOK_NAMED_CONVENTION.ipynb <- A notebook about a topic with a ticket number and description<- Jupyter notebooks. Naming convention is ticket number (for ordering the creator's initials, and a short free-text `-` delimited description, e.g. `JNE-01-jm-initial-data-exploration`
    │
    ├── outputs            <- Generated analysis as HTML, PDF, LaTeX, graphics and figures
    │
    ├── src                <- Source code for use in this project
        └── __init__.py    <- Makes src a Python module 
    │        
    ├── tests              <- All tests for this project
    │
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
    └── data_catalogue.ini <- The file storing data locations for access across the project
For more information on automated testing including PyTest, `pre-commit` hooks and GitHub Actions see [docs/README.md](docs/README.md)