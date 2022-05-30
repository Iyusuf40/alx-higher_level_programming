#include "lists.h"
int check_cycle(listint_t *list)
{
	int count = 0, i;
	listint_t *arr[1024];

	while (list)
	{
		i = 0;
		while (i < count)
		{
			if (arr[i] == list)
				return (1);
			i++;
		}
		arr[count] = list;
		count++;
		list = list->next;
	}
	return (0);
}
