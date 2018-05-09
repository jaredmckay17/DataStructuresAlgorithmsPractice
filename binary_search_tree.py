class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def get(self):
        return self.value

    def set(self, val):
        self.value = val

    def get_children(self):
        children = []
        if self.left != None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)
        return children

    def print_in_order(self):
        if self.left != None:
            self.left.print_in_order()
        print(self.data)
        if self.right != None:
            self.right.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left != None:
            self.left.print_pre_order()
        if self.right != None:
            self.right.print_pre_order()

    def print_post_order(self):
        if self.left != None:
            self.left.print_post_order()
        if self.right != None:
            self.right.print_post_order()
        print(self.data)


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
