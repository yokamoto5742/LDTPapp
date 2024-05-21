import pytest
from main import (
    MainDisease, SheetName, TemplateManager,
    load_patient_data, load_main_diseases, load_sheet_names, format_date)


@pytest.fixture
def template_manager():
    return TemplateManager()

def test_load_patient_data():
    data = load_patient_data()
    assert not data.empty
    assert data.shape[1] == 15

def test_load_main_diseases(mocker):
    mock_session = mocker.patch("your_module.Session")
    mock_session.return_value.query.return_value.all.return_value = [
        MainDisease(id=1, name="Test Disease 1"),
        MainDisease(id=2, name="Test Disease 2"),
    ]
    options = load_main_diseases()
    assert len(options) == 2
    assert options[0].key == "Test Disease 1"
    assert options[1].key == "Test Disease 2"

def test_load_sheet_names(mocker):
    mock_session = mocker.patch("your_module.Session")
    mock_session.return_value.query.return_value.filter.return_value.all.return_value = [
        SheetName(id=1, name="Test Sheet 1"),
        SheetName(id=2, name="Test Sheet 2"),
    ]
    options = load_sheet_names(1)
    assert len(options) == 2
    assert options[0].key == "Test Sheet 1"
    assert options[1].key == "Test Sheet 2"

def test_format_date():
    assert format_date("2023-04-18") == "2023/04/18"
    assert format_date(None) == ""
