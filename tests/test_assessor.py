import pytest
from fair_hubmap.assessor import Assessor, FAIRReport

def test_assessor_initialization():
    assessor = Assessor(dataset_id="HBM123.ABCD.456")
    assert assessor.dataset_id == "HBM123.ABCD.456"
    assert assessor.api_url == "https://portal.hubmapconsortium.org"

def test_evaluate_placeholder():
    assessor = Assessor(dataset_id="HBM123.ABCD.456")
    report = assessor.evaluate()
    assert isinstance(report, FAIRReport)
    assert 0 <= report.findable <= 1
    assert 0 <= report.accessible <= 1
    assert 0 <= report.interoperable <= 1
    assert 0 <= report.reusable <= 1
