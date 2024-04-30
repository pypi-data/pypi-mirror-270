from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

import pytest

from great_expectations.core import ExpectationSuite
from great_expectations.core.batch import BatchRequest
from great_expectations.core.yaml_handler import YAMLHandler
from great_expectations.rule_based_profiler import RuleBasedProfilerResult
from great_expectations.rule_based_profiler.rule_based_profiler import RuleBasedProfiler
from great_expectations.validator.metric_configuration import MetricConfiguration

if TYPE_CHECKING:
    from great_expectations.data_context import AbstractDataContext

yaml = YAMLHandler()


@pytest.mark.filesystem
def test_batches_are_accessible(
    multibatch_generic_csv_generator,
    multibatch_generic_csv_generator_context,
):
    """
    What does this test and why?
    Batches created in the multibatch_generic_csv_generator fixture should be available using the
    multibatch_generic_csv_generator_context
    This test most likely duplicates tests elsewhere, but it is more of a test of the configurable fixture.
    """  # noqa: E501

    context: AbstractDataContext = multibatch_generic_csv_generator_context
    data_relative_path = "../data"
    assert context.root_directory
    data_path = pathlib.Path(context.root_directory, data_relative_path)
    datasource_name = "generic_csv_generator"
    data_connector_name = "daily_data_connector"
    asset_name = "daily_data_asset"

    datasource = context.datasources[datasource_name]

    data_connector = datasource.data_connectors[data_connector_name]

    total_batches: int = 20
    file_list = multibatch_generic_csv_generator(
        data_path=data_path, num_event_batches=total_batches
    )

    assert (
        data_connector._get_data_reference_list_from_cache_by_data_asset_name(
            data_asset_name=asset_name
        )
        == file_list
    )

    batch_request_1 = BatchRequest(
        datasource_name="generic_csv_generator",
        data_connector_name="daily_data_connector",
        data_asset_name="daily_data_asset",
        data_connector_query={
            "index": -1,
        },
    )
    # Should give most recent batch
    validator_1 = context.get_validator(
        batch_request=batch_request_1,
        create_expectation_suite_with_name="my_expectation_suite_name_1",
    )
    metric_max = validator_1.get_metric(
        MetricConfiguration("column.max", metric_domain_kwargs={"column": "batch_num"})
    )
    assert metric_max == total_batches
    metric_value_set = validator_1.get_metric(
        MetricConfiguration(
            "column.distinct_values",
            metric_domain_kwargs={"column": "string_cardinality_3"},
        )
    )
    assert metric_value_set == {"category0", "category1", "category2"}

    batch_request_2 = BatchRequest(
        datasource_name="generic_csv_generator",
        data_connector_name="daily_data_connector",
        data_asset_name="daily_data_asset",
        data_connector_query={
            "index": -2,
        },
    )
    validator_2 = context.get_validator(
        batch_request=batch_request_2,
        create_expectation_suite_with_name="my_expectation_suite_name_2",
    )
    metric_max = validator_2.get_metric(
        MetricConfiguration("column.max", metric_domain_kwargs={"column": "batch_num"})
    )
    assert metric_max == total_batches - 1
    metric_value_set = validator_2.get_metric(
        MetricConfiguration(
            "column.distinct_values",
            metric_domain_kwargs={"column": "string_cardinality_3"},
        )
    )
    assert metric_value_set == {"category0", "category1", "category2"}

    for batch_num in range(1, total_batches + 1):
        batch_request = BatchRequest(
            datasource_name="generic_csv_generator",
            data_connector_name="daily_data_connector",
            data_asset_name="daily_data_asset",
            data_connector_query={
                "index": -batch_num,
            },
        )
        validator = context.get_validator(
            batch_request=batch_request,
            create_expectation_suite_with_name=f"my_expectation_suite_name__{batch_num}",
        )
        metric_max = validator.get_metric(
            MetricConfiguration("column.max", metric_domain_kwargs={"column": "batch_num"})
        )
        assert metric_max == (total_batches + 1) - batch_num
        metric_value_set = set(
            validator.get_metric(
                MetricConfiguration(
                    "column.distinct_values",
                    metric_domain_kwargs={"column": "string_cardinality_3"},
                )
            )
        )
        assert metric_value_set == {"category0", "category1", "category2"}


@pytest.mark.slow  # 2.04s
@pytest.mark.filesystem
def test_profile_includes_citations(
    alice_columnar_table_single_batch_context,
    alice_columnar_table_single_batch,
):
    # Load data context
    data_context: AbstractDataContext = alice_columnar_table_single_batch_context

    # Load profiler configs & loop (run tests for each one)
    yaml_config: str = alice_columnar_table_single_batch["profiler_config"]

    # Instantiate Profiler
    profiler_config = yaml.load(yaml_config)
    # `class_name`/`module_name` are generally consumed through `instantiate_class_from_config`
    # so we need to manually remove those values if we wish to use the **kwargs instantiation pattern  # noqa: E501
    profiler_config.pop("class_name")

    profiler: RuleBasedProfiler = RuleBasedProfiler(
        **profiler_config,
        data_context=data_context,
    )

    # BatchRequest yielding exactly one batch
    alice_single_batch_data_batch_request: dict = {
        "datasource_name": "alice_columnar_table_single_batch_datasource",
        "data_connector_name": "alice_columnar_table_single_batch_data_connector",
        "data_asset_name": "alice_columnar_table_single_batch_data_asset",
    }

    result: RuleBasedProfilerResult = profiler.run(
        batch_request=alice_single_batch_data_batch_request
    )

    assert result.citation is not None and len(result.citation.keys()) > 0


@pytest.mark.slow  # 2.16s
@pytest.mark.filesystem
def test_profile_get_expectation_suite(
    alice_columnar_table_single_batch_context,
    alice_columnar_table_single_batch,
):
    # Load data context
    data_context: AbstractDataContext = alice_columnar_table_single_batch_context

    # Load profiler configs & loop (run tests for each one)
    yaml_config: str = alice_columnar_table_single_batch["profiler_config"]

    # Instantiate Profiler
    profiler_config = yaml.load(yaml_config)
    # `class_name`/`module_name` are generally consumed through `instantiate_class_from_config`
    # so we need to manually remove those values if we wish to use the **kwargs instantiation pattern  # noqa: E501
    profiler_config.pop("class_name")

    profiler: RuleBasedProfiler = RuleBasedProfiler(
        **profiler_config,
        data_context=data_context,
    )

    # BatchRequest yielding exactly one batch
    alice_single_batch_data_batch_request: dict = {
        "datasource_name": "alice_columnar_table_single_batch_datasource",
        "data_connector_name": "alice_columnar_table_single_batch_data_connector",
        "data_asset_name": "alice_columnar_table_single_batch_data_asset",
    }

    result: RuleBasedProfilerResult = profiler.run(
        batch_request=alice_single_batch_data_batch_request
    )

    expectation_suite_name: str = "my_suite"

    suite: ExpectationSuite = result.get_expectation_suite(
        expectation_suite_name=expectation_suite_name
    )

    assert suite is not None and len(suite.expectations) > 0
