# Transform Handwritten Text into Digital Text with Hugging Face's Microsoft/Trocr-Large-Handwritten Model
Learn how to effortlessly convert handwritten text into editable digital text using the power of the Microsoft/Trocr-Large-Handwritten model from Hugging Face. With the help of Gradio, a user-friendly interface, you can streamline the process of extracting information from handwritten notes.

# create enviornment 
conda create --name trocr-large python=3.11 

# activaet the virtual enviornment
conda activate trocr-large

# install dependicies
conda install -c huggingface transformers
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c conda-forge gradio

# run code
python handwritten.py
