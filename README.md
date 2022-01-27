# Poutine Shop
​
This repository contains the data transformation logic for the Poutine Shop data warehouse.
​
The project is built on an open source tool: [dbt](https://www.getdbt.com/).
​
### Setup and Dependencies
​
dbt requires a functional Python environment on your workstation. It's best to avoid Python that comes pre-installed with your OS, and we recommend creating a virtual environment dedicated to the project. This can be done using any of Python's virtual environment tools including `virtualenv` or `conda` for example, although we recommend virtualenv for ease of use.
​
NOTE: These instructions are a general guideline only. They may or may not work as-is on your computer, as multiple factors can influence compatibility and steps. These instructions also assumes that you already have Git set up and your SSH keys configured to be able to clone and push changes.
#### Installing Python, dbt and pre-commit on Mac
​
There are many ways to install Python on a Mac. We recommend using [Homebrew](https://brew.sh/):
​
1. Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install Python 3.8: `brew install python@3.8` 
3. Install Virtualenv: `pip3 install virtualenv`
4. Go to the directory where you store your codebases. If you don't have any, we recommend creating a `~/Code` directory.
5. Clone the git repository: `git clone git@github.com:Montreal-Analytics/poutineshop.git`
6. Go to the `data-dbt` directory.
7. Create a virtual environment: `python3 -m venv venv_dbt`
8. Activate the virtual environment: `source venv_dbt/bin/activate`
9. Install dependencies: `pip3 install -r requirements.txt`
10. Install pre-commit hooks: `pre-commit install`
​
#### Installing Python, dbt and pre-commit on Windows
​
1. Install Python 3.8: https://www.python.org/downloads/release/python-3810/
2. Install Virtualenv: `py -m pip install virtualenv`
3. Go to the directory where you store your codebases. If you don't have any, we recommend creating a `\Code` directory.
4. Clone the git repository: `git clone git@github.com:Montreal-Analytics/poutineshop.git`
5. Go to the `data-dbt` directory.
6. Create a virtual environment: `py -m venv venv_dbt`
7. Activate the virtual environment: `.\venv_dbt\Scripts\activate`
8. Install dependencies: `py -m pip install -r requirements.txt`
9. Install pre-commit hooks: `pre-commit install`
​
#### Configure Profile and Connections
​
This project expects a `~/.dbt/profiles.yml` file.
​
1. You need to have a Redshift user, with the `transformer` and `reporter` groups assigned to it.
2. Create the `~/.dbt` directory:
- `mkdir ~/.dbt`
3. Copy the example profile to the directory:
- `cp profiles.sample.yml ~/.dbt/profiles.yml`
4. Add your username, password, and schema to your local file.
​
### Code Editor Setup
​
You can use any code editor to work with dbt, but VS Code and Atom are the most common ones and have useful extensions to make your life easier. We recommend VS Code if you don't currently have a preference.
​
Useful VS Code extensions:
​
- vscode-dbt by bastienboutonnet
- dbt Power User by innoverio
- Better Jinja by Samuel Colvin
- Find Related Files by Eric Amodio
- Rainbow CSV by mechatroner
- Todo Tree by Gruntfuggly
- YAML by Red Hat
- GitLens by Eric Amodio
- GitHub Pull Requests and Issues by GitHub
- dbt Power User by innoverio
​
#### Specific configurations (to be added in the settings.json of VS Code):
​
The following will remap Markdown, Yaml and SQL files to use the Jinja-flavoured interpreter:
​
```
    "files.associations":{
        "*.md": "jinja-md",
        "*.yml": "jinja-yaml",
        "*.sql": "jinja-sql",
    },
```
​
The following will configure Related Files rules for raw / compiled models:
​
```
"findrelated.rulesets": [
        {
            "name": "sql",
            "rules": [
                {
                    "pattern": "^(.*/)?models/(.*/)?(.+\\.sql)$",
                    "locators": [
                        "**/compiled/**/$3"
                    ]
                },
                {
                    "pattern": "^(.*/)?compiled/(.*/)?(.+\\.sql)$",
                    "locators": [
                        "**/run/**/$3"
                    ]
                },
                {
                    "pattern": "^(.*/)?run/(.*/)?(.+\\.sql)$",
                    "locators": [
                        "**/models/**/$3"
                    ]
                }
            ]
        }
    ],
```
​
The following will configure spacing/indentation rules to follow the style guide:
​
```
    "[yaml]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 2
    },
    "[sql]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
    "[jinja-yaml]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 2
    },
    "[jinja-sql]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
    "editor.detectIndentation": false,
    "editor.rulers": [
        { "column": 80, "color": "#403558" }
    ],
```
​
### Using the project:
​
Once everything has been setup, try running the following commands:
​
- dbt debug (if you're having issues)
- dbt deps
- dbt seed
- dbt run
- dbt test
​
### SQL Styleguide + dbt Best Practices
​
We follow the [Matt Mazur SQL style guide](https://github.com/mattm/sql-style-guide) and the one by [Fishtown Analytics for dbt-specific behaviors](https://github.com/fishtown-analytics/corp/blob/master/dbt_coding_conventions.md#sql-style-guide).
​
We also follow the [best practices documented on the dbt website](https://docs.getdbt.com/docs/guides/best-practices/).
​
SQL and YAML styles are enforced by linters that runs automatically before any commit.
​
### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- [How we structure our dbt projects](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](http://community.getbdt.com/) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
- dbt [Release notes](https://github.com/fishtown-analytics/dbt/releases)
