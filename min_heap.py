from data_utils import switch_array_position
import numpy as np

class HeapElement:
    def __init__(self, key, content):
        self.key = key
        self.content = content
    
    def __repr__(self):
        return "(key: {}, content: {})".format(self.key, self.content)

def parent(i):
    return int((i - 1) / 2)

def left_child(i):
    return int(2 * i + 1)

def right_child(i):
    return int(2 * i + 2)

def get_element_position(pos_H, element: int):
    return pos_H.index(element)

def up_heap(heap_list, pos_H, elem_pos):
    f = elem_pos
    while f > 0 and heap_list[parent(f)].key > heap_list[f].key:
        p = parent(f)
        switch_array_position(heap_list, f, p)
        switch_array_position(pos_H, heap_list[f].content, heap_list[p].content)
        f = p

def insert(heap_list, pos_H, heap_size, element: HeapElement):
    # Insert new element on last position
    
    if heap_size >= len(heap_list):
        return heap_size
    
    heap_list[heap_size] = element
    pos_H[element.content] = heap_size
    heap_size += 1

    # Call up_heap sending new element position on list
    up_heap(heap_list, pos_H, heap_size - 1)

    # Return total length of the heap
    return heap_size

def down_heap(heap_list, pos_H, heap_size, elem_pos):
    p = elem_pos

    # Function that checks if element has left child with a lower key
    def need_repl_lc(elem):
        lc = left_child(elem)
        if lc < heap_size:
            return heap_list[lc].key < heap_list[elem].key 
        return False
    
    # Function that checks if element has right child with a lower key
    def need_repl_rc(elem):
        rc = left_child(elem)
        if  rc < heap_size:
            return heap_list[rc].key < heap_list[elem].key
        return False


    while need_repl_lc(p) or need_repl_rc(p):
        f = left_child(p)
        rc = left_child(p)
        if p < heap_size and heap_list[rc].key < heap_list[f].key:
            f = right_child(p)
        
        switch_array_position(heap_list, f, p)
        switch_array_position(
            pos_H,
            heap_list[f].content,
            heap_list[p].content
        )

def remove(heap_list, pos_H, heap_size):
    # Replace root with last element
    last_elem_pos = heap_size - 1
    removed_elem = heap_list[0]
    switch_array_position(heap_list, 0, last_elem_pos)
    switch_array_position(pos_H, heap_list[0].content, heap_list[last_elem_pos].content)
    
    # Remove last element
    heap_size -= 1
    
    # Rebalance
    down_heap(heap_list, pos_H, heap_size, 0)
    return removed_elem, heap_size

def update(heap_list, pos_H, elem: HeapElement):
    pos = get_element_position(pos_H, elem.content)
    heap_list[pos].key = elem.key
    up_heap(heap_list, pos_H, pos)
