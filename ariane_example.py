def set_speed(speed:int) -> None:
    assert speed < 32768, "Speed must be in [0, 32767]"
    assert type(speed) == int, "Speed must be an integer"
    print("Speed set to", speed)

if __name__ == "__main__":
    set_speed(50)
    set_speed(32768)
    set_speed(1000000)