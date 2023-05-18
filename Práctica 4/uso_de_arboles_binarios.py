# -*- coding: utf-8 -*-

# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e INgeneiría de Datos
#                 Facultade de Informática
#                 Universidade da Coruña
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from binary_tree import BinaryTree
from linked_queue import Queue


def preorder(tree):
    """ Preorder iterator for a BinaryTree."""
    if not tree.is_empty():
        yield tree.root_element()
        for x in preorder(tree.left_child()):
            yield x
        for x in preorder(tree.right_child()):
            yield x
            
def inorder(tree):
    """ Inorder iterator for a BinaryTree."""
    if not tree.is_empty():
        for x in inorder(tree.left_child()):
            yield x
        yield tree.root_element()
        for x in inorder(tree.right_child()):
            yield x
            
def postorder(tree):
    """ Postorder iterator for a BinaryTree."""
    if not tree.is_empty():
        for x in postorder(tree.left_child()):
            yield x
        for x in postorder(tree.right_child()):
            yield x
        yield tree.root_element()

def print_preorder_indent(tree, d):
    """Print preorder representation of subtree of T at depth d."""
    if not tree.is_empty():
        print(2*d*' ' + str(tree.root_element()))         # use depth for indentation
        print_preorder_indent(tree.left_child(), d+1)     # child depth is d+1
        print_preorder_indent(tree.right_child(), d+1)    # child depth is d+1

def print_inorder_indent(tree, d):
    """Print preorder representation of subtree of T at depth d."""
    if not tree.is_empty():
        print_inorder_indent(tree.left_child(), d+1)      # child depth is d+1
        print(2*d*' ' + str(tree.root_element()))         # use depth for indentation
        print_inorder_indent(tree.right_child(), d+1)     # child depth is d+1
      
def print_postorder_indent(tree, d):
    """Print preorder representation of subtree of T at depth d."""
    if not tree.is_empty():
        print_postorder_indent(tree.left_child(), d+1)    # child depth is d+1
        print_postorder_indent(tree.right_child(), d+1)   # child depth is d+1
        print(2*d*' ' + str(tree.root_element()))         # use depth for indentation
      
def breadthfirst(tree):
    """Breadthfirst iterator for a BinaryTree."""
    if not tree.is_empty():
        q = Queue()        # subtrees not yet yielded
        q.enqueue(tree)          # starting with the full tree
        while not q.is_empty():
            subtree = q.dequeue()        # retrieve subtree from the queue
            yield subtree.root_element() # report its root element
            # add non empty children to queue
            if not subtree.left_child().is_empty():
                q.enqueue(subtree.left_child())
            if not subtree.right_child().is_empty():
                q.enqueue(subtree.right_child())     
                
def number_of_nodes(tree):
    """Return the number of nodes of tree."""
    if tree.is_empty():
        return 0
    else:
        return 1\
               + number_of_nodes(tree.left_child())\
               + number_of_nodes(tree.right_child())
    
def number_of_internal_nodes(tree):
    """Return the number of internal nodes of tree."""
    if tree.is_empty():
        return 0
    elif tree.left_child().is_empty() and tree.right_child().is_empty():
        return 0
    else:
        return 1\
               + number_of_internal_nodes(tree.left_child())\
               + number_of_internal_nodes(tree.right_child())
    
def number_of_leaf_nodes(tree):
    """Return the number of internal nodes of tree."""
    if tree.is_empty():
        return 0
    elif tree.left_child().is_empty() and tree.right_child().is_empty():
        return 1
    else:
        return number_of_leaf_nodes(tree.left_child())\
               + number_of_leaf_nodes(tree.right_child())
               
def height(tree):
    """Return the height of tree."""
    if tree.is_empty():
        return 0
    else:
        return 1+ max(height(tree.left_child()),\
                      height(tree.right_child()))

def is_full(tree):
    """Return True if tree is a full tree. False otherwise."""
    return tree.is_empty() or is_full(tree.left_child())\
                              and is_full(tree.right_child())\
                              and height(tree.left_child()) == height(tree.right_child())


