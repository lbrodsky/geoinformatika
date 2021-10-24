#!/usr/bin/env python3

# Binary Search Tree
# zdroj: CVUT Jan Kibic

import random


class BinarySearchTree:
    """ Strom = uzel. Prázdný strom reprezentujeme jako None
    """
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right


def contains(tree,key):
    """ Je prvek ’key’ ve stromu? """
    if tree: # je strom neprázdný?
        if tree.key==key: # je to hledaný klíc?
            return True
        if tree.key>key:
            return contains(tree.left,key)
        else:
            return contains(tree.right,key)
    return False


def add(tree,key):
    """ Vloží ’key’ do stromu a vrátí nový koren """
    if tree is None:
        return BinarySearchTree(key)
    if key<tree.key:
        tree.left=add(tree.left,key)
    elif key>tree.key:
        tree.right=add(tree.right,key)
    return tree # hodnota již ve stromu je


def delete(tree, key):
    """ Smaže ’key’ za stromu ’tree’ a vrátí nový koren. """
    if tree is not None:
        if key < tree.key: # najdi uzel ’key’
            tree.left = delete(tree.left, key)
        elif key > tree.key:
            tree.right = delete(tree.right, key)
        else: # uzel nalezen, má syny?
            if tree.left is None:
                return tree.right # jen pravý syn nebo nic
            elif tree.right is None:
                return tree.left # jen levý syn nebo nic
            else: # nahradíme uzel maximem levého podstromu
                w = rightmost_node(tree.left)
                tree.key = w.key
                tree.left = delete(tree.left, w.key)
    return tree

def rightmost_node(tree):
    while tree.right:
        tree=tree.right
    return tree


def set_difference(x,y):
    """ Mnozinovy rozdil
        Find elements in array y but not in array x.
    """
    t=None
    for i in y:
        t=add(t,i)
    for j in x:
        t=delete(t,j)
    return to_array(t)

def print_tree(tree,level=0,prefix=""):
    if tree:
        print(" "*(4*level)+prefix+str(tree.key))
        if tree.left:
            print_tree(tree.left,level=level+1,prefix="L:")
        if tree.right:
            print_tree(tree.right,level=level+1,prefix="R:")

def from_array(a):
    """ Build a tree (containing only keys) from an array """
    def build(a):
        if len(a)==0:
            return None
        if len(a)==1:
            return BinarySearchTree(a[0])
        m=len(a)//2
        return BinarySearchTree(a[m],left=build(a[:m]),
                                right=build(a[m+1:]))
    a=sorted(a)
    return build(a)


def to_array(tree):
    a=[]
    def insert_inorder(t):
        nonlocal a
        if t:
            insert_inorder(t.left)
            a+=[t.key]
            insert_inorder(t.right)
    insert_inorder(tree)
    return a


def main():
    # inicializace
    t=from_array([21, 16, 19, 87])
    print_tree(t)

    # pridani zaznamu
    t=add(t,41)
    t=add(t,16)
    print_tree(t)

    # odstraneni prvku
    t=delete(t,16)
    print_tree(t)


if __name__ == "__main__":
    main()