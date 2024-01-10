#include <Python.h>

void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        Py_UNICODE *unicode_str = PyUnicode_AS_UNICODE(p);
        Py_ssize_t length = PyUnicode_GET_LENGTH(p);

        printf("  type: compact unicode object\n");
        printf("  length: %ld\n", length);
        printf("  value: %ls\n", unicode_str);
    }
    else if (PyBytes_Check(p))
    {
        char *byte_str = PyBytes_AS_STRING(p);
        Py_ssize_t length = PyBytes_GET_SIZE(p);

        printf("  type: compact ascii\n");
        printf("  length: %ld\n", length);
        printf("  value: %s\n", byte_str);
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}
