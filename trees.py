from structures.stacks import Stack
import operator as op


class Tree:
    """Abstract base class representing a tree structure."""

    class Position:
        """An abstraction representing the location of an item's location."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    def root(self):
        """Return Position representing the trees root( or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children of Position p."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree."""
        if p is None:
            p = self.root()
        return self._height(p)

    def _height(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))


class BinaryTree:
    pass


class BinaryTreeTwo:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTreeTwo(new_node)
        else:
            t = BinaryTreeTwo(new_node)
            t.left = self.left
            self.left = t

    def get_right(self):
        return self.right

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTreeTwo(new_node)
        else:
            t = BinaryTreeTwo(new_node)
            t.right = self.right
            self.right = t

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def preorder(self):
        print(self.root)
        if self.get_left():
            self.get_left().preorder()
        if self.get_right():
            self.get_right().preorder()


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left = lc
        self.right = rc
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self


class BinarySearchTree:
    """
    put(): put key, value pair in tree
    get(): get value by key
    del: delete key, value pair while maintaining tree structure
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left)
            else:
                current_node.left = TreeNode(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right)
            else:
                current_node.right = TreeNode(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left
        return current

    @staticmethod
    def remove(current_node):
        # The node to be deleted has no children
        # Delete the node and remove reference to node in parent
        if current_node.is_leaf():
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None

        # The node to be deleted has both children
        # Find the successor and splice it out
        elif current_node.has_both_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload

        # The node to be deleted has only one child
        # Promote the child to take the place of its parent
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right_child():
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:
                    current_node.replace_node_data(current_node.left.key,
                                                   current_node.left.payload,
                                                   current_node.left.left,
                                                   current_node.left.right)
            else:   # current node is right child
                if current_node.is_left_child():
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                elif current_node.is_right_child():
                    current_node.right.parent = current_node.parent
                    current_node.parent.right = current_node.right
                else:
                    current_node.replace_node_data(current_node.right.key,
                                                   current_node.right.payload,
                                                   current_node.right.left,
                                                   current_node.right.right)


class ListTree:
    def __init__(self, r):
        self.tree = [r, [], []]

    def __str__(self):
        return str(self.tree)

    def insert_left(self, new_branch):
        t = self.tree.pop(1)
        if len(t) > 1:
            self.tree.insert(1, [new_branch, t, []])
        else:
            self.tree.insert(1, [new_branch, [], []])
        return self.tree

    def insert_right(self, new_branch):
        t = self.tree.pop(2)
        if len(t) > 1:
            self.tree.insert(2, [new_branch, [], t])
        else:
            self.tree.insert(2, [new_branch, [], []])
        return self.tree

    def get_root(self):
        return self.tree[0]

    def set_root(self, value):
        self.tree[0] = value

    def get_left_child(self):
        return self.tree[1]

    def get_right_child(self):
        return self.tree[2]


def animal():
    # start with a singleton
    root = BinaryTreeTwo("bird")

    # loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "):
            break

        # walk the tree
        my_tree = root
        while my_tree.get_left() is not None:
            prompt = my_tree.get_cargo() + "? "
            if yes(prompt):
                my_tree = my_tree.get_right()
            else:
                my_tree = my_tree.get_left()

        # make a guess
        guess = my_tree.get_cargo()
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # get new information
        prompt = "What is the animal's name? "
        my_animal = input(prompt)
        prompt = "What question would distinguish a %s from a %s? "
        question = input(prompt % (my_animal, guess))

        # add new information to the tree
        my_tree.set_cargo(question)
        prompt = "If the animal were %s the answer would be? "
        if yes(prompt % my_animal):
            my_tree.set_left(BinaryTreeTwo(guess))
            my_tree.set_right(BinaryTreeTwo(my_animal))
        else:
            my_tree.set_left(BinaryTreeTwo(my_animal))
            my_tree.set_right(BinaryTreeTwo(guess))


def yes(ques):
    ans = input(ques).lower()
    return ans == 'y'


def build_parse_tree(expr):
    fplist = expr.split()
    s = Stack()
    t = BinaryTreeTwo('')
    s.push(t)
    current_t = t
    for i in fplist:
        if i == '(':
            current_t.insert_left('')
            s.push(current_t)
            current_t = current_t.get_left()
        elif i not in "+-*/)":
            current_t.set_root(int(i))
            parent = s.pop()
            current_t = parent
        elif i in "+-*/":
            current_t.set_root(i)
            current_t.insert_right('')
            s.push(current_t)
            current_t = current_t.get_right()
        elif i == ")":
            current_t = s.pop()
        else:
            raise ValueError
    return t


def evaluate(tree):
    operators = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    if tree:
        res1 = evaluate(tree.get_left())
        res2 = evaluate(tree.get_right())
        if res1 and res2:
            return operators[tree.get_root()](res1, res2)
        else:
            return tree.get_root()


def preorder(tree):
    if tree:
        print(tree.get_root(), end=" ")
        preorder(tree.get_left())
        preorder(tree.get_right())


def post_order(tree):
    output_list = []
    if tree is not None:
        output_list.append(str(post_order(tree.get_left())))
        output_list.append(str(post_order(tree.get_right())))
        output_list.append(str(tree.get_root()))
    return output_list


def inorder(tree):
    output_list = []
    if tree is not None:
        output_list.append('(' + str(inorder(tree.get_left())))
        output_list.append(str(tree.get_root()))
        output_list.append(str(inorder(tree.get_right())) + ')')
    return ''.join(output_list)


def main():
    expression = "( ( 10 + 5 ) / 3 )"
    pt = build_parse_tree(expression)
    print(evaluate(pt))
    print(post_order(pt))

    # bst = BinarySearchTree()
    # bst[3] = "red"
    # bst[4] = "blue"
    # bst[5] = "yellow"
    # bst[6] = "at"
    #
    # print(bst[5])
    # print(bst[4])
    # del bst[4]
    # print(bst[4])

    # animal()


if __name__ == "__main__":
    main()
