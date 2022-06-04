#include "lists.h"
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of list
 *
 * Return: 0 or 1
 *
 */
int is_palindrome(listint_t **head)
{
	int arr[8134];
	int i = 0, j = 0, k = 0;

	if (!*head)
		return (1);

	while (*head)
	{
		arr[i] = (*head)->n;
		i++;
		*head = (*head)->next;
	}
	k = i;
	for (j = 0; j < k / 2; i--, j++)
	{
		if (arr[j] != arr[i - 1])
			return (0);
	}
	return (1);
}
