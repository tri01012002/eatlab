# **Streamlit App - Object Detection using YOLOv8**

## **Description**
This application uses the **YOLOv8** model to detect objects in uploaded videos or images. The project leverages Docker to package and deploy the Flask application with the YOLO model. You can upload a video or image and get object detection results.

## **System Requirements**
- Docker Desktop (Windows, macOS, Linux)
- Docker Compose
- Python 3.10 or higher
- Ensure that your machine has sufficient memory and CPU to run the application
- ## **Installation and Usage**
### **1. Clone the project repository**
Clone the project repository to your local machine:
```
git clone <https://github.com/tri01012002/eatlab>
cd streamlit_app
```
### **2. Build the Docker image**
Run the following command to build the Docker image from the **Dockerfile**:
```
docker-compose build
```
### **3. Run the application**
After the build process completes, you can start the application with the following command:
```
docker-compose up
```
This will start the containers, and you can access the application at `http://127.0.0.1:5000` in your browser.
To run the Docker container in the background, use:
```
docker-compose up -d
```
### **4. Upload a video or image for object detection**
- Navigate to **`http://127.0.0.1:5000`** in your browser.
- Upload a **video** or **image** and receive object detection results.
The application will return the detected objects along with the **bounding box coordinates** and **confidence** for each object.

### **5. Check logs**
If you encounter issues while running the application, you can check the **logs** of the application using the following command:
```
docker-compose logs
```

## **Directory Structure**
```
streamlit_app/
├── Dockerfile               # Dockerfile to create Docker image for the app
├── docker-compose.yml       # Docker Compose configuration file
├── app.py                   # Flask application code
├── requirements.txt         # Python libraries required
├── uploads/                 # Directory to store uploaded videos/images
├── output/                  # Directory to store processed videos/images
└── README.md                # Documentation file
```
### **Contact**
If you face any issues during the installation or usage of the application, feel free to contact us at: `tringuyen.01012002@gmail.com`.

