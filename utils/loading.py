import time
import sys

def loading_animation(teks="Memuat"):
    for i in range(3):
        print(f"\r{teks}{'.' * (i + 1)}{' ' * (3 - i)}", end="")
        sys.stdout.flush()
        time.sleep(1)

# loading_animation()