# trocr-large
 
#create enviornment 
conda create --name trocr-large python=3.11 

#activaet the virtual enviornment
conda activate trocr-large

#install dependicies
conda install -c huggingface transformers
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c conda-forge gradio

#run code
python handwritten.py
