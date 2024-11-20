# About this project

Implemantion of <https://medium.com/@imabhi1216/basic-to-advanced-rag-using-llamaindex-estimating-optimal-chunk-size-2-4935bdb0ef4a>

# Getting started

## Prerequisites

The following are prerequisites to run this codebase:

- Python 3.10.6
- Poetry
- Ollama

 ## Installation
### 1. Install poetry

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Install the poetry environment

```sh
cd rag_eval_chunk
poetry install
```

### 3. Activate poetry environment

On linux/mac:
```sh
source $(poetry env info --path)/bin/activate
```

On windows:
```powershell
& ((poetry env info --path) + "\Scripts\activate.ps1")
```

### 4. Instal Ollama
1. Download from [Ollama.com](https://ollama.com/download) 
2. Pull `Llama3.1`

```sh
ollama
ollama pull "llama3.1"
```

### 5. Run script

```sh
python3 rag_eval_chunk/main.py
```
