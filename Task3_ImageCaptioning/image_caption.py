from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("Loading Image Captioning Model...")

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load image
image = Image.open("sample.jpg").convert("RGB")

# Generate caption
inputs = processor(images=image, return_tensors="pt")
output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

print("\nGenerated Caption:")
print(caption)