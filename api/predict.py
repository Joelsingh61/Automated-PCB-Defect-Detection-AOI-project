from http.server import BaseHTTPRequestHandler
import json
import base64
import io
import os

from PIL import Image
from ultralytics import YOLO


MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "best.pt"
)

model = YOLO(MODEL_PATH)

CLASS_NAMES = [
    "Open",
    "Short",
    "Mousebite",
    "Spur",
    "Pin-hole",
    "Spurious Copper"
]


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        try:
            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)
            data = json.loads(body)

            image_data = data["image"]

            # Remove data URL prefix
            if "," in image_data:
                image_data = image_data.split(",", 1)[1]

            image_bytes = base64.b64decode(image_data)

            image = Image.open(
                io.BytesIO(image_bytes)
            ).convert("RGB")

            # Run YOLO
            results = model.predict(
                image,
                conf=0.25,
                verbose=False
            )

            result = results[0]

            detections = []

            if result.boxes is not None:

                for box in result.boxes:

                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])

                    x1, y1, x2, y2 = (
                        box.xyxy[0].tolist()
                    )

                    detections.append({
                        "defect": CLASS_NAMES[class_id],
                        "confidence": round(
                            confidence * 100, 2
                        ),
                        "box": [
                            round(x1),
                            round(y1),
                            round(x2),
                            round(y2)
                        ]
                    })

            status = "PASS" if len(detections) == 0 else "FAIL"

            response = {
                "status": status,
                "total_defects": len(detections),
                "detections": detections
            }

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.send_header(
                "Access-Control-Allow-Origin",
                "*"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

        except Exception as e:

            self.send_response(500)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps({
                    "error": str(e)
                }).encode()
            )
