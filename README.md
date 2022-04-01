# Poutine Shop
​
This repository contains the data transformation logic for the Poutine Shop data warehouse.
​
The project is built on an open source tool: [dbt](https://www.getdbt.com/).

# Install dbt
Install dbt by running `pip3 install -r requirements.txt`

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
