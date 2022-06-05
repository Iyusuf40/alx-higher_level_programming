#include <stdio.h>
#include <stdlib.h>
#include "object.h"
#include "listobject.h"
/**
 * print_python_list_info - prints info abt a list
 * @p: list to inspect
 */
void print_python_list_info(PyObject *p)
{
	int size, i = 0;

	printf("[*] Size of the Python List = %d\n", int(PyList_Size(p)));
	printf("[*] Allocated = %d\n", int(Py_SIZE(p)));

	size = int(PyList_Size(p))
	while (i < size)
	{
		printf("Element %d: %s\n", i, char *(Py_TYPE(p[i])));
		i++;
	}
}
