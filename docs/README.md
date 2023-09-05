# Automated checks run locally and on GitHub

## Hooks with [pre-commit](https://pre-commit.com/)
Pre-commit is a python tool for managing pre-commit hooks so that issues are fixed before they end up in the commit history of git. By installing pre-commit in a repo you can ensure your code is of the correct standard before you commit it and prevent issues when conducting PRs, freeing you up to focus on actual code review.
```bash
pip install pre-commit

# Run the following command in the repo directory
pre-commit install

# This command runs pre-commit against all files in the repo. Use this the first time it is installed
pre-commit run --all-files
```
The hooks currently installed are:
 - [nbstripout](https://github.com/kynan/nbstripout)
 - [pre-commit](https://github.com/pre-commit/pre-commit) incl. large file checks and [nbstripout](https://github.com/kynan/nbstripout)
 
 Style checks including black, flake8 and styleR are included but not enabled. If you would like to run styling/linting they can be enabled by removing the "#" signs from the relevant hook at `.pre-commit-config.yaml`. For example, to enable R style checks, go from:
 ```
  - repo: https://github.com/lorenzwalthert/precommit
        # rev: v0.3.2
        # hooks: 
        # -   id: style-files
```
 to:
 ```
   - repo: https://github.com/lorenzwalthert/precommit
        rev: v0.3.2
        hooks: 
        -   id: style-files
```
## GitHub Actions
GitHub Actions are pre-configured and can be enabled by adding relevant `.yml` files in the folder: `.github/workflows`. Additionally the `pre-commit` checks can be altered by changing the `~/.pre-commit-config.yaml` in the repositories root. <br>
GitHub Actions must be enabled on the remote repository. This can be done by going into the repository then "Settings" -> "Actions" -> "General" -> Allow the action level you require. If this is unavaliable, a request can be put through the service desk to request GitHub Actions for your repository. 

## Local vs Remote
`pre-commit` hooks, nbstripout and a variety of testing & automation can be run locally (on your laptop/AWS instance/notebook) or remotely (on GitHub through GitHub Actions). The difference between these is running locally allows us to protect our GitHub repositories from data & code security risks. By running `nbstripout` locally before pushing to GitHub, the potentially sensitive outputs in your notebooks can be removed before being put onto GitHub.<br>
Why is this useful? This will prevent sensitive data from being shared either around the organisation or even into the public, and plots in notebooks take up storage so our repositories become inefficient.<br>
GitHub Actions allows coders to test their code (alongside a lot of other capabilities) on a platform that others can see. This allows us to robustly understand issues in our repositories and monitor organisational problems. This does not allow us to defend our repositories from sensitive data entering, which must be done locally. 


## Testing using [Pytest](https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test)
Pytest is a common python testing framework. Tests are important for ensuring that changes to code do no break existing functionality and can be run in an automated manner to check this. Tests should be stored in the "tests" directory and be preceded with "test_XXX.py" so that pytest can identify them. Tests can be run as part of the pre-commit GitHub Actions on pull requests.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
