from school_scraper.fsdscraper import FSDScraper
from school_scraper.fsddistrict import FSDDistrict


def test_init(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    assert isinstance(str(obj), str)


def test_validate(fsd_test_data):
    assert FSDScraper.validate(fsd_test_data) is True


def test_validate_no_tables():
    sample = """
    <!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title></title></head>
<body>
</body>
</html>
"""
    assert FSDScraper.validate(sample) is False


def test_validate_invalid_html():
    sample = """fubar was here"""
    assert FSDScraper.validate(sample) is False


def test_validate_multiple_tables():
    sample = """
    <!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title></title></head>
<body>
<table>
    <tr>
		<td class="tblH0">Région</td>
		<td class="tblH1">Nom de l'école</td>
		<td class="tblH2">École</td>
		<td class="tblH3">Autobus</td>
		<td class="tblH4">Messages</td>
	</tr>
    <tr>
		<td>BAIE-SAINTE-ANNE</td>
		<td>École Régionale de Baie-Sainte-Anne</td>
		<td class="tblC2">Ouvert</td>
		<td class="tblC3">À l’heure</td>
		<td></td>
	</tr>
</table>
<table>
    <tr>
		<td class="tblH0">Région</td>
		<td class="tblH1">Nom de l'école</td>
		<td class="tblH2">École</td>
		<td class="tblH3">Autobus</td>
		<td class="tblH4">Messages</td>
	</tr>
	<tr>
		<td>BOUCTOUCHE</td>
		<td>École Clément-Cormier</td>
		<td class="tblC2">Ouvert</td>
		<td class="tblC3">À l’heure</td>
		<td></td>
	</tr>
</table>
</body>
</html>
"""
    assert FSDScraper.validate(sample) is False


def test_validate_empty_school_name():
    sample = """
    <!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title></title></head>
<body>
<table>
    <tr>
		<td class="tblH0">Région</td>
		<td class="tblH1">Nom de l'école</td>
		<td class="tblH2">École</td>
		<td class="tblH3">Autobus</td>
		<td class="tblH4">Messages</td>
	</tr>
    <tr>
		<td>BAIE-SAINTE-ANNE</td>
		<td></td>
		<td class="tblC2">Ouvert</td>
		<td class="tblC3">À l’heure</td>
		<td></td>
	</tr>
</table>
</body>
</html>
"""
    assert FSDScraper.validate(sample) is False


def test_validate_duplicate_school_names():
    sample = """
    <!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title></title></head>
<body>
<table>
    <tr>
		<td class="tblH0">Région</td>
		<td class="tblH1">Nom de l'école</td>
		<td class="tblH2">École</td>
		<td class="tblH3">Autobus</td>
		<td class="tblH4">Messages</td>
	</tr>
    <tr>
		<td>BAIE-SAINTE-ANNE</td>
		<td>École Régionale de Baie-Sainte-Anne</td>
		<td class="tblC2">Ouvert</td>
		<td class="tblC3">À l’heure</td>
		<td></td>
	</tr>
	<tr>
		<td>BOUCTOUCHE</td>
		<td>École Régionale de Baie-Sainte-Anne</td>
		<td class="tblC2">Ouvert</td>
		<td class="tblC3">À l’heure</td>
		<td></td>
	</tr>
</table>
</body>
</html>
"""
    assert FSDScraper.validate(sample) is False


def test_validate_empty_district_name():
    sample = """
    <!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title></title></head>
<body>
<table>
    <tr>
		<td class="tblH0">Région</td>
		<td class="tblH1">Nom de l'école</td>
		<td class="tblH2">École</td>
		<td class="tblH3">Autobus</td>
		<td class="tblH4">Messages</td>
	</tr>
    <tr>
		<td></td>
		<td>École Régionale de Baie-Sainte-Anne</td>
		<td class="tblC2">Ouvert</td>
		<td class="tblC3">À l’heure</td>
		<td></td>
	</tr>
</table>
</body>
</html>
"""
    assert FSDScraper.validate(sample) is False


def test_districts(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    assert isinstance(obj.districts, list)
    assert len(obj.districts) > 0
    for cur_dist in obj.districts:
        assert isinstance(cur_dist, FSDDistrict)


def test_district_names(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    assert isinstance(obj.district_names, list)
    assert len(obj.district_names) > 0
    assert len(obj.district_names) == len(obj.districts)

    for cur_name in obj.district_names:
        assert isinstance(cur_name, str)
        assert len(cur_name) > 0


def test_school_names(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    assert isinstance(obj.school_names, list)
    assert len(obj.school_names) > 0
    for cur_name in obj.school_names:
        assert isinstance(cur_name, str)
        assert len(cur_name) > 0


def test_get_district(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.get_district(obj.district_names[0])
    assert isinstance(res, FSDDistrict)


def test_get_district_invalid(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    res = obj.get_district("fubar was here")
    assert res is None


def test_get_all_districts(fsd_test_data):
    obj = FSDScraper(fsd_test_data)
    for cur_name in obj.district_names:
        assert isinstance(obj.get_district(cur_name), FSDDistrict)
