import pytest
import requests
from pathlib import Path
from school_scraper.fsdscraper import FSDScraper

SAMPLE_RESPONSE = """"""
TEST_DIR = Path(__file__).parent
SAMPLE_DATA = TEST_DIR.joinpath("sample.html")


@pytest.fixture(scope="session")
def fsd_test_data(request):

    update = request.config.getoption("--update")
    if update:
        temp = requests.get(FSDScraper.SCHEDULE_URL).text

        with SAMPLE_DATA.open("w") as fh:
            fh.write(temp)

    use_live = request.config.getoption("--live")
    if use_live:
        retval = requests.get(FSDScraper.SCHEDULE_URL).text
    else:
        with SAMPLE_DATA.open() as fh:
            retval = fh.read()

    yield retval


def pytest_addoption(parser):
    """Customizations for the py.test command line options"""
    parser.addoption(
        "--live",
        action="store_true",
        help="use live response data loaded from actual school websites"
    )
    parser.addoption(
        "--update",
        action="store_true",
        help="regenerate sample data from live school websites"
    )