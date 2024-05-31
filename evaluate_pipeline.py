from chat_modules.llamaindex import ServiceChatModule
from utils import StandardlizedDeepEvalLLM
from deepeval.test_case import LLMTestCase
from deepeval.metrics import *
from deepeval import evaluate,assert_test
from typing import List,Union
from deepeval.dataset import EvaluationDataset

# Define chat model
chat_service = ServiceChatModule(service_name="GEMINI")
chat_model = chat_service.get_chat_model()

# Define Deep Eval model
model = StandardlizedDeepEvalLLM(model = chat_model)

# Define metrics, for example:
metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4",
    include_reason=True
)

# Define test case, for examples
#test_case = LLMTestCase()
# For more information: https://docs.confident-ai.com/docs/evaluation-test-cases

# Run test case
def evaluate_metrics(test_case :Union[LLMTestCase,List[LLMTestCase],EvaluationDataset],
             metrics: List[BaseMetric]):
    """Evaluate test case based on several metrics"""
    if isinstance(test_case,LLMTestCase):
        assert_test(test_case = test_case, metrics = metrics)
    else:
        evaluate(test_cases = test_case,metrics = metrics)

def evaluate_single_metric(test_case :LLMTestCase,
             metrics: BaseMetric):
    """Evaluate test case based on specified metrics"""
    metric.measure(test_case)
    # Get value
    score = metrics.score
    reason = metrics.reason


