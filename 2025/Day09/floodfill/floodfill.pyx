# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True

from libc.stdlib cimport malloc, free

def flood_fill(
    unsigned char[:] blocked,
    int width,
    int height
):
    cdef int max_cells = width * height
    cdef unsigned char[:] visited = bytearray(max_cells)

    cdef int* qx = <int*> malloc(max_cells * sizeof(int))
    cdef int* qy = <int*> malloc(max_cells * sizeof(int))
    if not qx or not qy:
        raise MemoryError()

    cdef int head = 0
    cdef int tail = 0

    # Start bei (0,0)
    qx[0] = 0
    qy[0] = 0
    visited[0] = 1
    tail = 1

    cdef int x, y, nx, ny, i, index
    cdef int dx[4]
    cdef int dy[4]

    dx[0], dy[0] = 0, 1
    dx[1], dy[1] = 0, -1
    dx[2], dy[2] = 1, 0
    dx[3], dy[3] = -1, 0

    while head < tail:
        x = qx[head]
        y = qy[head]
        head += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue

            index = ny * width + nx

            if visited[index]:
                continue

            if blocked[index]:
                continue

            visited[index] = 1
            qx[tail] = nx
            qy[tail] = ny
            tail += 1

    free(qx)
    free(qy)

    return visited


# This cdef function is not exposed to Python, allowing for faster, C-level calls.
cdef bint _is_inside(long px, long py, set perimeter_tiles, list segments):
    if (px, py) in perimeter_tiles:
        return True
    
    cdef int crossings = 0
    cdef long x, y_min, y_max_exclusive
    
    for x, y_min, y_max_exclusive in segments:
        if px < x:
            if y_min <= py < y_max_exclusive:
                crossings += 1
    return crossings % 2 == 1


# This def function is exposed to Python.
def check_rectangle_perimeter(
    long min_x, long min_y, long max_x, long max_y,
    set perimeter_tiles,
    list vertical_segments
):
    cdef long x, y

    # Top and bottom edges
    for x in range(min_x, max_x + 1):
        if not _is_inside(x, min_y, perimeter_tiles, vertical_segments):
            return False
        if not _is_inside(x, max_y, perimeter_tiles, vertical_segments):
            return False

    # Left and right edges
    for y in range(min_y + 1, max_y):
        if not _is_inside(min_x, y, perimeter_tiles, vertical_segments):
            return False
        if not _is_inside(max_x, y, perimeter_tiles, vertical_segments):
            return False
            
    return True
