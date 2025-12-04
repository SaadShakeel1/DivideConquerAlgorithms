import math
from typing import Callable, List, Optional, Tuple


Point = Tuple[float, float]


def point_distance(first: Point, second: Point) -> float:
    return math.hypot(first[0] - second[0], first[1] - second[1])


def closest_pair_recursive(sorted_x: List[Point],
                           sorted_y: List[Point],
                           log_step: Optional[Callable[[str], None]] = None,
                           depth: int = 0) -> Tuple[float, Point, Point]:
    n = len(sorted_x)
    indent = "  " * depth
    
    if log_step:
        log_step(f"{indent}Processing {n} points")
    
    if n <= 3:
        if log_step:
            log_step(f"{indent}Base case: checking all pairs")
        best_distance = float("inf")
        best_points = (sorted_x[0], sorted_x[0])
        for i in range(n):
            for j in range(i + 1, n):
                distance = point_distance(sorted_x[i], sorted_x[j])
                if distance < best_distance:
                    best_distance = distance
                    best_points = (sorted_x[i], sorted_x[j])
        if log_step:
            log_step(f"{indent}Found closest: distance = {best_distance:.4f}")
        return best_distance, best_points[0], best_points[1]

    middle = n // 2
    divider = sorted_x[middle][0]

    if log_step:
        log_step(f"{indent}Dividing at x = {divider:.2f} into left ({middle} points) and right ({n - middle} points)")

    left_x = sorted_x[:middle]
    right_x = sorted_x[middle:]

    left_set = set(left_x)
    left_y = [item for item in sorted_y if item in left_set]
    right_y = [item for item in sorted_y if item not in left_set]

    left_distance, left_a, left_b = closest_pair_recursive(left_x, left_y, log_step, depth + 1)
    right_distance, right_a, right_b = closest_pair_recursive(right_x, right_y, log_step, depth + 1)

    if log_step:
        log_step(f"{indent}Left side best: {left_distance:.4f}, Right side best: {right_distance:.4f}")

    if left_distance < right_distance:
        best_distance = left_distance
        best_points = (left_a, left_b)
    else:
        best_distance = right_distance
        best_points = (right_a, right_b)

    stripe = [point for point in sorted_y if abs(point[0] - divider) < best_distance]
    
    if log_step:
        log_step(f"{indent}Checking {len(stripe)} points in strip near divider")

    for i in range(len(stripe)):
        comparison_limit = min(i + 8, len(stripe))
        for j in range(i + 1, comparison_limit):
            distance = point_distance(stripe[i], stripe[j])
            if distance < best_distance:
                best_distance = distance
                best_points = (stripe[i], stripe[j])
                if log_step:
                    log_step(f"{indent}Found closer pair in strip: {best_distance:.4f}")

    if log_step:
        log_step(f"{indent}Final result: distance = {best_distance:.4f}")
    
    return best_distance, best_points[0], best_points[1]


def find_closest_pair(points: List[Point], log_step: Optional[Callable[[str], None]] = None) -> Tuple[float, Point, Point]:
    if len(points) < 2:
        raise ValueError("Need at least two points.")

    if log_step:
        log_step(f"Starting closest pair algorithm with {len(points)} points")
        log_step("Sorting points by x and y coordinates")

    sorted_by_x = sorted(points, key=lambda p: (p[0], p[1]))
    sorted_by_y = sorted(points, key=lambda p: (p[1], p[0]))
    
    return closest_pair_recursive(sorted_by_x, sorted_by_y, log_step, 0)


def karatsuba_multiply(x: int, y: int,
                       log_step: Optional[Callable[[str], None]] = None,
                       depth: int = 0) -> int:
    indent = "  " * depth
    
    if x < 10 or y < 10:
        if log_step:
            log_step(f"{indent}Base case: {x} * {y} = {x * y}")
        return x * y

    width = max(x.bit_length(), y.bit_length())
    half = (width + 1) // 2

    if log_step:
        log_step(f"{indent}Multiplying: {x} * {y}")
        log_step(f"{indent}Splitting into {half} bit halves")

    mask = (1 << half) - 1
    x_low = x & mask
    y_low = y & mask
    x_high = x >> half
    y_high = y >> half

    if log_step:
        log_step(f"{indent}x = {x_high} * 2^{half} + {x_low}")
        log_step(f"{indent}y = {y_high} * 2^{half} + {y_low}")

    if log_step:
        log_step(f"{indent}Computing z0 = x_low * y_low")
    z0 = karatsuba_multiply(x_low, y_low, log_step, depth + 1)
    
    if log_step:
        log_step(f"{indent}Computing z2 = x_high * y_high")
    z2 = karatsuba_multiply(x_high, y_high, log_step, depth + 1)
    
    if log_step:
        log_step(f"{indent}Computing z1 = (x_low + x_high) * (y_low + y_high) - z0 - z2")
    z1 = karatsuba_multiply(x_low + x_high, y_low + y_high, log_step, depth + 1) - z0 - z2

    result = (z2 << (2 * half)) + (z1 << half) + z0
    if log_step:
        log_step(f"{indent}Result: {z2} * 2^{2 * half} + {z1} * 2^{half} + {z0} = {result}")
    
    return result


def karatsuba_from_strings(first_number: str, second_number: str,
                           log_step: Optional[Callable[[str], None]] = None) -> int:
    left = int(first_number.strip())
    right = int(second_number.strip())
    
    if log_step:
        log_step(f"Starting Karatsuba multiplication")
        log_step(f"Number A: {len(first_number.strip())} digits")
        log_step(f"Number B: {len(second_number.strip())} digits")
    
    return karatsuba_multiply(left, right, log_step, 0)


