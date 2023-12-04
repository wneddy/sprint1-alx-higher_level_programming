#include "lists.h"

/**
 * is_palindrome - palindrome checker for lists
 * @head: first address element
 *
 * Return: returns 1 -> palindrome, 0 -> otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	return (check_if_palindrome(head, *head));
}

/**
 * check_if_palindrome - recursive function check for palindrome
 * @head: lists address
 * @last: last node - act as head
 *
 * Return: returns 1 -> palindrome, 0 -> otherwise
 */
int check_if_palindrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
	{
		return (1);
	}
	if (check_if_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
