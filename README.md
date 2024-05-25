# dagster-pipes-gcp

🚧 Experimental!

Deploy a simple GCP function and orchestrate it with Dagster.

## Devcontainer

This repository contains a devcontainer. I recommend that you use it.

## Setup

Add a service account JSON credentials called 'sa.json' file to '.devcontainer/.secrets'. This service account should have permissions to invoke a cloud function & read logs, but to be honest I've used a service account with very broad permissions for now.

In .devcontainer/.env, change the GOOGLE_PROJECT_ID environment variable to your GCP project id.

Open the project in the devcontainer and run `just setup`/`just s`. This will install the dependencies and configure gcloud.

## CI/CD

In GitHub secrets, ensure that you have set the `GOOGLE_CREDENTIALS` secret with the JSON service account credentials of a service account that is allowed to deploy cloud functions.

Also, you should change the 'gcp_project_id' input to your own project id in the 'deploy' templates used by '.github/workflows/pipeline-nprod.yaml' and .'github/workflows/pipeline-prod.yaml'.

Your project must enable the following APIs:

- ...

CI/CD workflow is as follows:

- On PR to main: run pre-commit hooks
- On push to main:
  - Run pre-commit hooks
  - Build function source code
  - Deploy function source code
- On release:
  - Build function source code
  - Deploy function source code

## Executing an asset that orchestrates a cloud function

Go to 'dagster/DAG.py' and change the 'function_url' parameter to the URL of your cloud function.

> The cloud function uses the default compute service account because that was easy to set up. You should probably make a custom one.

Then start dagster locally:

```
just dd
```

And materialize the asset.
