"""Pipeline modules.

Import concrete pipeline functions from their modules, for example
`src.pipelines.prepare_data`. This keeps data-only workflows independent from
training dependencies such as Torch and Optuna until they are actually needed.
"""
