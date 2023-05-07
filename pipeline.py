import os
from tfx.proto import example_gen_pb2
from tfx.orchestration import pipeline
from tfx.components import CsvExampleGen


# example_gen_pb2 - split data into training and testing
# beam_pipeline_args - apache beam

def create_pipeline(
    pipeline_name,
    pipeline_root,
    data_path,
    serving_path,
    metadata_connection_config=None,
    beam_pipeline_args=None):

    components = []

    # Component ExampleGen
    output = example_gen_pb2.output(
        split_config = example_gen_pb2.SplitConfig(
            splits=[
                example_gen_pb2.SplitConfig(name='train', has_buckets=8),
                example_gen_pb2.SplitConfig(name='train', has_buckets=8)
            ]
        )
    )

    example_gen = CsvExampleGen(input_base=data_path, output_config=output)
    components.append(example_gen)

    return pipeline.Pipeline(
        pipeline_name=pipeline_name,
        pipeline_root=pipeline_root,
        components=components,
        metadata_connection_config=metadata_connection_config,
        beam_pipeline_args=beam_pipeline_args
    )



