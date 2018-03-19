1. How to save a 2D (m x n) matrix in C?

- allocate memory size of (m x n), save all matrix element inside. 
```c
int *a = malloc(m * n * sizeof(int))
```
`a[i][j]` (element in row i, col j) is stored at: `i * m + j`
- allocate m pointers to pointer 
