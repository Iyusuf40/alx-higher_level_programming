#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: head of linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *faster = NULL;

	if (list)
		faster = list->next;
	while (list && faster)
	{
		if (faster == list)
			return (1);
		if (faster->next)
			faster = faster->next->next;
		else
			faster = faster->next;
		list = list->next;
	}
	return (0);
}
