import subprocess

scripts = [
    "capture_video.py",
    "hand_detection.py",
    "gesture_detection.py",
    "gesture_recognition.py",
    "send_sos_with_location.py",
    "live_location_sos.py",
    "sos_with_alarm.py"
]

processes = []
for script in scripts:
    print(f"Starting {script}...")
    process = subprocess.Popen(["python", script])
    processes.append(process)

# Keep running until all scripts are finished
for process in processes:
    process.wait()
