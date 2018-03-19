#include <stdio.h>
#include "matrix_mul.c"
#define SIZE 2

int main()
{
    void print_matrix(int a[2][2], int n);
    int a[2][2] = {{1, 3}, {7, 5}};
    int b[2][2] = {{6, 8}, {4, 2}};
    int c[2][2];
    print_matrix(a, SIZE);
}

void print_matrix(int a[2][2], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}
