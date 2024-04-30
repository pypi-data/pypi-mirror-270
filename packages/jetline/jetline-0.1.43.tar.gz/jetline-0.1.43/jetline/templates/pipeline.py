from jetline.pipeline.pipeline import Pipeline
from jetline.pipeline.node import Node
from example_pipeline import nodes as func


def register(data_manager) -> Pipeline:
    node1 = Node(
        function=func.node_function_1,
        inputs=["Name"],
        outputs=["Name"],
        viz={"y": 200, "x": 00, "sources": ['Name']}
    )
    node2 = Node(
        function=func.node_function_2,
        inputs=["Name"],
        viz={"y": 400, "x": 200, "sources": ["node_function_1", "Name"]}
    )

    return Pipeline(nodes=[node1, node2], data_manager=data_manager)
