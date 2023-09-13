from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests
import gradio as gr 

# app title
title = "Welcome on your first handwritten recognition app!"

#you can load any model from huggingface
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-handwritten')

# prediction function for handwritting
def predict(ImageUrl,imgDraw,imgUplod):

  #fetch the image from url or handwritten canvas or the uplaoded image
  if ImageUrl :
    image = Image.open(requests.get(ImageUrl, stream=True).raw).convert("RGB")
  elif imgDraw : 
    image = imgDraw.convert("RGB")
  else :
    image = imgUplod.convert("RGB")

  #predict the image using microsoft/trocr-large-handwritten model loaded earlier
  pixel_values = processor(images=image, return_tensors="pt").pixel_values
  generated_ids = model.generate(pixel_values)
  generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
  return generated_text

#gradio interface
interface = gr.Interface(fn=predict, inputs=["text",gr.Sketchpad(type="pil",shape=(500, 500)),gr.Image(type="pil")], outputs="text", title=title )
interface.launch(server_name="0.0.0.0", server_port=8080)

