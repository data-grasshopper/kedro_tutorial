from kedro.pipeline import node, Pipeline
from kedro_tutorial.nodes.price_prediction import *

ds_pipeline = Pipeline(
        [
            node(
                split_data,
                ["master_table", "params:test_size", "params:random_state"],
                ["X_train", "X_test", "y_train", "y_test"], tags=['stage4', 'preprocess']
            ),
            node(train_model, ["X_train", "y_train"], "regressor", tags=['stage4']),
            node(evaluate_model, ["regressor", "X_test", "y_test"], None, tags=['stage4']),
        ],
    name = 'ds_tag')