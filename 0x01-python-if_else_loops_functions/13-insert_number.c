#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node
 * @head: head of list
 * @number: int
 * Return: NULL on fail
 */
listint_t *insert_node(listint_t **head, const int number)
{
	listint_t *isCurrent, *tempo;
	listint_t *node = (listint_t *) malloc(sizeof(listint_t));

	if (head == NULL)
		return (NULL);
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL || number <= (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	isCurrent = *head;
	while (isCurrent->next != NULL)
	{
		if (isCurrent->n < number && isCurrent->next->n >= number)
		{
			tempo = isCurrent->next;
			isCurrent->next = node;
			node->next = tempo;
		}
		isCurrent = isCurrent->next;
	}

	if (number >= isCurrent->n)
	{
		tempo = isCurrent->next;
		isCurrent->next = node;
		node->next = tempo;
	}
	return (*head);
}