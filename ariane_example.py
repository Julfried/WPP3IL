def set_speed(speed:int) -> None:
    assert speed < 32768, "Speed must be in [0, 32767]"
    print("Speed set to", speed)

set_speed(50)
set_speed(32768)
set_speed(1000000)