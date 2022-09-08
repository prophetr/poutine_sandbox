This script creates random generated data table 

----

## Contents

**[Tables](#tables)**
- [number_of_records](#number_of_records)

**[Columns](#columns)**
- [pk](#pk)
- [cache_columns](#cache_columns)

**[Data Types](#data-types)**
- [int](#int)
- [accepted_values](#accepted_values)
- [text](#text)
- [date](#date)
- [from_date](#from_date)
- [phone](#phone)
- [name](#name)
- [email](#email)
- [fk](#fk)
- [mapped_values](#mapped_values)

**[Improvements](#improvements)** 

----

### Tables

#### number_of_records

The number of records to generate for this table

**Usage:**
```yaml
tables:
  - name: users
    number_of_records: 10
```

----

### Columns

#### pk

Set to `true` if the column is a primary key. The primary key column
is used to generate `fk` data type columns.

default: `false`

**Usage**
```yaml
tables:
  - name: users
    number_of_records: 10
    columns:
      - name: id
        pk: true
```


#### cache_column

Certain data type depends on other data columns for reference.
Set cache_column to `true` if another column(s) needs to reference it. 

default = `false`

Note: The following data types depend on a cache_column:
`from_date` and `mapped_values`

**Usage**
```yaml
tables:
  - name: users
    number_of_records: 10
    columns:
      - name: created_at
        cache_column: true
```

----

### Data Types

#### int

Generate sequenced or random integers

**Usage**
```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: id
        pk: true
        generate_config:
          data_type: int
          method: sequence
          min: 1
          max: 1001
```
**Args:**
    
- `method` (required): 
  - `sequence`: Ordered integer starting with `min` to `max` value
  - `random`: Generate random integers between `min` and `max` value
- `min` (required): The lowest integer number
- `max` (required): The highest integer number

#### accepted_values

Generate random values from the inputted list

**Usage**
```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: is_active
        generate_config:
          data_type: accepted_values
          accepted_values: [true, false]
          weights: [0.9, 0.1]
```
**Args:**
    
- `accepted_values` (required): A list of accepted values that will be randomly 
assigned throughout the column
- `weights` (optional): A list of weight percentage to the `accepted_values` distribution
respectively

#### text

Generate a random text

**Usage**
```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: title
        generate_config:
          data_type: text
          size: small
```
**Args:**
    
- `size` (required): 
  - `small`: Generate a small text
  - `medium`: Generate a medium text
  - `large`: Generate a large text

#### date

Generate a random date between `start_date` and `end_date`

```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: created_at
        generate_config:
          data_type: date
          start_date: '2021-01-01'
          end_date: '2022-10-01'
          timestamp: true
```
**Args:**
    
- `start_date` (required): The min date
- `end_date` (required): The max date
- `timestamp` (optional) - (`default = false`): True to include a timestamp

#### from_date
```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: updated_at
        generate_config:
          data_type: from_date
          timeline: after
          referenced_table: users
          referenced_column: created_at
          max_seconds_apart: 31536000 # one year
```
**Args:**
    
- `timeline` (required):
  - `before`: Subtract from the referenced date
  - `after`: Add from the referenced date
- `referenced_table` (optional) - (`default = table_name`): The name of the table where the referenced 
cached_column exist
- `referenced_column` (required) - (`default = false`): The name of the cached_column that this 
column is referring to
- `max_seconds_apart`(optional) - (`default = 31536000`): The max count of seconds apart from the 
referenced date

#### phone

Generate random phone numbers

```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: phone
        generate_config:
          data_type: phone
```

#### name

Generate random names

```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: name
        generate_config:
          data_type: name
```

#### email

Generate random emails

```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: email
        generate_config:
          data_type: email
```

#### fk

Generate a random foreign key from an existing table's primary key

```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: group_id
        generate_config:
          data_type: date
          referenced_table: 'group'
          repeat: true
```
**Args:**
    
- `referenced_table` (required): The name of the table where the primary key is referenced 
- `repeat` (optional) - (`default = true`): If the same foreign key can be repeated

#### mapped_values

Generate values using a mapped dictionary where the keys are from a cached column 

**Usage**
```yaml
tables:
  - name: users
    number_of_records: 1000
    columns:
      - name: group_name
        generate_config:
          data_type: mapped_values
          referenced_table: groups
          referenced_column: group_id
          mapped_values: {
              1: "Montreal",
              2: "Vancouver",
              3: "Toronto"              
          }
```
**Args:**
- `referenced_table` (optional) - (`default = table_name`): The name of the table where the referenced 
cached_column exist
- `referenced_column` (required): The name of the cached_column that this column is referring to
- `mapped_values` (required): The mapped values 

----

### Improvements

- Link email and name column to match in the same df
- Ability to cache and reference dataframes instead of only series
- Nullable options