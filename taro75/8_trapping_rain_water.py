def trapping_rain_water(elevations: list[int]) -> int:
    n = len(elevations)
    if n < 2:
        return 0
    water = 0
    left = 1
    right = n - 2
    left_max = elevations[0]
    right_max = elevations[-1]
    while left <= right:
        if left_max < right_max:
            current_water = left_max - elevations[left]
            left_max = max(left_max, elevations[left])
            left += 1
        else:
            current_water = right_max - elevations[right]
            right_max = max(right_max, elevations[right])
            right -= 1
        if current_water > 0:
            water += current_water
    return water


def main() -> None:
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trapping_rain_water(array)
    print(result)
    assert result == 6


if __name__ == "__main__":
    main()
