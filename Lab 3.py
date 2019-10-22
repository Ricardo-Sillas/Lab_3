red = "red"
black = "black"
count = 0


class Node(object):
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.color = red

######################AVL Tree############################
class avl_tree:
    def __init__(self, root=None):
        self.root = root

    def avl_search(self, data, cur):
        if not cur:
            return 0
        if data == cur.data:
            return 1
        if data < cur.data:
            return self.avl_search(data, cur.left)
        if data > cur.data:
            return self.avl_search(data, cur.right)

    def print_tree(self, node):
        if node is None:
            return
        print(node.data)
        self.print_tree(node.left)
        self.print_tree(node.right)

    def avl_update_height(self, node):
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        node.height = max(left_height, right_height) + 1

    def avl_set_child(self, parent, which_child, child):
        if which_child != "left" and which_child != "right":
            return False
        if which_child == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        self.avl_update_height(parent)
        return True

    def avl_replace_child(self, parent, cur_child, new_child):
        if parent.left == cur_child:
            return self.avl_set_child(parent, "left", new_child)
        elif parent.right == cur_child:
            return self.avl_set_child(parent, "right", new_child)
        return False

    def avl_get_balance(self, node):
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        return left_height - right_height

    def avl_rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            self.avl_replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.avl_set_child(node.left, "right", node)
        self.avl_set_child(node, "left", left_right_child)

    def avl_rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            self.avl_replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.avl_set_child(node.right, "left", node)
        self.avl_set_child(node, "right", right_left_child)

    def avl_insertion(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            node.parent = None
            return
        cur = self.root
        while cur is not None:
            if node.data < cur.data:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        node = node.parent
        while node is not None:
            self.avl_rebalance(node)
            node = node.parent

    def avl_rebalance(self, node):
        self.avl_update_height(node)
        if self.avl_get_balance(node) == -2:
            if self.avl_get_balance(node.right) == 1:
                self.avl_rotate_right(node.right)
            return self.avl_rotate_left(node)
        elif self.avl_get_balance(node) == 2:
            if self.avl_get_balance(node.left) == -1:
                self.avl_rotate_left(node.left)
            return self.avl_rotate_right(node)
        return node

########################Red and Black Tree############################
class red_black_tree:
    def __init__(self, root=None, height=-1):
        self.root = root

    def rb_search(self, data, cur):
        if not cur:
            return 0
        if cur.data == data:
            return 1
        if data < cur.data:
            return self.rb_search(data, cur.left)
        if data > cur.data:
            return self.rb_search(data, cur.right)

    def print_tree(self,node):
        if node is None:
            return
        print(node.data, node.color)
        self.print_tree(node.left)
        self.print_tree(node.right)
        return

    def rb_set_child(self, parent, which_child, child):
        if which_child != "left" and which_child != "right":
            return False
        if which_child == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        return True

    def rb_replace_child(self, parent, cur_child, new_child):
        if parent.left == cur_child:
            return self.rb_set_child(parent, "left", new_child)
        elif parent.right == cur_child:
            return self.rb_set_child(parent, "right", new_child)
        return False

    def rb_rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            self.rb_replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.rb_set_child(node.right, "left", node)
        self.rb_set_child(node, "right", right_left_child)

    def rb_rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            self.rb_replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.rb_set_child(node.left, "right", node)
        self.rb_set_child(node, "left", left_right_child)

    def rb_insertion(self, data):
        node = Node(data)
        self._bst_insertion(node)
        node.color = red
        self.rb_balance(node)

    def _bst_insertion(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
            return
        cur = self.root
        while cur is not None:
            if node.data < cur.data:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        # node = node.parent

    def rb_get_grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def rb_get_uncle(self, node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left == node.parent:
            return grandparent.right
        else:
            return grandparent.left

    def rb_balance(self, node):
        if node.parent is None:
            node.color = black
            return
        if node.parent.color == black:
            return
        parent = node.parent
        grandparent = self.rb_get_grandparent(node)
        uncle = self.rb_get_uncle(node)
        if uncle is not None and uncle.color == red:
            parent.color = uncle.color = black
            grandparent.color = red
            self.rb_balance(grandparent)
            return
        if node == parent.right and parent == grandparent.left:
            self.rb_rotate_left(parent)
            node = parent
            parent = node.parent
        elif node == parent.left and parent == grandparent.right:
            self.rb_rotate_right(parent)
            node = parent
            parent = node.parent
        parent.color = black
        grandparent.color = red
        if node == parent.left:
            self.rb_rotate_right(grandparent)
        else:
            self.rb_rotate_left(grandparent)

# Getting the number of anagrams for a word in the avl tree
def count_anagrams_avl(word, english_words, prefix=""):
    global count
    if len(word) <= 1:
        if english_words.avl_search(prefix + word, english_words.root):
            count = count + 1
        else:
            for i in range(len(word)):
                cur = word[i: i + 1]
                before = word[0: i]  # letters before cur
                after = word[i + 1:]  # letters after cur
                if cur not in before:  # Checks if cur rearranged has been created
                    count_anagrams_avl(before + after, english_words, prefix + cur)
        return count


def most_anagrams_avl(english_words): # finds word with most anagrams in the file
    file = open("test.txt", "r")
    biggest = 0
    word = ""
    global count
    count = 0
    for singleLine in file:
        #Inserts each line in avl
        a = str(singleLine.replace("\n", ""))
        q = count_anagrams_avl(a, english_words)
        if q > biggest:
            word = a
            biggest = q
        count = 0
    print(word, biggest)
    return 0



def print_anagrams_avl(word, english_words, prefix = ""):
    if len(word) <= 1:
        if english_words.avl_search(prefix + word, english_words.root):
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]
            if cur not in before:
                print_anagrams_avl(before + after, english_words, prefix + cur)


def print_anagrams_rb(word, english_words, prefix = ""):
    if len(word) <= 1:
        if english_words.rb_search(prefix + word, english_words.root):
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]
            if cur not in before:
                print_anagrams_rb(before + after, english_words, prefix + cur)


def read_file_avl():
    file = open("test.txt", "r")
    avl = avl_tree()
    for single_line in file:
        avl.avl_insertion(single_line.replace("\n", ""))
    return avl


def print_anagrams_avl(word, english_words, prefix = ""):
    a = []
    num = 0
    if len(word) <= 1:
        if english_words.avl_search(prefix + word, english_words.root):
            print(prefix + word)
            a.append(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]
            if cur not in before:
                print_anagrams_avl(before + after, english_words, prefix + cur)
    return num + len(a)


def print_anagrams_rb(word, english_words, prefix = ""):
    if len(word) <= 1:
        if english_words.rb_search(prefix + word, english_words.root):
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]
            if cur not in before:
                print_anagrams_rb(before + after, english_words, prefix + cur)
    return count


def read_file_rb():
    file = open("test.txt", "r")
    rb = red_black_tree()
    for single_line in file:
        rb.rb_insertion(single_line.replace("\n", ""))
    return rb


def main():
    print("Hello. Would you like to use an AVL tree or a Red and Black tree.")
    print('For AVL tree, please insert "AVL", and for Red and Black, please insert "RB".')
    users_tree = input()
    if users_tree.upper() == "AVL":
        print("Please enter a word.")
        users_word = input()
        print("______")
        english_words = read_file_avl()
        # english_words.print_tree(english_words.root)
        # print("Anagrams:)
        print(count_anagrams_avl(users_word, english_words))
        print(print_anagrams_avl(users_word, english_words))
    elif users_tree.upper() == "RB":
        print("Please enter a word")
        users_word = input()
        print("______")
        english_words = read_file_rb()
        # english_words.print_tree(english_words.root)
        # print("Anagrams: ")
        print(print_anagrams_rb(users_word, english_words))
    else:
        print("That is not a valid input, please try again.")


main()
