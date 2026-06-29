import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def dash_app(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    return dash_duo


def test_header_is_present(dash_app):
    dash_app.wait_for_element("#header", timeout=10)
    header = dash_app.find_element("#header")
    assert header is not None
    assert "Pink Morsel" in header.text


def test_chart_is_present(dash_app):
    dash_app.wait_for_element("#sales-chart", timeout=10)
    chart = dash_app.find_element("#sales-chart")
    assert chart is not None


def test_region_picker_is_present(dash_app):
    dash_app.wait_for_element("#region-picker", timeout=10)
    picker = dash_app.find_element("#region-picker")
    assert picker is not None
