from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from msrest.exceptions import HttpOperationError
import requests
from io import BytesIO

# Function to authenticate Azure AI Vision client
def authenticate_client(endpoint, key):
    return ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        if not ai_endpoint or not ai_key:
            print("AI_SERVICE_ENDPOINT and AI_SERVICE_KEY must be set in the .env file.")
            return

        print(f"AI Endpoint: {ai_endpoint}")
        print(f"AI Key: {ai_key}")

        # Authenticate Azure AI Vision client
        cv_client = authenticate_client(ai_endpoint, ai_key)

        # Get image
        image_file = 'images/street.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        if not os.path.exists(image_file):
            print(f"Image file {image_file} does not exist.")
            return

        with open(image_file, "rb") as f:
            image_data = f.read()

        # Analyze image
        AnalyzeImage(image_file, image_data, cv_client)
        
        # Background removal
        BackgroundForeground(ai_endpoint, ai_key, image_file)

    except Exception as ex:
        print(ex)

def AnalyzeImage(image_filename, image_data, cv_client):
    print('\nAnalyzing image...')

    try:
        # Get result with specified features to be retrieved
        features = [VisualFeatureTypes.categories, VisualFeatureTypes.description,
                    VisualFeatureTypes.color, VisualFeatureTypes.objects]
        analysis = cv_client.analyze_image_in_stream(BytesIO(image_data), visual_features=features)

        # Print analysis results
        print("Categories:")
        for category in analysis.categories:
            print(f" - {category.name} (confidence: {category.score})")

        print("\nDescription:")
        for caption in analysis.description.captions:
            print(f" - {caption.text} (confidence: {caption.confidence})")

        print("\nColor:")
        color = analysis.color
        print(f" - Dominant Foreground Color: {color.dominant_color_foreground}")
        print(f" - Dominant Background Color: {color.dominant_color_background}")
        print(f" - Dominant Colors: {', '.join(color.dominant_colors)}")
        print(f" - Accent Color: #{color.accent_color}")

        print("\nObjects:")
        for obj in analysis.objects:
            print(f" - {obj.object_property} (confidence: {obj.confidence})")
            rect = obj.rectangle
            print(f"   Bounding box: X: {rect.x}, Y: {rect.y}, Width: {rect.w}, Height: {rect.h}")

        # Display the image with object outlines if any
        image = Image.open(image_filename)
        draw = ImageDraw.Draw(image)
        for obj in analysis.objects:
            rect = obj.rectangle
            draw.rectangle([(rect.x, rect.y), (rect.x + rect.w, rect.y + rect.h)], outline='red', width=5)
        plt.imshow(image)
        plt.axis("off")
        plt.show()

    except HttpOperationError as e:
        print(f"Status code: {e.response.status_code}")
        print(f"Reason: {e.response.reason}")
        print(f"Message: {e.response.text}")

def BackgroundForeground(endpoint, key, image_file):
    print('\nRemoving background...')

    # Define the API version and mode
    api_version = "2023-02-01-preview"
    mode = "backgroundRemoval"  # Can be "foregroundMatting" or "backgroundRemoval"
    
    url = f"{endpoint}/computervision/imageanalysis:segment?api-version={api_version}&mode={mode}"
    
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Content-Type': 'application/octet-stream'
    }
    
    with open(image_file, "rb") as f:
        image_data = f.read()

    response = requests.post(url, headers=headers, data=image_data)
    
    if response.status_code == 200:
        result = response.json()
        mask_url = result.get('mask', {}).get('url')
        if mask_url:
            mask_response = requests.get(mask_url)
            mask_image = Image.open(BytesIO(mask_response.content))
            mask_image_path = os.path.splitext(image_file)[0] + "_no_background.png"
            mask_image.save(mask_image_path)
            print(f"Background removed image saved at: {mask_image_path}")
            plt.imshow(mask_image)
            plt.axis("off")
            plt.show()
        else:
            print("No mask URL found in the response.")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    main()



# pip install azure-cognitiveservices-vision-computervision requests python-dotenv matplotlib Pillow
