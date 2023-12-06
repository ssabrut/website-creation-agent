# ⚡️ Website Creation Agent

This project focuses on leveraging Language Model capabilities, particularly Large Language Models (LLMs), for the development of an innovative Website Creation Agent. By harnessing the power of advanced natural language processing, this agent aims to streamline and simplify the process of creating websites.

## 🚀 Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.11.5 ([python.org](https://www.python.org/downloads/))
- Poetry ([python-poetry.org](https://python-poetry.org/docs/))
- Pip ([pip.pypa.io](https://pip.pypa.io/en/stable/installation/))
- PyTorch Nvidia CUDA 12.1 ([Windows tutorial](https://www.youtube.com/watch?v=Kp6c5v9iL84))
- Vercel Account ([Vercel](https://vercel.com/))

## 🛠 Installation

Clone the project and go to project directory

```bash
git clone https://github.com/ssabrut/website-creation-agent.git
cd website-creation-agent
```

Create and start virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

Install PyTorch dependencies
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

After that, install all necessary dependencies from using Poetry
```bash
poetry install
```

Then run the server using poetry
```bash
poetry run python app.py
```

## 👩‍💻 Authors

- [@ssabrut](https://github.com/ssabrut)

