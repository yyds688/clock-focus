import time
import sys

def pomodoro_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while True:
        remaining_time = end_time - time.time()
        if remaining_time <= 0:
            print("Time's up!")
            break

        minutes, seconds = divmod(int(remaining_time), 60)
        sys.stdout.write("\r{:02d}:{:02d} remaining".format(minutes, seconds))
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    focus_duration = 25  # 专注时长，以分钟为单位
    pomodoro_timer(focus_duration)
