# artifician.extractors package

## artifician.extractors.html_extractors module

### artifician.extractors.html_extractors.count_child_nodes(node: List[str | Tag])

Counts the number of child nodes for a given node.

Args:
: node (List[Union[str, Tag]]): The node list to count children for.

Returns:
: int: The number of child nodes.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

### artifician.extractors.html_extractors.get_child_attribute(node: List[str | Tag], attribute: str)

Retrieves the value of a specified attribute from the first child of a given node.

Args:
: node (List[Union[str, Tag]]): The node list to get the child attribute from.
  attribute (str): The name of the attribute to retrieve.

Returns:
: str: The value of the attribute from the child node.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

### artifician.extractors.html_extractors.get_child_node_text(node: List[str | Tag])

Extracts text from the first child node of a given node.

Args:
: node (List[Union[str, Tag]]): The node list to extract child text from.

Returns:
: str: The text content of the child node.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

### artifician.extractors.html_extractors.get_node_attribute(node: List[str | Tag], attribute: str)

Retrieves the value of a specified attribute from a given node.

Args:
: node (List[Union[str, Tag]]): The node list to get the attribute from.
  attribute (str): The name of the attribute to retrieve.

Returns:
: str: The value of the attribute.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

### artifician.extractors.html_extractors.get_node_text(node: List[str | Tag])

Extracts text from a given node.

Args:
: node (List[Union[str, Tag]]): The node list to extract text from.

Returns:
: str: The text content of the node.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.
  ValueError: If the node list is empty.

### artifician.extractors.html_extractors.get_parent_attribute(node: List[str | Tag], attribute: str)

Retrieves the value of a specified attribute from the parent of a given node.

Args:
: node (List[Union[str, Tag]]): The node list to get the parent attribute from.
  attribute (str): The name of the attribute to retrieve.

Returns:
: str: The value of the attribute from the parent node.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

### artifician.extractors.html_extractors.get_parent_node_text(node: List[str | Tag])

Extracts text from the parent node of a given node.

Args:
: node (List[Union[str, Tag]]): The node list to extract parent text from.

Returns:
: str: The text content of the parent node.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

### artifician.extractors.html_extractors.get_sibling_node_text(node: List[str | Tag])

Extracts text from the first sibling node of a given node.

Args:
: node (List[Union[str, Tag]]): The node list to extract sibling text from.

Returns:
: str: The text content of the sibling node.

Raises:
: TypeError: If the first element in the node list is not a bs4.element.Tag.

## Module contents
