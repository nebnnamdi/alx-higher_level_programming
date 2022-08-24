#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node to linked list
 * @head: head of the singly linked list
 * @number: the input value
 * Return: the address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node, *tmp1;

  tmp1 = *head;
  if (!head)
    return (NULL);
  new_node = malloc(sizeof(listint_t));
  if (!new_node)
    return (NULL);
  new_node->n = number;
  if (!tmp1 || tmp1->n >= number)
    {
      new_node->next = tmp1;
      *head = new_node;
      return (new_node);
    }
  return (new_node);
}
