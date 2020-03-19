from kedro.pipeline import node, Pipeline
from kedro_tutorial.nodes.data_engineering import *

de_pipeline = Pipeline([
        node(preprocess_companies, 'companies', 'preprocessed_companies', name='preprocess1', tags=["stage1"]),
        node(preprocess_shuttles, 'shuttles', 'preprocessed_shuttles', name='preprocess2', tags=['stage1']),
        node(create_master_table, ["preprocessed_shuttles", "preprocessed_companies", "reviews"],
             'master_table', name='master_table', tags=['stage2'])
    ],
    name = 'de_tag')