import pytest
import os


def test_evaluation_dataset():
    from deepeval.dataset import EvaluationDataset

    csv_filename = "sample.csv"

    csv_file = """id,query,expected_output
    1,"Hello, world!","This is a greeting."
    2,"OpenAI GPT-3","A powerful language model."
    3,"CSV Example","Working with CSV data."
    4,"Python Programming","Coding in Python."
    5,"Data Science","Analyzing data."
    """

    with open(csv_filename, "w") as file:
        file.write(csv_file)

    dataset = EvaluationDataset.from_csv(
        csv_filename,
        query_column="query",
        expected_output_column="expected_output",
        id_column="id",
    )
    assert len(dataset) == 5


@pytest.mark.skip(reason="OpenAI costs")
def test_create_synthetic_dataset():
    """
    test for creating a synthetic dataset
    """
    from deepeval.dataset import create_evaluation_query_output_pairs

    dataset = create_evaluation_query_output_pairs(
        openai_api_key=os.environ["OPENAI_API_KEY"],
        context="FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.",
        n=1,
    )
    assert len(dataset) == 1
