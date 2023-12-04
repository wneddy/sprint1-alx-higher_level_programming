#include <Python.h>

/**
 * print_python_list_info - function to output info about python list
 * @p: check object
 */
void print_python_list_info(PyObject *p)
{
	int  len, loc, x;
	PyObject *objectCheck;

	len = Py_SIZE(p);
	loc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", loc);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		objectCheck = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(objectCheck)->tp_name);
}
