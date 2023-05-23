# Flask CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using Flask and SQLAlchemy ORM, which interacts with a Microsoft SQL Server database. The application manages information about banks, including their names and locations.

## Requirements

- Docker
- Python 3.x
- Python Virtual Environment (`venv`)

## Setting up the Project

1. **Clone the Repository:**
   
    ```bash
    git clone git@github.com:orestissab/Flask_CRUD_Application.git
    cd repository
    ```

2. **Create Python Virtual Environment:**
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Necessary Packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Docker Containers for SQL Server:**

    Ensure Docker is installed and running on your machine. Then, run the following commands to setup the main and test SQL server Docker containers:

    ```bash
    # Replace the <sa_password> with your preferred strong password.
    docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=<sa_password>' -p 1433:1433 --name sql_server -d mcr.microsoft.com/mssql/server
    docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=<sa_password>' -p 1434:1433 --name test_sql_server -d mcr.microsoft.com/mssql/server
    ```

6. **Setup Databases with Azure Data Studio:
**
    6.1. Download and install Azure Data Studio from the official Microsoft [website](https://docs.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio?view=sql-server-ver15).
    6.2. Open Azure Data Studio.
    6.3. Connect to the main SQL Server container using the following credentials:
        - Server: `localhost,1433`
        - Authentication Type: `SQL Login`
        - User name: `sa`
        - Password: `<sa_password>`
    6.4 Connect to the test SQL Server container using the following credentials:
        - Server: `localhost,1434`
        - Authentication Type: `SQL Login`
        - User name: `sa`
        - Password: `<sa_password>`
    6.5. Create the banks_db and test_banks_db databases in the main and test SQL Server containers respectively.
    6.6 Create the banks table in the banks_db and test_banks_db databases using the following SQL query:
        ```sql
        CREATE TABLE banks (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            location VARCHAR(50) NOT NULL
        );
        ```
    

7. **Setup the Environment Variables:**

    Create a `.env` file in the project root directory with the following environment variables:

    ```bash
    MAIN_DB_URI="mssql+pyodbc://sa:<sa_password>@localhost:1433/sql_server?driver=ODBC+Driver+17+for+SQL+Server"
    TEST_DB_URI="mssql+pyodbc://sa:<sa_password>@localhost:1434/test_sql_server?driver=ODBC+Driver+17+for+SQL+Server"
    ```

## Running the Application

Run the application using the following command:

```bash
python app.py
```
You can then access the application by visiting http://localhost:5000 on your web browser.

## Running the Tests

Run the tests using the following command:

```bash
pytest test_app.py
```