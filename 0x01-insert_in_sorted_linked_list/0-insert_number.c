#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be inserted in the list
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if (head == NULL || *head == NULL)
		return (add_nodeint_end(head, number));

	current = *head;

	if (!number)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next != NULL && current->next->n < new->n)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
