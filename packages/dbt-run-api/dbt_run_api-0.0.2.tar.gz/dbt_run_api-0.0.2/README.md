# dbt-run-api


Once installed allows DBT commands to be sent via an api call. 

### Installation:

```bash
pip install dbt-run-api
```

### Set up:

After installing the package ensure your DBT project is set up correctly with all needed profile variables either explicitly defined or available as ENV-variables. 


### Execution:

#### Run server while in the same directory as your `dbt_project.yml':

```bash
uvicorn dbt_run_api:app
```
![](./images/1_start_server.png)


#### Ensure you DBT project has access to the database you have defined in profile.yml

#### Send call to endpoint:

```bash
curl -X POST http://localhost:8000/dbt -H 'Content-Type: application/json' -d '{"cmd":"test", "parameters": {"--vars":"{\"test_var\":1}", "--project-dir":"./"}}' 
```

**Notes:** 
- the `/` are necessary when passing a nested json
- commands are passed without `dbt` at the start. All dbt commands should be valid e.g `run`, `test`, et cetera. 

![](./images/3_api_call.png)

#### Results in the server log:

![](./images/2_server_log_after_api_call.png)