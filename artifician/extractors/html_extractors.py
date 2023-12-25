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
from bs4 import Tag
from typing import List, Union

def get_node_text(node: List[Union[str, Tag]]) -> str:
    """
    Extracts text from a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to extract text from.

    Returns:
        str: The text content of the node.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
        ValueError: If the node list is empty.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")
    
    actual_node = node[0] if type(node) is list else node
    
    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")
    
    return actual_node.text.strip()

def get_node_attribute(node: List[Union[str, Tag]], attribute: str) -> str:
    """
    Retrieves the value of a specified attribute from a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to get the attribute from.
        attribute (str): The name of the attribute to retrieve.

    Returns:
        str: The value of the attribute.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")
    
    actual_node = node[0] if type(node) is list else node
    
    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")
    
    return " ".join(actual_node.get(attribute, ""))

def get_parent_node_text(node: List[Union[str, Tag]]) -> str:
    """
    Extracts text from the parent node of a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to extract parent text from.

    Returns:
        str: The text content of the parent node.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")

    actual_node = node[0] if type(node) is list else node if type(node) is list else node

    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")

    parent_node = actual_node.find_parent()

    return parent_node.text.strip() if parent_node else ""

def get_child_node_text(node: List[Union[str, Tag]]) -> str:
    """
    Extracts text from the first child node of a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to extract child text from.

    Returns:
        str: The text content of the child node.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")

    actual_node = node[0] if type(node) is list else node

    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")

    child_node = actual_node.find_next()

    return child_node.text.strip() if child_node else ""

def count_child_nodes(node: List[Union[str, Tag]]) -> int:
    """
    Counts the number of child nodes for a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to count children for.

    Returns:
        int: The number of child nodes.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")

    actual_node = node[0] if type(node) is list else node

    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")

    return len(actual_node.find_all())

def get_sibling_node_text(node: List[Union[str, Tag]]) -> str:
    """
    Extracts text from the first sibling node of a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to extract sibling text from.

    Returns:
        str: The text content of the sibling node.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")

    actual_node = node[0] if type(node) is list else node

    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")

    sibling_node = actual_node.find_next_sibling()

    return sibling_node.text.strip() if sibling_node else ""

def get_parent_attribute(node: List[Union[str, Tag]], attribute: str) -> str:
    """
    Retrieves the value of a specified attribute from the parent of a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to get the parent attribute from.
        attribute (str): The name of the attribute to retrieve.

    Returns:
        str: The value of the attribute from the parent node.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")
    actual_node = node[0] if type(node) is list else node

    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")

    parent_node = actual_node.find_parent()
    attribute = parent_node.get(attribute, "") if parent_node else ""

    return "".join(attribute) if type(attribute) is list else attribute

def get_child_attribute(node: List[Union[str, Tag]], attribute: str) -> str:
    """
    Retrieves the value of a specified attribute from the first child of a given node.

    Args:
        node (List[Union[str, Tag]]): The node list to get the child attribute from.
        attribute (str): The name of the attribute to retrieve.

    Returns:
        str: The value of the attribute from the child node.
        
    Raises:
        TypeError: If the first element in the node list is not a bs4.element.Tag.
    """
    if not node:
        raise ValueError("Node list cannot be empty.")
    actual_node = node[0] if type(node) is list else node
    
    if not isinstance(actual_node, Tag):
        raise TypeError(f"Expected a bs4.element.Tag, got {type(actual_node)} instead.")

    child_node = actual_node.find_next()
    return " ".join(child_node.get(attribute, "")) if child_node else ""