#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - function to check if a single list is palindrome
 * @head: head of the list
 * Return: 1 (Palindrome) 0 (Not palindrome)
 **/
int is_palindrome(listint_t **head)
{
  listint_t *aux_head = *head;
  int array[5000];
  int i, j;

  if (!(*head))
    return (1);
  for (i = 0; aux_head; i++)
    {
      array[i] = aux_head->n;
      aux_head = aux_head->next;
    }
  for (j = 0; j < i; i--, j++)
    {
      if (array[j] != array[i - 1])
	return (0);
    }
  return (1);
}
