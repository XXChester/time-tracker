from main import *

def test_get_time_ranges_am():
    result = get_time("9:30am")
    assert 9 == result.hour
    assert 30 == result.minute

def test_get_time_ranges_pm():
    result = get_time("1:35pm")
    assert 13 == result.hour
    assert 35 == result.minute

def test_get_time_no_minutes():
    result = get_time("3pm")
    assert 15 == result.hour
    assert 0 == result.minute

def test_hour_and_half():
    test_case = "10:30am-12:00pm"
    result = get_duration(test_case)
    assert 90 == result

def test_15_minutes():
    test_case = "11:55am-12:10pm"
    result = get_duration(test_case)
    assert 15 == result

def test_span_next_day():
    test_case = "11:55pm-12:01am"
    result = get_duration(test_case)
    assert 6 == result

def test_hours_span_next_day():
    test_case = "11pm-1:01am"
    result = get_duration(test_case)
    assert 121 == result


