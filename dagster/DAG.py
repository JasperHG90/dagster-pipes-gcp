import google.cloud.storage
from dg_pipes import PipesCloudFunctionClient, PipesCloudStorageMessageReader

from dagster import AssetExecutionContext, Definitions, MaterializeResult, asset  # type: ignore


@asset(
    description="A cloud function that writes fake data to a delta table.",
)
def cloud_function_pipes_asset(
    context: AssetExecutionContext, pipes_function_client: PipesCloudFunctionClient
) -> MaterializeResult:
    return pipes_function_client.run(
        context=context,
        # function_url="http://127.0.0.1:8080",
        function_url="https://europe-west4-jasper-ginn-dagster.cloudfunctions.net/dagster-pipes-gcp-nprod",
        event={
            "dl_bucket": "gs://jasper-ginn-dagster-data-lake/",
        },
    ).get_materialize_result()


defs = Definitions(
    assets=[cloud_function_pipes_asset],
    resources={
        "pipes_function_client": PipesCloudFunctionClient(
            message_reader=PipesCloudStorageMessageReader(
                bucket="jasper-ginn-dagster-dagster-pipes-logs",
                client=google.cloud.storage.Client(),
            )
        )
    },
)
