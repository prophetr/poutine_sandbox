# Poutine Shop
​
This repository contains the data transformation logic for the Poutine Shop data warehouse.
​
The project is built on an open source tool: [dbt](https://www.getdbt.com/).

# Installation

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dev requirements ([dbt](https://www.getdbt.com/), [pre-commit](https://pre-commit.com/))
- Run `pre-commit install` to set up your git hook scripts. This will set your hooks so that the next time you push, pre-commit will be invoked (note: on its first invocation, pre-commit will need to install its own dependencies which may take a minute; these dependencies will be installed outside of your project and will be available from that moment onwards).

```bash
$ pip install -r requirements.txt
$ pre-commit install
```

# Profile

In order to use Poutine Shop, add the following to your ~/.dbt/profiles.yml file, taking care to replace the value of the `user` and `schema` parameter.
If you don't already have a profiles file, create a new one.

```
poutine_shop:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: lo43931.us-central1.gcp
      user: martin.guindon

      # SSO config
      authenticator: externalbrowser

      database: poutineshop_dev_db
      warehouse: elt_xs_wh
      schema: dbt_mguindon
      threads: 8

```
# Set up an environment variable

In order to set up account as an environment variable, follow the below steps,

- Activate your virtual environment for poutine shop.
- Run the command, export sf_account_id="lo43931.us-central1.gcp"
- Validate the above step by running the command, echo "$sf_account_id"
- Modify the value for account field to "{{ env_var('sf_account_id') }}" in the profiles.yml file.


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

# Working with Pre-Commit
- Pre-commit is configured to run various checks automatically when you attempt to push your code. We've overridden the default commit pattern to run on push to make committing small changes easier. When you attempt to push your code the pre-commit hooks will run, and if they pass, the push will succeed; if not there is some sort of issue that needs to be resolved before pushing your changes.
- Pre-commit will only run against changed files to keep its execution as quick as possible.
- On its first execution, pre-commit will install any dependencies it needs into a virtual environment (located outside of this repo); this may take a few minutes on its first run, but every following run will reuse that env and as a result will be much quicker.

# Working with SQLFluff
- SQLFluff lint is configured as a pre-commit hook that runs on push, so in most cases no explicit commands are needed. This will only list errors and will not fix any errors if found.
- If you would like to run SQLFluff lint manually, or would like to run it in fix mode, you can do so with the following commands which will run them through pre-commit. 
```
pre-commit run --hook-stage push sqlfluff-lint --all-files
pre-commit run --hook-stage manual sqlfluff-fix --all-files
```

# Working with YAMLLint
- YAMLLint is configured as a pre-commit, so in most cases no explicit commands are needed. This will only list errors and will not fix any errors if found.
- If you would like to run YAMLLint manually, you can do so with the following command which will run it through pre-commit.
```
pre-commit run --hook-stage push yamllint
```
