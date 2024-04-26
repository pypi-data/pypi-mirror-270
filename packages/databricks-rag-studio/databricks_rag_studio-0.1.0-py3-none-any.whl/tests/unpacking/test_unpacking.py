import datetime
import json

import pandas as pd
import pytest
from databricks.rag.unpacking import unpack_and_split_payloads
from databricks.rag.unpacking.schemas import (
    ASSESSMENT_LOG_SCHEMA,
    REQUEST_LOG_SCHEMA,
    REQUEST_LOG_V2_SCHEMA,
)
from pyspark.sql import types as T

from .eval_test_utils import schemas_equal

_INFERENCE_TABLE_PAYLOD_SCHEMA = T.StructType(
    [
        T.StructField("client_request_id", T.StringType()),
        T.StructField("databricks_request_id", T.StringType()),
        T.StructField("date", T.DateType()),
        T.StructField("timestamp_ms", T.LongType()),
        T.StructField("status_code", T.StringType()),
        T.StructField("execution_time_ms", T.LongType()),
        T.StructField("request", T.StringType()),
        T.StructField("response", T.StringType()),
        T.StructField("sampling_fraction", T.DoubleType()),
        T.StructField("request_metadata", T.StringType()),
    ]
)


@pytest.fixture()
def sample_requests():
    return [
        # A RAG request
        """
            {
              "messages": [
                {
                  "role": "user",
                  "content": "Is mlflow good?"
                }
              ],
              "databricks_options": {
                "return_trace": true,
                "conversation_id": "123456"
              }
            }
            """,
        # A text assessment request
        """
            {
              "dataframe_records": [
                {
                  "request_id": "24680",
                  "source" : {
                    "type": "end_user",
                    "id" : "alkis"
                  },
                  "text_assessments": [{
                    "step_id": "0123",
                    "ratings": {
                      "harmful": {
                        "value": true,
                        "rationale": "too mean"
                      }
                    },
                    "suggested_output": "We have 2 months of vacation",
                    "free_text_comment": "I really didn't like the answer because..."
                  }]
                }
              ]
            }
            """,
        # A retrieval assessment request with multiple assessments
        """
            {
              "dataframe_records": [
                {
                  "request_id": "35209",
                  "source" : {
                    "type": "expert",
                    "id" : "ali-ghodsi"
                  },
                  "retrieval_assessments": [
                    {
                      "step_id": "0123",
                      "position": 0,
                      "ratings": {
                        "relevant": {
                          "value": false,
                          "rationale": "too long"
                        }
                      },
                      "free_text_comment": "I'm leaving a comment!"
                    },
                    {
                      "step_id": "0123",
                      "position": 1,
                      "ratings": {
                        "relevant": {
                          "value": true,
                          "rationale": "spot on"
                        }
                      }
                    }
                  ]
                }
              ]
            }
            """,
        # An erroneous request that will be filtered out
        "blah",
        # An assessment request with both text and retrieval assessments
        """
            {
              "dataframe_records": [
                {
                  "request_id": "729962",
                  "source" : {
                    "type": "expert",
                    "id" : "corey_zumar",
                    "tags": {}
                  },
                  "text_assessments": [{
                    "step_id": "012233",
                    "ratings": {
                      "faithfulness": {
                        "value": false,
                        "rationale": "unfaithful"
                      }
                    }
                  }],
                  "retrieval_assessments": [
                    {
                      "step_id": "0123",
                      "position": 0,
                      "ratings": {
                        "relevant": {
                          "value": false,
                          "rationale": "too long"
                        }
                      },
                      "free_text_comment": "I'm leaving a comment!"
                    },
                    {
                      "step_id": "0123",
                      "position": 1,
                      "ratings": {
                        "faithful": {
                          "value": true,
                          "rationale": "spot on"
                        }
                      }
                    }
                  ]
                }
              ]
            }
            """,
    ]


@pytest.fixture()
def sample_rag_response():
    return """
            {
              "object": "chat.completion",
              "created": 1705451212,
              "choices": [
                {
                  "index": 0,
                  "message": {"role": "assistant", "content": "MLflow is amazing!"}
                }
              ],
              "id": "12345",
              "databricks_output" : {
                "trace": {
                  "app_version_id": "avi123",
                  "start_timestamp": "2024-01-03T19:51:10.686454",
                  "end_timestamp": "2024-01-03T19:51:24.932795",
                  "is_truncated": false,
                  "steps": [
                      {
                        "step_id": "29470854",
                        "name": "Retriever",
                        "type": "RETRIEVAL",
                        "retrieval": {
                          "query_text": "What did the president say about the economy?",
                          "chunks": [
                            {
                              "chunk_id": "a0251297-78e4-407c-aeb4-7bb6410ccc2d",
                              "content": "Vice President Harris and I ran for office with a new vision for America.",
                              "doc_uri": null
                            },
                            {
                              "chunk_id": "21a53baa-65b0-450d-8d38-6314eb8a2383",
                              "content": "And so many families are living paycheck to paycheck, struggling to keep up...",
                              "doc_uri": null
                            }
                          ]
                        },
                        "start_timestamp": "2024-01-03T19:51:10.686454",
                        "end_timestamp": "2024-01-03T19:51:11.290311"
                      },
                      {
                        "step_id": "00928383",
                        "name": "LLM",
                        "type": "LLM_GENERATION",
                        "text_generation": {
                          "prompt": "Human",
                          "generated_text": "The president"
                        },
                        "start_timestamp": "2024-01-03T19:51:11.292079",
                        "end_timestamp": "2024-01-03T19:51:24.932795"
                      },
                      {
                        "step_id": "87620983",
                        "name": "LLM",
                        "type": "LLM_GENERATION",
                        "text_generation": {
                          "prompt": "Human",
                          "generated_text": "The president"
                        },
                        "start_timestamp": "2024-01-03T19:51:11.292079",
                        "end_timestamp": "2024-01-03T19:51:24.932795"
                      }
                  ]
                }
              }
            }
            """


