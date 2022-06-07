#include <stdio.h>
#include <stdio.h>
#include <sys/types.h>
#include <python3.4/python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>

/**
 * print_python_list_info - prints info abt a list
 * @p: list to inspect
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i = 0;

	printf("[*] Size of the Python List = %u\n", (unsigned int)PyList_Size(p));
	printf("[*] Allocated = %u\n", (unsigned int)Py_SIZE(p));

	size = PyList_Size(p)
	while (i < size)
	{
		printf("Element %u: %s\n", (unsigned int)i, (char *)Py_TYPE(p[i]));
		i++;
	}
}
