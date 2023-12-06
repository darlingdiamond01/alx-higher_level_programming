#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes_data;

    if (!PyBytes_Check(p)) {
        printf("[!] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    bytes_data = ((PyBytesObject *)p)->ob_sval;

    printf("[.] bytes object info\n");
    printf("  Size: %ld\n", size);
    printf("  trying string: %s\n", bytes_data);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx%c", bytes_data[i], i < size - 1 ? ' ' : '\n');
    }
}