def sample_payload_logs(spark, sample_requests, rag_response):
    payload_data = {
        "client_request_id": [None, None, None, None, None],
        "databricks_request_id": ["12345", "67890", "099883", "204838", "709714"],
        "date": [
            datetime.date(2023, 1, 1),
            datetime.date(2023, 1, 2),
            datetime.date(2023, 1, 3),
            datetime.date(2023, 1, 4),
            datetime.date(2023, 1, 5),
        ],
        "timestamp_ms": [
            1609459200000,
            1609459200001,
            1609459200002,
            1609459200003,
            1609459200004,
        ],
        "status_code": ["200", "200", "200", "404", "200"],
        "execution_time_ms": [37, 73, 92, 22, 11],
        "request": sample_requests,
        "response": [
            # A RAG response
            rag_response,
            # A text assessment response
            "",
            # A retrieval assessment response
            "",
            # An erroneous request response
            "",
            # A text and retrieval assessment response
            "",
        ],
        "sampling_fraction": [1.0, 1.0, 1.0, 1.0, 1.0],
        "request_metadata": [None, None, None, None, None],
    }
    return spark.createDataFrame(
        pd.DataFrame(payload_data),
        _INFERENCE_TABLE_PAYLOD_SCHEMA,
    )


# Our unpacking logic uses edge Spark features, namely the ":" query notation for semi-structured data.
@pytest.mark.edge_spark
def test_unpack_and_split_payloads(spark, sample_requests, sample_rag_response):
    payloads = sample_payload_logs(spark, sample_requests, sample_rag_response)
    request_log, assessment_log = unpack_and_split_payloads(payloads)

    # Check that the schema of the resulting DataFrames is correct
    assert schemas_equal(request_log.schema, REQUEST_LOG_SCHEMA)
    assert schemas_equal(assessment_log.schema, ASSESSMENT_LOG_SCHEMA)

    # Check the row counts for the resulting DataFrames
    # We have 5 payloads in the sample data, but 1 is an erroneous request that will be filtered out
    # The request payload results in 1 row
    # The text assessment payload results in 1 row +
    # The retrieval assessment payload results in 2 rows +
    # The combined assessment payload results in 3 more rows (1 text + 2 retrieval)
    expected_request_log_count = 1
    expected_assessment_log_count = 1 + 2 + (1 + 2)
    request_log_count = request_log.count()
    assessment_log_count = assessment_log.count()
    assert (
        request_log_count == expected_request_log_count
    ), f"expected {expected_request_log_count} rows, got {request_log_count}"
    assert (
        assessment_log_count == expected_assessment_log_count
    ), f"expected {expected_assessment_log_count} rows, got {assessment_log_count}"

    # Spot check a few values in the request log
    request_log_values = request_log.collect()[0].asDict()
    assert request_log_values["request"]["last_input"] == "Is mlflow good?"
    assert (
        request_log_values["trace"]["steps"][0]["retrieval"]["chunks"][0]["content"]
        == "Vice President Harris and I ran for office with a new vision for America."
    )
    assert (
        request_log_values["output"]["choices"][0]["message"]["content"]
        == "MLflow is amazing!"
    )

    # Spot check a few values in the assessment log
    assessment_log_values = assessment_log.collect()[0].asDict()
    assert (
        assessment_log_values["text_assessment"]["ratings"]["harmful"]["rationale"]
        == "too mean"
    )
    assert assessment_log_values["retrieval_assessment"] is None


