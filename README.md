# cookiecutter-repo_name
 
Project contact: [*lauren.dunn@ukhsa.gov.uk*](mailto:*project_contact_email*)


## PURPOSE
This repo shows how CPIH and CPI at division level has changed over time. The results are shown on a interactive dashboard which the user can filter for date, dataset and division level. 

## GUIDANCE/ GROUND RULES

1) Run main.ipynb
2) Change to notebooks then type into the terminal streamlit run app.py 


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