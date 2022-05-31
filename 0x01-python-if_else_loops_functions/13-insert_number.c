#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a sorted list
 * @head: head of list
 * @number: value to add
 * Return: address of node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *save, *prev;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;

	if (*head && (number <= (*head)->n))
	{
		node->next = *head;
		return (node);
	}

	save = *head;
	prev = *head;

	while(save)
	{
		if (number <= save->n)
		{
			node->next = save;
			if (save != prev)
				prev->next = node;
			return (node);
		}
		prev = save;
		save = save->next;
	}
	if ((*head != save) && !save)
		prev->next = node;
	else
		*head = node;

	node->next = NULL;

	return (node);
}
