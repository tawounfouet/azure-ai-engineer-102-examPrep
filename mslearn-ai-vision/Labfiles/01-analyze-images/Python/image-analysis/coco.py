import json
import os
import cv2
from PIL import Image
from datetime import datetime

def create_coco_file(image_path, annotations, output_file):
    # Load image and get dimensions
    image = Image.open(image_path)
    width, height = image.size

    # Prepare COCO data structure
    coco_data = {
        "info": {
            "description": "COCO Dataset",
            "url": "http://cocodataset.org",
            "version": "1.0",
            "year": datetime.now().year,
            "contributor": "",
            "date_created": datetime.now().strftime("%Y/%m/%d")
        },
        "licenses": [
            {
                "id": 1,
                "name": "Unknown",
                "url": "http://example.com/license"
            }
        ],
        "images": [
            {
                "id": 1,
                "width": width,
                "height": height,
                "file_name": os.path.basename(image_path),
                "license": 1,
                "flickr_url": "",
                "coco_url": "",
                "date_captured": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        ],
        "annotations": [],
        "categories": []
    }

    category_ids = {}
    annotation_id = 1

    # Process annotations
    for annotation in annotations:
        category_name = annotation['category']
        if category_name not in category_ids:
            category_id = len(category_ids) + 1
            category_ids[category_name] = category_id
            coco_data["categories"].append({
                "id": category_id,
                "name": category_name,
                "supercategory": "none"
            })

        category_id = category_ids[category_name]
        bbox = annotation['bbox']
        
        # COCO bounding box format is [x, y, width, height]
        coco_annotation = {
            "id": annotation_id,
            "image_id": 1,
            "category_id": category_id,
            "bbox": bbox,
            "area": bbox[2] * bbox[3],  # width * height
            "segmentation": [],
            "iscrowd": 0
        }
        coco_data["annotations"].append(coco_annotation)
        annotation_id += 1

    # Save to JSON file
    with open(output_file, 'w') as f:
        json.dump(coco_data, f, indent=4)

# Example usage
image_path = 'path/to/your/image.jpg'
annotations = [
    {
        "category": "cat",
        "bbox": [100, 150, 50, 50]  # [x, y, width, height]
    },
    {
        "category": "dog",
        "bbox": [200, 250, 75, 75]
    }
]
output_file = 'path/to/output/coco_annotations.json'

create_coco_file(image_path, annotations, output_file)
