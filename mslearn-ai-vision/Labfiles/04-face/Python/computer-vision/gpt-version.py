from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

def main():
    global cv_client

    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Get image
        image_file = 'images/people.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Authenticate Azure AI Vision client
        credentials = CognitiveServicesCredentials(ai_key)
        cv_client = ComputerVisionClient(ai_endpoint, credentials)
        
        # Analyze image
        AnalyzeImage(image_file, cv_client)

    except Exception as ex:
        print(ex)

def AnalyzeImage(image_file, cv_client):
    print('\nAnalyzing', image_file)

    # Specify features to be retrieved (Objects, including people)
    features = [VisualFeatureTypes.objects]

    # Open the image
    with open(image_file, 'rb') as image_stream:
        results = cv_client.analyze_image_in_stream(image_stream, visual_features=features)

    # Prepare image for drawing
    image = Image.open(image_file)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    # Get objects in the image
    if results.objects:
        print("\nObjects in image:")
        for detected_object in results.objects:
            # Draw object bounding box if confidence > 50%
            if detected_object.object_property == "person" and detected_object.confidence > 0.5:
                # Draw object bounding box
                r = detected_object.rectangle
                bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
                draw.rectangle(bounding_box, outline=color, width=3)
            
                # Print the confidence of the person detected
                print(" {} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))
            
        # Save annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'detected_people.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)
    else:
        print("No objects detected.")

if __name__ == "__main__":
    main()

# pip install azure-cognitiveservices-vision-computervision