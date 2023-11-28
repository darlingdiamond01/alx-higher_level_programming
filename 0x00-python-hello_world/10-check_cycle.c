#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked lists has a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *speed, *slow;

	if (!list || !list->next)
		return (0);
	speed = list->next->next;
	slow = list;

	while (slow && speed && speed->next)
	{
		if (slow == speed)
			return (1);
		slow = slow->next;
		speed = speed->next->next;
	}
	return (0);
}
