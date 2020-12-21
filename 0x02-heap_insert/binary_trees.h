#ifndef _BINARY_TREES_H_
#define _BINARY_TREES_H_

#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/* Basic Binary Tree */

/**
 * struct binary_tree_s - Binary tree node
 *
 * @n: Integer stored in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left child node
 * @right: Pointer to the right child node
 */
struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

/* Max Binary Heap */
typedef struct binary_tree_s heap_t;

typedef struct binary_tree_s binary_tree_t;

/* Function to print a binary tree */
void binary_tree_print(const binary_tree_t *);

/* Function to create a binary tree node */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);

/* Function to insert a value in a Max Binary Heap*/
heap_t *heap_insert(heap_t **root, int value);

/* Function to measure the size of a binary tree */
size_t binary_tree_size(const binary_tree_t *tree);

/* Function to validate if parent node is greater than its child */
void heap_parent_vs_child(heap_t **son, heap_t **father);

#endif /* _BINARY_TREES_H_ */
