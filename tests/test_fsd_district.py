from school_scraper.fsdscraper import FSDScraper
from school_scraper.fsdschool import FSDSchool


def test_properties(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    expected_name = obj.district_names[0]
    res = obj.get_district(expected_name)
    assert res is not None
    assert res.name == expected_name
    assert isinstance(str(res), str)


def test_schools(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.districts[0]
    assert isinstance(res.schools, list)
    assert len(res.schools) > 0
    for cur_school in res.schools:
        assert isinstance(cur_school, FSDSchool)


def test_school_names(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.districts[0]
    assert isinstance(res.school_names, list)
    assert len(res.school_names) > 0
    assert len(res.schools) == len(res.school_names)

    for cur_name in res.school_names:
        assert isinstance(cur_name, str)
        assert len(cur_name) > 0


def test_get_school(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.districts[0]

    school = res.get_school(res.school_names[0])
    assert isinstance(school, FSDSchool)


def test_get_school_invalid(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.districts[0]

    school = res.get_school("fubar was here")
    assert school is None


def test_get_all_schools(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.districts[0]
    for cur_name in res.school_names:
        assert res.get_school(cur_name) is not None
