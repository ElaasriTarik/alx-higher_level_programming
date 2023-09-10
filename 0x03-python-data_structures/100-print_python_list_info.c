#include <Python.h>

void print_python_list_info(PyObject *p) {
    PyObject *item;
    Py_ssize_t size, allocated, i;
    PyListObject *list = (PyListObject *)p;
    size = PyList_Size(p);
    allocated = list->allocated;
    if (!PyList_Check(p))
    {
        PyErr_Format(PyExc_TypeError, "Object is not a list\n");
        return;
    }

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