def is_perfect(tree):
    """Return True if all leaves are at the same level. False otherwise"""
    if tree.is_empty() or tree.left_child().is_empty()\
                          and tree.right_child().is_empty():
        return True
    elif tree.left_child().is_empty():
        return is_perfect(tree.right_child())
    elif tree.right_child().is_empty():
        return is_perfect(tree.left_child())
    else:
        return is_perfect(tree.left_child())\
               and is_perfect(tree.right_child())\
               and height(tree.left_child()) == height(tree.right_child())
               
def are_equal_trees(t1, t2):
    """True if t1 and t2 has the same shape and the same contents. False otherwise"""
    if t1.is_empty() and t2.is_empty():
        return True
    elif t1.is_empty() or t2.is_empty():
        return False
    else:
        return t1.root_element() == t2.root_element()\
               and are_equal_trees(t1.left_child(), t2.left_child())\
               and are_equal_trees(t1.right_child(), t2.right_child())
        
               
if __name__ == '__main__':
    # Ejemplos de utilización. NO es un test exhaustivo
    a = BinaryTree()
    b = BinaryTree(10)
    c = BinaryTree(10, BinaryTree(), BinaryTree())
    d = BinaryTree(10,\
                   BinaryTree(20,\
                              BinaryTree(40),\
                              BinaryTree(50)),\
                   BinaryTree(30,\
                              BinaryTree(60),\
                              BinaryTree(70)))
    e = BinaryTree(10,\
                   BinaryTree(20,\
                              BinaryTree(40),\
                              BinaryTree(50)))
    f = BinaryTree(10,\
                   BinaryTree(20),
                   BinaryTree(30,\
                              BinaryTree(60),\
                              BinaryTree(70)))
    
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    print("e = ", e)

    print("prueba preorden d", end=": ")
    for x in preorder(d):
        print(x, end=" ")
    print()
    
    print("prueba inorden d", end=": ")
    for x in inorder(d):
        print(x, end=" ")
    print()
        
    print("prueba posorden d", end=": ")
    for x in postorder(d):
        print(x, end=" ")
    print()
    
    print("prueba anchura d", end=": ")
    for x in breadthfirst(d):
        print(x, end=" ")
    print()    

    print("Preorden indentado d:")
    print_preorder_indent(d, 0); print()
    print("inorden indentado d:")
    print_inorder_indent(d, 0); print()
    print("Postorden indentado d:")
    print_postorder_indent(d, 0); print()
    
    print("número de nodos de a:", number_of_nodes(a))
    print("número de nodos de b:", number_of_nodes(b))
    print("número de nodos de d:", number_of_nodes(d))
    print("número de nodos de e:", number_of_nodes(e))

    
    print("número de nodos internos de a:", number_of_internal_nodes(a))
    print("número de nodos internos de b:", number_of_internal_nodes(b))
    print("número de nodos internos de d:", number_of_internal_nodes(d))
    print("número de nodos internos de e:", number_of_internal_nodes(e))

    print("número de nodos hoja de a:", number_of_leaf_nodes(a))
    print("número de nodos hoja de b:", number_of_leaf_nodes(b))
    print("número de nodos hoja de d:", number_of_leaf_nodes(d))
    print("número de nodos hoja de e:", number_of_leaf_nodes(e))

    print("altura de a:", height(a))
    print("altura de b:", height(b))
    print("altura de d:", height(d))
    print("altura de e:", height(e))

    print("a lleno?:", is_full(a))
    print("b lleno?:", is_full(b))
    print("d lleno?:", is_full(d))
    print("e lleno?:", is_full(e))
    
    print("a perfecto?:", is_perfect(a))
    print("b perfecto?:", is_perfect(b))
    print("d perfecto?:", is_perfect(d))
    print("e perfecto?:", is_perfect(e))
    print("f perfecto?:", is_perfect(f))

    print("iguales b y c", are_equal_trees(b, c))
    print("iguales d y d", are_equal_trees(d, d))
    print("iguales d y e", are_equal_trees(d, e))


    # Errores
    #f = BinaryTree(10, [], [])
