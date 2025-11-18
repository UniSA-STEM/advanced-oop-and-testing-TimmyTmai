'''
File: test_helper.py
Description: Tests for validation helper functions.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
import helper


def test_validate_string_valid():
    assert helper.validate_string("Lion", "name") is True


def test_validate_string_empty():
    assert helper.validate_string("", "name") is False


def test_validate_string_whitespace_only():
    assert helper.validate_string("   ", "name") is False


def test_validate_string_wrong_type():
    assert helper.validate_string(123, "name") is False



@pytest.mark.parametrize("level", ["low", "medium", "high", "LOW", " High "])
def test_validate_level_valid(level):
    assert helper.validate_level(level, "severity") is True


def test_validate_level_invalid_value():
    assert helper.validate_level("urgent", "severity") is False


def test_validate_level_non_string():
    assert helper.validate_level(10, "severity") is False


def test_validate_date_valid_format():
    assert helper.validate_date("25/12/2024", "date_reported") is True


@pytest.mark.parametrize("date_str", ["2024-12-25", "25-12-2024", "not a date"])
def test_validate_date_invalid_format(date_str):
    assert helper.validate_date(date_str, "date_reported") is False


def test_validate_date_non_string():
    assert helper.validate_date(20241225, "date_reported") is False


@pytest.mark.parametrize("value", [True, False])
def test_validate_bool_valid(value):
    assert helper.validate_bool(value, "active") is True


@pytest.mark.parametrize("value", [1, 0, "True", None])
def test_validate_bool_invalid(value):
    assert helper.validate_bool(value, "active") is False


@pytest.mark.parametrize("age", [0, 5, 120])
def test_validate_age_valid(age):
    assert helper.validate_age(age) is True


def test_validate_age_negative():
    assert helper.validate_age(-1) is False


def test_validate_age_too_large():
    assert helper.validate_age(300) is False


def test_validate_age_wrong_type():
    assert helper.validate_age("five") is False


def test_validate_environment_valid_lowercase():
    env = helper.validate_environment("savannah")
    assert env == "savannah"


def test_validate_environment_valid_mixed_case():
    env = helper.validate_environment(" Forest ")
    assert env == "forest"


def test_validate_environment_invalid_value():
    with pytest.raises(ValueError):
        helper.validate_environment("ocean", "environment")


def test_validate_environment_wrong_type():
    with pytest.raises(TypeError):
        helper.validate_environment(123, "environment")


def test_validate_issue_valid():
    # VALID_ISSUES = ["injuries", "illness", "behavioral concerns"]
    iss = helper.validate_issue("Injuries", "issue")
    assert iss == "injuries"


def test_validate_issue_invalid_value():
    with pytest.raises(ValueError):
        helper.validate_issue("flu", "issue")


def test_validate_issue_wrong_type():
    with pytest.raises(TypeError):
        helper.validate_issue(123, "issue")
