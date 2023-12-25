"""
   Copyright 2023 Plato Solutions, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import unittest
from bs4 import BeautifulSoup
from artifician.extractors.html_extractors import (get_node_text, get_node_attribute, get_parent_node_text, 
                         get_child_node_text, count_child_nodes, get_sibling_node_text,
                         get_parent_attribute, get_child_attribute)

class TestHTMLExtractors(unittest.TestCase):
    
    def setUp(self):
        self.html = '''<html><head><title>Test Page</title></head>
                       <body><div id="parent" class="parent-class">
                       <p class="child">Hello, world!</p>
                       <span class="sibling">Hi, sibling!</span>
                       </div></body></html>'''
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.valid_node = [self.soup.find('p')]
        self.invalid_node = ['plain text']
        self.empty_node = []

    def test_get_node_text_valid(self):
        self.assertEqual(get_node_text(self.valid_node), 'Hello, world!')

    def test_get_node_text_invalid(self):
        with self.assertRaises(TypeError):
            get_node_text(self.invalid_node)

    def test_get_node_text_empty(self):
        with self.assertRaises(ValueError):
            get_node_text(self.empty_node)

    def test_get_node_attribute_valid(self):
        self.assertEqual(get_node_attribute(self.valid_node, 'class'), 'child')

    def test_get_node_attribute_invalid(self):
        with self.assertRaises(TypeError):
            get_node_attribute(self.invalid_node, 'class')

    def test_get_parent_node_text_valid(self):
        self.assertEqual(get_parent_node_text(self.valid_node), 'Hello, world!\nHi, sibling!')

    def test_get_parent_node_text_invalid(self):
        with self.assertRaises(TypeError):
            get_parent_node_text(self.invalid_node)

    def test_get_child_node_text_valid(self):
        self.assertEqual(get_child_node_text(self.valid_node), "Hi, sibling!")

    def test_get_child_node_text_invalid(self):
        with self.assertRaises(TypeError):
            get_child_node_text(self.invalid_node)

    def test_count_child_nodes_valid(self):
        self.assertEqual(count_child_nodes(self.valid_node), 0)

    def test_count_child_nodes_invalid(self):
        with self.assertRaises(TypeError):
            count_child_nodes(self.invalid_node)

    def test_get_sibling_node_text_valid(self):
        self.assertEqual(get_sibling_node_text(self.valid_node), 'Hi, sibling!')

    def test_get_sibling_node_text_invalid(self):
        with self.assertRaises(TypeError):
            get_sibling_node_text(self.invalid_node)

    def test_get_parent_attribute_valid(self):
        self.assertEqual(get_parent_attribute(self.valid_node, 'id'), 'parent')

    def test_get_parent_attribute_invalid(self):
        with self.assertRaises(TypeError):
            get_parent_attribute(self.invalid_node, 'id')

    def test_get_child_attribute_valid(self):
        self.assertEqual(get_child_attribute(self.valid_node, 'class'), 'sibling')

    def test_get_child_attribute_invalid(self):
        with self.assertRaises(TypeError):
            get_child_attribute(self.invalid_node, 'class')

if __name__ == '__main__':
    unittest.main()
