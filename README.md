# Storage Query Python Client
This document describes all operations that can be executed on the StorageQuery API.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/storagequery/storage-query-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/storagequery/storage-query-python-client.git`)

Then import the package:
```python
import storagequery
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import storagequery
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import storagequery
from storagequery.rest import ApiException
from pprint import pprint

configuration = storagequery.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.storagequery.com/v1
configuration.host = "https://api.storagequery.com/v1"

# Defining host is optional and default to https://api.storagequery.com/v1
configuration.host = "https://api.storagequery.com/v1"
# Enter a context with an instance of the API client
with storagequery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storagequery.StorageQuerySQLApi(api_client)
    authorization = 'authorization_example' # str | Defines the user authorization API key
content_type = 'content_type_example' # str | Defines the request content media type
request_body_data_access_sql = storagequery.RequestBodyDataAccessSql() # RequestBodyDataAccessSql |  (optional)

    try:
        api_response = api_instance.run_sql_query(authorization, content_type, request_body_data_access_sql=request_body_data_access_sql)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageQuerySQLApi->run_sql_query: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.storagequery.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StorageQuerySQLApi* | [**run_sql_query**](docs/StorageQuerySQLApi.md#run_sql_query) | **POST** /data_access/sql | 


## Documentation For Models

 - [RequestBodyDataAccessSql](docs/RequestBodyDataAccessSql.md)
 - [SuccessResponseDataAccessSql](docs/SuccessResponseDataAccessSql.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

