from __future__ import annotations
from typing import Any, List, Tuple, Optional


class TreeNode:

    def __init__(self, value: Any):
        self._value = value 
        self._children = []  # references to other nodes

    @property
    def value(self) -> Any:
        return self._value

    @property
    def children(self) -> List[TreeNode]:
        return self._children

    def add_child(self, child_node: TreeNode):
        """creates parent-child relationship"""
        print(f"Adding {child_node.value}")
        self._children.append(child_node)

    def remove_child(self, child_node: TreeNode) -> None:
        """Removes parent-child relationship"""
        print(f"Removing {child_node.value} from {self._value}")
        self._children = [child for child in self._children
                          if child is not child_node]

    def traverse(self) -> None:
        """Moves through each node referenced from self downwards.
        (Breadth first search)"""
        nodes_to_visit = [self]  # start with this node
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node._value)
            nodes_to_visit += current_node.children


def dfs(root: TreeNode, 
        target: Any, 
        path: Tuple[TreeNode]=()) -> Optional[str]:
    """Depth first search with a O(n) performance.
    Explores the depth of the tree first. Then backups to parent
    node to revist other children if target was not found"""
    path = path + (root.value,)  # appends parent node to path during recusion

    if root.value == target:  # exit condition for recursion
        return path

    for child in root.children:  # iterate through every child
        path_found = dfs(child, target, path)

        if path_found is not None:  # only append nodes linked to found path
            return path_found

    return None



if __name__ == "__main__":
    root = TreeNode(1)
    branch_1 = TreeNode(2)
    branch_1.add_child(TreeNode(10))
    branch_1.add_child(TreeNode(23))

    branch_2 = TreeNode(3)
    branch_2.add_child(TreeNode(5))
    branch_2.add_child(TreeNode(9))

    root.add_child(branch_1)
    root.add_child(branch_2)

    print(dfs(root, 9))
