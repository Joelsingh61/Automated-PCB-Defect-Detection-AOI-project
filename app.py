```python
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import pandas as pd

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="PCB Quality Inspection",
    page_icon="🔍",
    layout="wide"
)

# --------------------------------------------------
# Load YOLO model
# --------------------------------------------------

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# --------------------------------------------------
# Class names
# --------------------------------------------------

class_names = [
    "Open",
    "Short",
    "Mousebite",
    "Spur",
    "Pin-hole",
    "Spurious Copper"
]

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🔍 Automated PCB Defect Detection")
st.subheader("AI-Based PCB Quality Inspection using YOLO26")

st.write(
    "Upload a PCB image to automatically detect and classify "
    "manufacturing defects."
)

# --------------------------------------------------
# Upload image
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload PCB Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# Inspection
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.write("### Original PCB")
    st.image(image, use_container_width=True)

    # Run YOLO
    results = model.predict(
        image,
        conf=0.25,
        verbose=False
    )

    result = results[0]

    # Plot detections
    annotated_image = result.plot()

    # Convert BGR → RGB
    annotated_image = annotated_image[:, :, ::-1]

    # --------------------------------------------------
    # Display detected PCB
    # --------------------------------------------------

    st.write("### Inspection Result")

    st.image(
        annotated_image,
        caption="Detected PCB Defects",
        use_container_width=True
    )

    # --------------------------------------------------
    # Extract detections
    # --------------------------------------------------

    detections = []

    if result.boxes is not None:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            detections.append({
                "Defect": class_names[class_id],
                "Confidence": f"{confidence * 100:.2f}%"
            })

    # --------------------------------------------------
    # PASS / FAIL
    # --------------------------------------------------

    if len(detections) == 0:

        st.success("✅ PCB PASS")
        st.write("No defects detected.")

    else:

        st.error("❌ PCB FAIL")

        st.write(
            f"**Total defects detected: {len(detections)}**"
        )

        df = pd.DataFrame(detections)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # --------------------------------------------------
        # Defect summary
        # --------------------------------------------------

        st.write("### Defect Summary")

        counts = (
            df["Defect"]
            .value_counts()
            .reset_index()
        )

        counts.columns = ["Defect", "Count"]

        st.dataframe(
            counts,
            use_container_width=True,
            hide_index=True
        )
```

