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
