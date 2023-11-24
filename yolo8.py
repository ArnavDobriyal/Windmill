from ultralytics import YOLO

model = YOLO("yolov8s.pt") #pretrained
results = model.train(data="config.yaml", epochs=40) 
