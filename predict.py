
from ultralytics import YOLO

# Specify the path to the latest run directory
latest_run_path = "C:/Users/dobri/Documents/for jobs/assignment for job/runs/detect/train17/weights/best.pt"

# Load the model from the latest run
model = YOLO(latest_run_path)

# Now you can use the model for predictions
results = model.val()
results.show()
