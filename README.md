# **🚀 Query Optimizer**

A custom-built Transformer decoder model designed to convert natural language prompts into structured SQL queries.

This project explores how sequence models (inspired by GPT-style architectures) can be adapted for structured reasoning tasks, specifically query generation and optimization.

## 🧠 Project Overview

This repository implements a decoder-only Transformer architecture trained on synthetic SQL data. The goal is simple but powerful:

Convert human-readable prompts into valid SQL queries with reasoning context.

Unlike generic language models, this system is designed to:

Learn structured output patterns
Handle prompt → query mapping
Incorporate rule-based explanations during training

## ⚙️ Model Architecture

The model is a custom implementation of a GPT-style decoder:

🔹 Core Components

    Token Embedding + Positional Encoding
    Stacked Decoder Layers (6 layers)
    Masked Multi-Head Self Attention
    Feed Forward Networks
    Layer Normalization
    
🔹 Key Hyperparameters

    d_model = 256
    num_heads = 4
    num_layers = 6
    dropout = 0.1
    vocab_size = 375

## 🏗️ Architecture Flow

    Input Text → Tokenization → Embedding + Positional Encoding
            ↓
       Decoder Stack (Masked Attention)
            ↓
         Linear Projection
            ↓
         Output Tokens (SQL Query)
         
## 📂 Dataset

The model is trained on a synthetic SQL dataset containing:

Natural language prompts
Corresponding SQL queries
Optional rules and explanations
Example:
Prompt: Get all users with age > 25
Query: SELECT * FROM users WHERE age > 25;


### 🔤 Tokenization

    Uses SentencePiece
    Custom-trained tokenizer
    Vocabulary size: 375
    spm.SentencePieceTrainer.train(
        input="clean_data.jsonl",
        model_prefix="Query_Tokenizer",
        vocab_size=375
    )
    
### 🧪 Training Setup

    Loss Function
    Cross Entropy Loss (with padding ignored)
    Optimizer
    AdamW
    Scheduler
    Linear Warmup
    Training Details
    lr = 1e-4
    epochs = 100
    batch_size = 64
    max_seq_len = 140
    
### 📊 Data Pipeline

    JSONL dataset parsing
    Tokenization (input + output)
    Padding & truncation
    Train / Validation / Test split
    PyTorch Dataset + DataLoader
    
### 🏋️ Training Loop

Includes:

    Batch-wise training
    Validation loop
    Loss tracking
    TensorBoard logging
    runs/sql_training

### 📈 Monitoring

TensorBoard is used for:

Training loss
Validation loss
Learning dynamics

    Run:
    
    tensorboard --logdir=runs

### 🧩 Key Features

✔️ Custom Transformer from scratch (no HuggingFace shortcuts)
✔️ End-to-end pipeline (data → tokenizer → model → training)
✔️ Structured output learning (SQL generation)
✔️ Clean modular design (decoder, dataset, training loop)

### ⚠️ Limitations

Let’s be real for a second:

Synthetic dataset → limited real-world generalization
No beam search / decoding strategy yet
No execution-based validation of SQL queries
Model focuses more on pattern learning than deep reasoning

### 🔮 Future Improvements

This is where things get interesting:

🔹 Add execution-aware training (reward valid SQL)
🔹 Integrate RL-based fine-tuning
🔹 Add beam search / top-k decoding
🔹 Move toward schema-aware query generation
🔹 Hybrid system: Transformer + RL planner (your bigger vision 👀)

### 🛠️ Tech Stack

PyTorch
SentencePiece
TensorBoard
Python


### 🚀 How to Run

#### Install dependencies

    pip install torch sentencepiece tensorboard

#### Train tokenizer

    python tokenizer.py

#### Train model

    python train.py

#### Monitor training

    tensorboard --logdir=runs

### 💡 Inspiration

This project sits at the intersection of:

Language Models (GPT-style)
Structured Prediction
Program Synthesis
Query Optimization

### 🧠 Author’s Note

This isn’t just about generating SQL.

It’s about pushing Transformers beyond text…
toward structured reasoning systems.
