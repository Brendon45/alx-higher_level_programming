#include "lists.h"

/**
 * check_cycle - A function to check if there is cycle in list
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;
	
	if (!list || !list->next)
	return (0);
	fast = list;
	slow = list;
	
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
