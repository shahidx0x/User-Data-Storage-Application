# FastAPI

## Description

FastAPI is a web framework for building APIs with Python.

## API Documentation

This API follows the OpenAPI 3.1.0 specification.

### Base URL

All endpoints are relative to the following base URL:


## Endpoints

### Parents

#### Create Parent

- **Method**: POST
- **URL**: `/parents`
- **Summary**: Create a new parent.
- **Request Body**:
  - `ParentSchema`

#### Get Parents

- **Method**: GET
- **URL**: `/parents`
- **Summary**: Get a list of parents.
- **Query Parameters**:
  - `search` (optional): Search by parent's first name.
  - `page` (optional): Page number.
  - `limit` (optional): Number of items to display per page.

#### Update Parent

- **Method**: PATCH
- **URL**: `/parents/{parent_id}`
- **Summary**: Update an existing parent.
- **Path Parameters**:
  - `parent_id`: ID of the parent to update.
- **Request Body**:
  - `ParentUpdateSchema`

#### Delete Parent

- **Method**: DELETE
- **URL**: `/parents/{parent_id}`
- **Summary**: Delete an existing parent.
- **Path Parameters**:
  - `parent_id`: ID of the parent to delete.

### Children

#### Get Children

- **Method**: GET
- **URL**: `/children`
- **Summary**: Get a list of children.
- **Query Parameters**:
  - `search` (optional): Search by child's first name.
  - `page` (optional): Page number.
  - `limit` (optional): Number of items to display per page.

#### Make Children

- **Method**: POST
- **URL**: `/children`
- **Summary**: Create a new child.
- **Request Body**:
  - `ChildSchema`

#### Update Children

- **Method**: PATCH
- **URL**: `/children/{children_id}`
- **Summary**: Update an existing child.
- **Path Parameters**:
  - `children_id`: ID of the child to update.
- **Request Body**:
  - `ChildrenUpdateSchema`

#### Delete Children

- **Method**: DELETE
- **URL**: `/children/{children_id}`
- **Summary**: Delete an existing child.
- **Path Parameters**:
  - `children_id`: ID of the child to delete.

## Schemas

- `ParentSchema`
- `ParentUpdateSchema`
- `ChildSchema`
- `ChildrenUpdateSchema`
- `HTTPValidationError`
- `ValidationError`
