from pygame.math import Vector2


def get_inverse_matrix_2(v1: Vector2, v2: Vector2):
    det = get_determinant_2(v1, v2)
    if det == 0:
        return None

    a = v1.x
    b = v2.x
    c = v1.y
    d = v2.y

    v_1 = Vector2(d, -b)
    v_2 = Vector2(-c, a)
    return (1 / det) * v_1, (1 / det) * v_2


def get_determinant_2(a: Vector2, b: Vector2):
    return a.x * b.y - (b.x * a.y)
