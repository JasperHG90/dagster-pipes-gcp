# from dagster import (
#     AssetExecutionContext,
#     PipesResult,
#     PipesTempFileContextInjector,
#     PipesTempFileMessageReader,
#     asset,
#     open_pipes_session,
# )

CLOUD_FUNCTIONS_URL = (
    "https://europe-west4-jasper-ginn-dagster.cloudfunctions.net/dagster-pipes-gcp-acc"
)
SERVICE_ACCOUNT_FILE = "/Users/jasperginn/Downloads/jasper-ginn-dagster-897f24248ee6.json"
LOGGER_NAME = "dagster-pipes-gcp"


# @asset
# def some_pipes_asset(context: AssetExecutionContext) -> Iterator[PipesResult]:
#     with open_pipes_session(
#         context=context,
#         extras={"foo": "bar"},
#         context_injector=PipesTempFileContextInjector(),
#         message_reader=PipesTempFileMessageReader(),
#     ) as pipes_session:
#         # Get the bootstrap payload encoded as a Dict[str, str] suitable for passage as environment
#         # variables.
#         env_vars = pipes_session.get_bootstrap_env_vars()

#         # `launch_external_process` is responsible for including the passed `env_vars` in the
#         # launched external process.
#         external_process = launch_external_process(env_vars)

#         # Continually poll the external process and stream any incrementally received messages back
#         # to Dagster
#         while not is_external_process_done(external_process):
#             yield from pipes_session.get_results()

#     # Yield any remaining results received from the external process.
#     yield from pipes_session.get_results()
