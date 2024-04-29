# DataAetherScan

`dataaetherscan` is a Python package that facilitates interaction with the DataAetherScan API. It provides methods for authentication and access to various API resources such as users, channels, jobs, and credits.

## Installation

Install the package using `pip` with the following command:

```bash
pip install dataaetherscan
```

## Usage

First, you need to create a `DataAetherScan` object with your credentials:

```python
from dataaetherscan import DataAetherScan

das = DataAetherScan("yourEmail@example.com", "yourPassword")
```

### Authentication

Authentication is automatically performed upon instantiation:

```python
das.authenticate()
```

### API Methods

After successful authentication, you can access various API endpoints:

#### Retrieve User Information

```python
user_info = das.get_user()
print(user_info)
```

#### Retrieve Channel List

```python
channels = das.get_channels()
print(channels)
```

#### Retrieve Credit Information

```python
credit_info = das.get_credit()
print(credit_info)
```

#### Retrieve and Manage Jobs

- Retrieve all jobs:

  ```python
  jobs = das.get_jobs()
  print(jobs)
  ```

- Retrieve a specific job:

  ```python
  job = das.get_job(job_id)
  print(job)
  ```

- Create a new job:

  ```python
  job_data = {'name': 'Job1', 'description': 'Data processing'}
  new_job = das.create_job(job_data)
  print(new_job)
  ```

- Delete a job:

  ```python
  response = das.delete_job(job_id)
  print(response)
  ```

## Error Handling

The methods can raise a `ValueError` if there are issues with the API request. Make sure to handle your requests within try-except blocks:

```python
try:
    user_info = das.get_user()
except ValueError as e:
    print("An error occurred:", e)
```





---

# Creating a Job with DataAetherScan

This section outlines how to properly configure and send a request to create a job using the `dataaetherscan` API. A job is a task submitted to the API that involves tracking certain products across different channels and countries.

## Job Data Structure

To create a job, you need to specify details about the channels, country codes, and products. Here’s the structure of the data required:

```python
job_data = {
    "channel": "Google",
    "country_code": "DE",
    "products": [
        {
            "sku": 1,
            "gtin_ean": "761856508385"
        }
    ]
}
```

### Parameters

- **channel**: (string) The name of the channel where the products will be tracked.
- **country_code**: (string) The ISO country code where the channel is located.
- **products**: (list of dictionaries) A list of products to be tracked, each with specific attributes.

#### Product Attributes

Each product dictionary may contain the following fields:

- **sku**: (string, required) The stock keeping unit or identifier for the product.
- **gtin_ean**: (string, optional) The global trade item number or European article number of the product.
- **title**: (string, optional) The title or name of the product.

### Validation Rules

The job creation involves several validation steps to ensure the integrity of the data:

1. **Product Validation**:
   - At least one of `gtin_ean` or `title` must be present along with `sku`.
   - If neither `gtin_ean` nor `title` is provided, a validation error will be raised, indicating that at least one of these fields is required.

2. **Job Serializer Validation**:
   - Products must be provided as a list of dictionaries.
   - An empty list of products is not allowed.
   - Each product's data is validated individually.

## Creating a Job

To create a job, use the `create_job` method of your `DataAetherScan` instance:

```python
das = DataAetherScan("yourEmail@example.com", "yourPassword")
try:
    new_job = das.create_job(job_data)
    print("Job created successfully:", new_job)
except ValueError as e:
    print("An error occurred while creating the job:", e)
```

## Error Handling

Handle potential errors during the job creation process to manage situations where the input data might not meet the API requirements:

- Use try-except blocks to catch exceptions, particularly `ValueError`, which indicates a problem with the job data or an API request failure.

This guide provides a comprehensive overview of the requirements and steps to create a job using the `dataaetherscan` package, ensuring that all data complies with the underlying API's validation rules.





## Contributing

Improvements and pull requests are welcome! Please ensure that you follow existing code styles and practices.
