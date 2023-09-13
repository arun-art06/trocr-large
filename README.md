# Transform Handwritten Text into Digital Text with Hugging Face's Microsoft/Trocr-Large-Handwritten Model
Learn how to effortlessly convert handwritten text into editable digital text using the power of the Microsoft/Trocr-Large-Handwritten model from Hugging Face. With the help of Gradio, a user-friendly interface, you can streamline the process of extracting information from handwritten notes.

# Run
The provided set of commands is a series of instructions for creating a Python environment, activating it, installing dependencies, and running a Python script. Let me break down each step for you:

## create enviornment 
$ conda create --name trocr-large python=3.11 
This command creates a new Conda virtual environment named "trocr-large" with Python version 3.11. Virtual environments are isolated environments where you can install specific packages and dependencies without affecting your system-wide Python installation.

## activaet the virtual enviornment
$ conda activate trocr-large
After creating the environment, you need to activate it. This ensures that any subsequent package installations or code executions occur within the isolated environment you just created.

## install dependicies
$ conda install -c huggingface transformers
$ conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
$ conda install -c conda-forge gradio
These commands install the necessary dependencies into the "trocr-large" environment:
The first command installs the "transformers" package from the Hugging Face repository.
The second command installs PyTorch, torchvision, and torchaudio, specifying CUDA version 11.7 for GPU support.
The third command installs Gradio, a Python library for creating user interfaces for machine learning models.

## run code
$ python handwritten.py
Finally, this command runs a Python script named "handwritten.py" within the "trocr-large" virtual environment. This script likely contains code that utilizes the installed packages and performs some functionality related to handwritten text processing, potentially using the Microsoft/Trocr-Large-Handwritten model.
