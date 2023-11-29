#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node -function that inserts a number in an ordered linked list
 *
 * @head: linked list double *
 * @number: no. to insert
 *
 * Return: & of the new node, or NULL (0)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *crnt = *head;
	listint_t *latest = NULL;
	listint_t *temporary = NULL;

	if (!head)
	{
		return (NULL);
	}

	latest = malloc(sizeof(listint_t));
	if (!latest)
	{
		return (NULL);
	}
	latest->n = number;
	latest->next = NULL;

	if (!*head || (*head)->n > number)
	{
		latest->next = *head;
		return (*head = latest);
	}
	else
	{
		while (crnt && crnt->n < number)
		{
			temporary = crnt;
			crnt = crnt->next;
		}
		temporary->next = latest;
		latest->next = crnt;
	}

	return (latest);
}
