import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval_junit_reporter import assert_test_with_junit_report

def test_chatbot():
    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5
    )
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output from your LLM application
        actual_output="You have 30 days to get a full refund at no extra cost.",
        expected_output="We offer a 30-day full refund at no extra costs.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra costs."]
    )

    assert_test_with_junit_report(test_case, [correctness_metric], output_path="test_reports/deepeval_results.xml")

def test_testbusters_night():

    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.8,
        verbose_mode=True
    )

    relevancy_metric = AnswerRelevancyMetric(
        threshold=0.8,
        include_reason=True
    )

    testbusters_night_test_case = LLMTestCase(
        input="Is Testbusters Night in Vienna an amazing event?",
        actual_output="Yes, TestBusters Night is a great event in Vienna for testers and qa professionals with great talks and a lovely host. And Vienna has great Schnitzel.",
        expected_output="Yes, TestBusters Night in Vienna is widely considered an excellent, high-energy event for software testing and QA professionals, with great talks and networking."
    )

    assert_test_with_junit_report(testbusters_night_test_case, [correctness_metric, relevancy_metric], output_path="test_reports/deepeval_results.xml")