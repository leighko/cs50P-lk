from adieu import ask_and_store_name, convert_names_to_string
import pytest


def test_ask():
    assert ask_and_store_name("") == ["Leigh"]


def test_ask_two():
    assert ask_and_store_name("") == ["Leigh", "Cody"]


def test_convert_one():
    assert convert_names_to_string(["Elsie"]) == "Elsie"


def test_convert_two():
    assert convert_names_to_string(["Elsie", "Fitz"]) == "Elsie and Fitz"


def test_convert_three():
    assert convert_names_to_string(["Elsie", "Fitz", "Rose"]) == "Elsie, Fitz, and Rose"


def test_convert_four():
    assert convert_names_to_string(["Elsie", "Fitz", "Rose", "Poe"]) == "Elsie, Fitz, Rose, and Poe"