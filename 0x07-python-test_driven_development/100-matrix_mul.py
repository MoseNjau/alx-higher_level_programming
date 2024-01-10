#!/usr/bin/python3
'''Module for multiplication of a matrix'''


def matrix_mul(m_a, m_b):
    '''Function to multiply a matrix'''
    rows_m_a = len(m_a)
    cols_m_a = len(m_a[0])
    rows_m_b = len(m_b)
    cols_m_b = len(m_b[0])

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    


    C = [[0 for row in range(cols_m_b)] for col in range(rows_m_a)]

    for i in range(rows_m_a):
        for j in range(cols_m_b):
            for k in range(cols_m_a):
                if i in m_a is not int and i in m_a is not float:
                    raise TypeError('m_a should contain only integers or floats')
                if j in m_b is not int and i in m_b is not float:
                    raise TypeError('m_b should contain only integers or floats')
                C[i][j] += m_a[i][k] * m_b[k][j]
    return C
