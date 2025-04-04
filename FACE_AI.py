import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

class FaceDetectorRecognizer:
    def __init__(self):
        # Load pre-trained Haar Cascade for face detection
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        if not os.path.exists(cascade_path):
            raise FileNotFoundError("Haar Cascade file not found!")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        # Simple database to store known face embeddings
        self.known_faces = {}
        self.embedding_size = 128
        
    def detect_faces(self, image):
        """Detect faces in an image using Haar Cascade"""
        if image is None or image.size == 0:
            raise ValueError("Input image is empty or invalid")
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        return faces
    
    def generate_embedding(self, face_image):
        face_resized = cv2.resize(face_image, (64, 64))
        embedding = face_resized.flatten().astype(np.float32)
        embedding = embedding / np.linalg.norm(embedding)
        if len(embedding) < self.embedding_size:
            embedding = np.pad(embedding, (0, self.embedding_size - len(embedding)))
        else:
            embedding = embedding[:self.embedding_size]
        return embedding
    
    def register_face(self, image_path, identity):
        """Register a known face"""
        if not os.path.exists(image_path):
            print(f"Error: Image file not found at {image_path}")
            return False
            
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not load image from {image_path}")
            return False
            
        faces = self.detect_faces(image)
        if len(faces) == 0:
            print(f"Warning: No faces detected in {image_path}")
            return False
            
        x, y, w, h = faces[0]  # Take first face
        face = image[y:y+h, x:x+w]
        embedding = self.generate_embedding(face)
        self.known_faces[identity] = embedding
        print(f"Successfully registered {identity}")
        return True
    
    def recognize_face(self, image):
        """Recognize faces in an image"""
        faces = self.detect_faces(image)
        results = []
        
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            embedding = self.generate_embedding(face)
            
            best_match = "Unknown"
            best_score = -1
            
            for identity, known_embedding in self.known_faces.items():
                similarity = cosine_similarity(
                    embedding.reshape(1, -1),
                    known_embedding.reshape(1, -1)
                )[0][0]
                if similarity > best_score and similarity > 0.7:
                    best_score = similarity
                    best_match = identity
            
            results.append({
                'bbox': (x, y, w, h),
                'identity': best_match,
                'confidence': best_score if best_score > -1 else 0
            })
            
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image, f"{best_match} ({best_score:.2f})",
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        return image, results

def main():
    try:
        # Initialize detector/recognizer
        fr = FaceDetectorRecognizer()
        
        # Define image paths (adjust these to your actual file locations)
        base_path = r"c:\Users\hasin\OneDrive\Desktop\Encryptrix"
        person1_path = os.path.join(base_path, "person1.jpg")
        person2_path = os.path.join(base_path, "person2.jpg")
        
        # Register known faces
        fr.register_face(person1_path, "Alice")
        fr.register_face(person2_path, "Bob")
        
        # Process video
        cap = cv2.VideoCapture(0)  # Webcam
        if not cap.isOpened():
            raise ValueError("Could not open video capture device")
            
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
                
            processed_frame, results = fr.recognize_face(frame)
            cv2.imshow('Face Recognition', processed_frame)
            
            for result in results:
                print(f"Found {result['identity']} at {result['bbox']} "
                      f"with confidence {result['confidence']:.2f}")
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()