@pytest.fixture()
def sample_rag_response_v2():
    trace = {
        "mlflow.trace_schema.version": 2,
        "spans": [
            {
                "name": "LLMChain",
                "context": {
                    "span_id": "ec0d493e-f07a-4ea6-9ea3-c25995baf9e6",
                    "trace_id": "",
                },
                "parent_id": None,
                "start_time": 1713229821507930112,
                "end_time": 1713229821511368960,
                "status_code": "OK",
                "status_message": "",
                "attributes": json.dumps(
                    {
                        "mlflow.spanInputs": {"product": "MLflow"},
                        "mlflow.spanOutputs": {"text": "test"},
                        "mlflow.spanType": "CHAIN",
                    }
                ),
                "events": [
                    {
                        "name": "start",
                        "timestamp": 1713229821507930112,
                        "attributes": "{}",
                    },
                    {
                        "name": "end",
                        "timestamp": 1713229821511368960,
                        "attributes": "{}",
                    },
                ],
            },
            {
                "name": "OpenAI",
                "context": {
                    "span_id": "cb8124ef-3938-41fb-8559-1ab63087f93e",
                    "trace_id": "",
                },
                "parent_id": "ec0d493e-f07a-4ea6-9ea3-c25995baf9e6",
                "start_time": 1713229821508729856,
                "end_time": 1713229821511215872,
                "status_code": "OK",
                "status_message": "",
                "attributes": json.dumps(
                    {
                        "invocation_params": {
                            "model_name": "gpt-3.5-turbo-instruct",
                            "temperature": 0.9,
                            "top_p": 1,
                            "frequency_penalty": 0,
                            "presence_penalty": 0,
                            "n": 1,
                            "logit_bias": {},
                            "max_tokens": 256,
                            "_type": "openai",
                            "stop": None,
                        },
                        "options": {"stop": None},
                        "batch_size": 1,
                        "mlflow.spanInputs": {
                            "prompt": "What is a good name for a company that makes MLflow?"
                        },
                        "mlflow.spanOutputs": {"generated_text": "test"},
                        "mlflow.spanType": "LLM",
                    }
                ),
                "events": [
                    {
                        "name": "start",
                        "timestamp": 1713229821508729856,
                        "attributes": "{}",
                    },
                    {
                        "name": "end",
                        "timestamp": 1713229821511215872,
                        "attributes": "{}",
                    },
                ],
            },
        ],
        "start_timestamp": "2024-04-16T01:10:21.507930",
        "end_timestamp": "2024-04-16T01:10:21.511369",
        "app_version_id": "avi123",
        "is_truncated": False,
    }
    response = {
        "object": "chat.completion",
        "created": 1705451212,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": "MLflow is amazing!"},
            }
        ],
        "id": "12345",
        "databricks_output": {"trace": trace},
    }
    return json.dumps(response)


@pytest.mark.edge_spark
def test_unpack_and_split_payloads_trace_v2(
    spark, sample_requests, sample_rag_response_v2, monkeypatch
):
    monkeypatch.setenv("RAG_TRACE_V2_ENABLED", "true")
    payloads = sample_payload_logs(spark, sample_requests, sample_rag_response_v2)
    request_log, assessment_log = unpack_and_split_payloads(payloads)

    # Check that the schema of the resulting DataFrames is correct
    assert schemas_equal(request_log.schema, REQUEST_LOG_V2_SCHEMA)
    assert schemas_equal(assessment_log.schema, ASSESSMENT_LOG_SCHEMA)

    # Check the row counts for the resulting DataFrames
    # We have 5 payloads in the sample data, but 1 is an erroneous request that will be filtered out
    # The request payload results in 1 row
    # The text assessment payload results in 1 row +
    # The retrieval assessment payload results in 2 rows +
    # The combined assessment payload results in 3 more rows (1 text + 2 retrieval)
    expected_request_log_count = 1
    expected_assessment_log_count = 1 + 2 + (1 + 2)
    request_log_count = request_log.count()
    assessment_log_count = assessment_log.count()
    assert (
        request_log_count == expected_request_log_count
    ), f"expected {expected_request_log_count} rows, got {request_log_count}"
    assert (
        assessment_log_count == expected_assessment_log_count
    ), f"expected {expected_assessment_log_count} rows, got {assessment_log_count}"

    # Spot check a few values in the request log
    request_log_values = request_log.collect()[0].asDict()
    attributes = request_log_values["trace"]["spans"][0]["attributes"]
    assert attributes == json.dumps(
        {
            "mlflow.spanInputs": {"product": "MLflow"},
            "mlflow.spanOutputs": {"text": "test"},
            "mlflow.spanType": "CHAIN",
        }
    )

    assert (request_log_values["request_id"]) == "12345"
    assert (request_log_values["timestamp"]) == datetime.datetime(2021, 1, 1, 0, 0)
    assert (request_log_values["app_version_id"]) == "avi123"
    assert (request_log_values["last_request_input"]) == "Is mlflow good?"
    assert request_log_values["response_output"] == "MLflow is amazing!"

    assert request_log_values["request"]["last_input"] == "Is mlflow good?"
    assert (
        request_log_values["output"]["choices"][0]["message"]["content"]
        == "MLflow is amazing!"
    )

    # Spot check a few values in the assessment log
    assessment_log_values = assessment_log.collect()[0].asDict()
    assert assessment_log_values["request_id"] == "24680"
    assert (
        assessment_log_values["text_assessment"]["ratings"]["harmful"]["rationale"]
        == "too mean"
    )
    assert assessment_log_values["retrieval_assessment"] is None
