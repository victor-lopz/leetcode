def trapping_rain_water(elevations: list[int]) -> int:
    water = 0
    left = 0
    right = len(elevations) - 1
    left_max = 0
    right_max = 0
    while left < right:
        if elevations[left] < elevations[right]:
            if left_max > elevations[left]:
                water += left_max - elevations[left]
            else:
                left_max = elevations[left]
            left += 1
        else:
            if right_max > elevations[right]:
                water += right_max - elevations[right]
            else:
                right_max = elevations[right]
            right -= 1
    return water


def main() -> None:
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trapping_rain_water(array)
    assert result == 6


if __name__ == "__main__":
    main()
