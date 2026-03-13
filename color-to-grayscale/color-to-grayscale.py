def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    n = len(image)
    m = len(image[0])
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            r, g, b = image[i][j]
            y = 0.299*r + 0.587*g + 0.114*b
            row.append(y)
        result.append(row)
        
    return result