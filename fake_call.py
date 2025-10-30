# fake_call.py -- harmless local simulation
import time
import os

caller = "Friend (Simulated)"
ring_file = "/data/data/com.termux/files/home/storage/shared/Download/ringtone.mp3"

print(f"=== Simulating incoming call from: {caller} ===")
# play ringtone with mpv (runs in background)
# adjust path above if needed
os.system(f"mpv --no-terminal '{ring_file}' &")
# duration of ring simulation (seconds)
ring_duration = 12
for i in range(ring_duration):
    print(f"Ringing... {i+1}s", end="\r")
    time.sleep(1)

# stop mpv
os.system("pkill mpv || true")
print("\nCall simulation ended.")
