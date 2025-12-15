# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False

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
    qx[0], qy[0] = 0, 0
    visited[0] = 1
    tail = 1

    cdef int x, y, nx, ny, i, index
    cdef int dx[4]
    cdef int dy[4]
    dx[0] = 0; dx[1] = 0; dx[2] = 1; dx[3] = -1
    dy[0] = 1; dy[1] = -1; dy[2] = 0; dy[3] = 0

    while head < tail:
        x, y = qx[head], qy[head]
        head += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < width and 0 <= ny < height:
                index = ny * width + nx
                if not visited[index] and not blocked[index]:
                    visited[index] = 1
                    qx[tail], qy[tail] = nx, ny
                    tail += 1
    free(qx)
    free(qy)
    return visited

def check_rectangle_perimeter(
    long min_x, long min_y, long max_x, long max_y,
    set perimeter_tiles,
    list vertical_segments,
    list horizontal_segments
):
    cdef dict segments_by_x = {}
    cdef dict segments_by_y = {}
    cdef long x, y, val, y_min, y_max, x_min, x_max, crossings
    cdef bint is_on_perimeter
    cdef long x_seg, y_min_seg, y_max_seg
    cdef long y_seg, x_min_seg, x_max_seg

    # --- Horizontal Scanline Check (for top/bottom edges) ---
    for x, y_min, y_max in vertical_segments:
        if x not in segments_by_x: segments_by_x[x] = []
        segments_by_x[x].append((y_min, y_max))

    for y in [min_y, max_y]:
        crossings = 0
        for x_seg, y_min_seg, y_max_seg in vertical_segments:
            if min_x < x_seg:
                if y_min_seg <= y < y_max_seg:
                    crossings += 1
        
        for x in range(min_x, max_x + 1):
            is_on_perimeter = (x, y) in perimeter_tiles
            if not is_on_perimeter and crossings % 2 == 0:
                return False
            if x in segments_by_x:
                for y_min_seg, y_max_seg in segments_by_x[x]:
                    if y_min_seg <= y < y_max_seg:
                        crossings -= 1
    
    # --- Vertical Scanline Check (for left/right edges) ---
    for y, x_min, x_max in horizontal_segments:
        if y not in segments_by_y: segments_by_y[y] = []
        segments_by_y[y].append((x_min, x_max))

    for x in [min_x, max_x]:
        # Correct initial calculation for a downward scan from max_y
        crossings = 0
        for y_seg, x_min_seg, x_max_seg in horizontal_segments:
            if y_seg < max_y: # Segments below the start point
                if x_min_seg <= x < x_max_seg:
                    crossings += 1
        
        # Scan downwards from max_y to min_y
        for y in range(max_y, min_y - 1, -1):
            is_on_perimeter = (x, y) in perimeter_tiles
            if not is_on_perimeter and crossings % 2 == 0:
                return False
                
            # Update crossings for the next point (y-1)
            # If we are at a horizontal segment, it will no longer be "below" us
            if y in segments_by_y:
                for x_min_seg, x_max_seg in segments_by_y[y]:
                    if x_min_seg <= x < x_max_seg:
                        crossings -= 1
            
    return True
