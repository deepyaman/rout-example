"""int_pipeline defines the subpipeline to create the int data layer."""
from kedro.pipeline import Pipeline, node
import pandas as pd

int_pipeline = Pipeline(  # pylint: disable=invalid-name
    [
        node(
            lambda df: df.rename(columns={c: c[:-2] for c in df.columns}),
            "raw_seal_population.1",
            "raw_seal_population.1_renamed",
        ),
        node(
            lambda *objs: pd.concat(objs),
            ["raw_seal_population", "raw_seal_population.1_renamed"],
            "int_seal_population",
        ),
    ],
    name="intermediate",
)
