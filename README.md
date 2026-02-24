# Alaska Archives LLM Toolchain

This repository contains the initial toolchain validation for the Alaska Archives research project.
The goal is to support processing historical Russian scans (including handwriting) using an OCR + open-source transformer stack.

## Environment Check

The toolchain script verifies that the following dependencies are installed and working:

- Python version
- NumPy
- Pandas
- OCR stack: Pillow + PyTesseract
- Meta / open-source LLM stack: PyTorch + Transformers

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
