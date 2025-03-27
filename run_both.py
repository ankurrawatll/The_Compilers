import subprocess
import time

# Define the scripts to run
eye_script = "direction.py" 
prediction_script = "prediction.py"

# Start both processes
eye_process = subprocess.Popen(["python", eye_script]) 
prediction_process = subprocess.Popen(["python", prediction_script])  

print("✅ Both scripts started successfully!")  

try:
    while True:  
        time.sleep(1)  # Keep the main script running  
except KeyboardInterrupt:
    print("\n🔴 Stopping both scripts...")

    # Terminate both processes safely
    eye_process.terminate()   