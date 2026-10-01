import os
from pathlib import Path

project_source_name='src'
app_name = "bike"
Files_Folder_list=[
    f"{project_source_name}/{app_name}/__init__.py",

    f"{project_source_name}/{app_name}/models/architecture/model.py", # your current DL model, moved out of the notebook
    f"{project_source_name}/{app_name}/models/baseline.py", # seasonal naive, LightGBM
    f"{project_source_name}/{app_name}/models/datasets.py", # seasonal naive, LightGBM
    f"{project_source_name}/{app_name}/models/export.py", # seasonal naive, LightGBM
    f"{project_source_name}/{app_name}/config/setting.py", # pydantic-settings: env vars, paths, secrets refs
    f"{project_source_name}/{app_name}/config/schemas.py", # Pydantic models for config (train, backtest, serving)

    f"{project_source_name}/{app_name}/data/ingest/trips.py",  # TfL / own trip data loaders
    f"{project_source_name}/{app_name}/data/validation/schemas.py",  # Pandera / Great Expectations checks per table
    f"{project_source_name}/{app_name}/data/validation/checks.py", # freshness, row counts, missing hours
    f"{project_source_name}/{app_name}/data/io.py", # read/write lakehouse, Postgres, Parquet
    f"{project_source_name}/{app_name}/data/splits.py", # time-based / rolling-origin splits

    # One definition, used in training AND serving
    f"{project_source_name}/{app_name}/features/time_features.py",  # hour, weekday, holiday, cyclical encodings
    f"{project_source_name}/{app_name}/features/lag_features.py",  # lags, rolling means (leakage-safe)
    f"{project_source_name}/{app_name}/features/weather_features.py", # forecast-weather features (point-in-time)
    f"{project_source_name}/{app_name}/features/spatial_features.py", # zone/H3 aggregates, neighbour demand
    f"{project_source_name}/{app_name}/features/pipeline.py",  # builds the full feature table
    f"{project_source_name}/{app_name}/features/store.py", # Feast client wrapper (offline + online fetch)
    f"{project_source_name}/{app_name}/pipeline/__init__.py",

    # Training, hyper-parameter tunning
    f"{project_source_name}/{app_name}/training/train.py",  # Lightning trainer, logs to MLflow
    f"{project_source_name}/{app_name}/training/tune.py",  # Optuna search
    f"{project_source_name}/{app_name}/training/callbacks.py",  # early stopping, checkpoints
    
    ## evaluation
    f"{project_source_name}/{app_name}/evaluation/metrics.py", # WAPE, MAE, RMSE, bias, coverage of intervals
    f"{project_source_name}/{app_name}/evaluation/backtest.py", # rolling-origin backtest over many weeks
    f"{project_source_name}/{app_name}/evaluation/reconcile.py", # station → zone → city reconciliation
    f"{project_source_name}/{app_name}/evaluation/gate.py", # "does challenger beat champion?" promotion rule

    ## registry
    f"{project_source_name}/{app_name}/resgistry/mlflow_registry.py",  # register, set aliases (champion/challenger), load

    ## inference
    f"{project_source_name}/{app_name}/inference/predictor.py",  # loads model by alias, predicts (shared by batch + API)
    f"{project_source_name}/{app_name}/inference/batch.py",  # hourly batch scoring → forecasts table
    f"{project_source_name}/{app_name}/inference/postprocess.py", # clip negatives, round, reconcile, add intervals

    ## serving: Thin HTTP layer over inference/
    f"{project_source_name}/{app_name}/api/main.py", # FastAPI app, /health, /ready
    f"{project_source_name}/{app_name}/api/routes.py", # /forecast endpoints 
    f"{project_source_name}/{app_name}/api/schemas.py", # request/response models
    f"{project_source_name}/{app_name}/api/metrics.py",  # Prometheus instrumentation

    ## monitoring 
    f"{project_source_name}/{app_name}/monitoring/accuracy.py", # join forecasts to actuals, WAPE/bias per zone
    f"{project_source_name}/{app_name}/monitoring/drift.py", # Evidently data drift, PSI
    f"{project_source_name}/{app_name}/monitoring/alerts.py", # thresholds → Slack/email

    ## Pipelines
    f"{project_source_name}/{app_name}/pipelines/ingest_pipeline.py",
    f"{project_source_name}/{app_name}/pipelines/training_pipeline.py", # features → train → backtest → register
    f"{project_source_name}/{app_name}/pipelines/scoring_pipeline.py",
    f"{project_source_name}/{app_name}/pipelines/monitoring_pipeline.py",

    ##  
    f"{project_source_name}/{app_name}/cli.py", # `bikecast train`, `bikecast score` (Typer)
    f"{project_source_name}/{app_name}/utils/logging.py", ## structured JSON logs
    f"{project_source_name}/{app_name}/utils/seed.py", ## reproducibility
    f"{project_source_name}/{app_name}/utils/exception.py", ## reproducibility
    "README.md",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".gitignore"
]

for filepath in Files_Folder_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")