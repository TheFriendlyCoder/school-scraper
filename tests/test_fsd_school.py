from school_scraper.fsdscraper import FSDScraper
from school_scraper.fsdschool import FSDSchool


def test_properties(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    dist = obj.districts[0]
    expected_name = dist.school_names[0]
    res = dist.get_school(expected_name)
    assert res is not None
    assert res.name == expected_name
    assert isinstance(res.messages, str)
    assert isinstance(res.has_late_busses, bool)
    assert isinstance(res.is_open, bool)
    assert isinstance(str(res), str)


def test_all_schools_properties(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    for cur_dist in obj.districts:
        for cur_name in cur_dist.school_names:
            cur_school = cur_dist.get_school(cur_name)
            assert isinstance(cur_school, FSDSchool)
            assert cur_school.name == cur_name
            assert isinstance(cur_school.messages, str)
            assert isinstance(cur_school.has_late_busses, bool)
            assert isinstance(cur_school.is_open, bool)


def test_find_school(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    expected_name = obj.school_names[0]
    result = obj.find_school(expected_name)
    assert isinstance(result, FSDSchool)
    assert result.name == expected_name


def test_find_invalid_school(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    result = obj.find_school("fubar")
    assert result is None


def test_school_closure(fsd_test_data):
    closed_school = "École Régionale de Baie-Sainte-Anne"
    obj = FSDScraper(fsd_test_data)

    result = obj.find_school(closed_school)
    assert isinstance(result, FSDSchool)
    assert result.is_open is False


def test_school_open(fsd_test_data):
    opened_school = "École Clément-Cormier"
    obj = FSDScraper(fsd_test_data)

    result = obj.find_school(opened_school)
    assert isinstance(result, FSDSchool)
    assert result.is_open is True


def test_buses_running(fsd_test_data):
    opened_school = "École Clément-Cormier"
    obj = FSDScraper(fsd_test_data)

    result = obj.find_school(opened_school)
    assert result.are_busses_running is True


def test_buses_not_running(fsd_test_data):
    closed_school = "École Régionale de Baie-Sainte-Anne"
    obj = FSDScraper(fsd_test_data)

    result = obj.find_school(closed_school)
    assert result.are_busses_running is False