from abc import ABC, abstractmethod


class NodeData:
    def __init__(self, value, color, number):
        self.value = value
        self.color = color
        self.number = number

    def set_node(self, value, color, number):
        self.value = value
        self.color = color
        self.number = number

    def get_node(self, value, color, number):
        return self.value, self.color, self.number


class TreeNode(NodeData):
    def __init__(self, children = []):
        self.children = []
        self.depth = 0

    def add_children(self, child):
        self.children.append(child)
        return self.children

    def set_children(self, children):
        self.children = children

    def get_children(self, children):
        return self.children


class Tree:
    nodes = []

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def getValue(self, node_number):
        return self.nodes[node_number - 1].value

    def getColor(self, node_number):
        return self.nodes[node_number - 1].color

    def getDepth(self, node_number):
        root_node = 0
        node_depth = 0
        current_node_number = node_number
        if node_number != root_node:
            for child in reversed(child_list):
                if child[1] == current_node_number:
                    node_depth += 1
                    current_node_number = child[0]

        return node_depth


class TreeVis(ABC):
    def __int__(self):
        super().__init__()

    @abstractmethod
    def getResult(self):
        pass

    @abstractmethod
    def visitNode(self, treeNode):
        pass

    @abstractmethod
    def visitLeaf(self, treeLeaf):
        pass


class SumInLeavesVisitor(TreeVis):
    result = 0

    def getResult(self):
        return self.result

    def visitNode(self, treeNode : Tree):
        pass

    def visitLeaf(self, treeLeaf : Tree):
        for current_node in treeLeaf.nodes:
            if current_node.children == []:
                self.result += current_node.value


class ProductOfRedNodesVisitor(TreeVis):
    result = 1

    def getResult(self):
        return self.result

    def visitNode(self, treeNode : Tree):
        for i in range(len(treeNode.nodes)):
            if treeNode.getColor(i + 1) == 0:
                self.result *= treeNode.getValue(i + 1)

    def visitLeaf(self, treeLeaf : Tree):
        pass

class FancyVisitor(TreeVis):
    nonLeafNodesEvenDepth = 0
    greenLeafNodes = 0

    def getResult(self):
        return abs(self.nonLeafNodesEvenDepth - self.greenLeafNodes)

    def visitNode(self, treeNode : Tree):
        for i in range(len(treeNode.nodes)):
            if (treeNode.getDepth(i+1) % 2 == 0) and (treeNode.nodes[i].children != []):
                self.nonLeafNodesEvenDepth += treeNode.getValue(i+1)


    def visitLeaf(self, treeLeaf : Tree):
        for current_node in treeLeaf.nodes:
            if (current_node.children == []) and (current_node.color == 1):
                self.greenLeafNodes += current_node.value


# Test
if __name__ == '__main__':
    values = [4, 7, 2, 5, 12]
    colors = [0, 1, 0, 0, 1]
    child_list = [
        [1, 2],
        [1, 3],
        [3, 4],
        [3, 5]
    ]


    myTree = Tree()
    for i in range(len(values)):
        node = TreeNode()
        node.set_node(values[i], colors[i], i+1)
        for edge in child_list:
            if edge[0] == node.number:
                node.add_children(edge[1])

        print(node.value, node.color, node.number, node.children)
        myTree.add_node(node)

    sumInLeavesVisitor = SumInLeavesVisitor()
    sumInLeavesVisitor.visitLeaf(myTree)
    print(f"Result of SumInLeavesVisitor class: {sumInLeavesVisitor.getResult()}")

    productOfRedNodesVisitor = ProductOfRedNodesVisitor()
    productOfRedNodesVisitor.visitNode(myTree)
    print(f"Result of ProductOfRedNodesVisitor class: {productOfRedNodesVisitor.getResult()}")

    fancyVisitor = FancyVisitor()
    fancyVisitor.visitLeaf(myTree)
    fancyVisitor.visitNode(myTree)
    print(f"Result of FancyVisitor class: {fancyVisitor.getResult()}")