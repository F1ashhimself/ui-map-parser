# -*- coding: utf-8 -*-

__author__ = 'f1ashhimself@gmail.com'

import pytest

from hamcrest import assert_that, equal_to, raises

from ui_map_parser import UIMapException


def test_simple_element(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('SimpleELEMENT')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div'))


def test_element_with_different_cased_properties(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('ElementWithDifferentCasedProperties')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div'))


def test_element_without_type(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('ElementWithoutType')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div'))


def test_element_with_parent_in_common(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('Foo.ElementWithParent')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div/span'))


def test_element_with_parent_not_in_common(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('ElementWithParent')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('/div[@id="some_id"]'))


def test_element_with_template(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('ElementWithTemplate', template={'id_name': 'some_id'})
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div[@id="some_id"]'))


def test_element_with_template_in_parent(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('Foo.ElementWithTemplateInParent',
                                                          template={'id_name': 'some_id'})
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div[@id="some_id"]/span'))


@pytest.mark.parametrize('ui_map_parser', ['en'], indirect=True)
def test_element_with_different_language(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('ElementWithSelectorForEnLanguage')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('//div[text()="some text"]'))


def test_file_not_found(ui_map_parser):
    file_name = 'UnexistingFile'
    assert_that(lambda: ui_map_parser.parse_element(f'{file_name}.UnexistingElement'),
                raises(UIMapException, f'File "{file_name.lower()}" was not found.'))


def test_element_not_found(ui_map_parser):
    element_name = 'UnexistingElement'
    assert_that(lambda: ui_map_parser.parse_element(element_name),
                raises(UIMapException, f'Element "{element_name}" was not found.'))


def test_element_with_parent_but_different_types(ui_map_parser):
    element_name = 'Foo.ElementWithParentDifferentTypes'
    assert_that(lambda: ui_map_parser.parse_element(element_name),
                raises(UIMapException,
                       f'"{element_name}" element and "SimpleElement" element have different element '
                       f'types.'))


def test_element_with_different_register(ui_map_parser):
    selector_type, selector = ui_map_parser.parse_element('bAr.ElementWithDifferentREgister')
    assert_that(selector_type, equal_to('xpath'))
    assert_that(selector, equal_to('/div/span'))
