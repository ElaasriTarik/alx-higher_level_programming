#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
int countList(listint_t **head);

int is_palindrome(listint_t **head)
{
  listint_t* curr = *head;
  int list_length = countList(head);
  int *arr = malloc(sizeof(int) * list_length);
  int x = 0;
  int first = 0;
  while (curr != NULL)
    {
      arr[x] = curr->n;
      x++;
      curr = curr->next;
    }
  x = x - 1;
  while (first != x && x >= 0)
    {
      if (arr[first] != arr[x])
	{
	  free(arr);
	  return (0);
	}

      x--;
      first++;
    }
  free(arr);
  return (1);
}


int countList(listint_t **head) {
    int count = 0;
    listint_t* curr = *head;

    while (curr != NULL) {
        count++;
        curr = curr->next;
    }
    return (count);
}
