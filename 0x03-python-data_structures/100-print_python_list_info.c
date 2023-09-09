#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print list info about Python
 * @p: Pyobjext pointer
 * Return: Success
 */

void print_python_list_info(PyObject *p)
{
  int x;
  long int s = PyList_Size(p);
  PyListObject *obj = (PyListObject *)p;

  printf("[*] Size of the Python List = %li\n", s);
  printf("[*] Allocated = %li\n", obj->allocated);
  for (x = 0; x < s; x++)
    {
      printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
    }
}
