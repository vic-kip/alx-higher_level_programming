#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *x, f, a, v;

	temp = *head;
	v = 0;
	while (temp != NULL)
	{
		v++;
		temp = temp->next;
	}
	x = (int*)malloc(sizeof(int) * v);
	if (x == NULL)
	{
		free(x);
	}
	if (*head == NULL)
	{
		return 1;
	}
	temp = *head;
	for (a = 0; a < v; a++)
	{
		x[a] = temp->n;
		temp = temp->next;
	}
	for (a = 0, f = v - 1; a < f; a++, f--)
	{
		if (x[a] != x[f])
		{
			free(x);
			return 0;
		}
	}
	free(x);
	return 1;
}
