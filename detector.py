import psutil

print("=" * 50)
print("        KEYLOGGER DETECTOR")
print("=" * 50)

# Suspicious keywords
suspicious_words = [
    "keylogger",
    "logger",
    "hook",
    "spy",
    "monitor"
]

found = False

print("\nScanning Running Processes...\n")

for process in psutil.process_iter(['pid', 'name']):

    try:
        process_name = process.info['name'].lower()

        for word in suspicious_words:

            if word in process_name:
                found = True
                print(f"[ALERT] Suspicious Process Found")
                print(f"Process Name : {process.info['name']}")
                print(f"PID          : {process.info['pid']}")
                print("-" * 40)

    except:
        pass

if not found:
    print("No suspicious processes detected.")

print("\n" + "=" * 50)
print("Scan Completed")
print("=" * 50)