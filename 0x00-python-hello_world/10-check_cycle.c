#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - prototype function to checking singly linked list.
 * @list: * to linked lists.
 *
 * Return: 0 for no cycle, 1 for cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	while (slower && faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;
		if (faster == slower)
		{
			return (1);
		}
	}
	return (0);
}
