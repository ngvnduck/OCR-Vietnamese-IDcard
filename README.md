# OCR Vietnamese Identity Card
(This is a small AI project for AI and application class HUST 2023.1 semester)<br><br>
Using OCR model and fine-tuning to extract information from Vietnamese Identity Card
- Text detection: PaddleOCR
- Text recognition: VietOCR
# Result
- Text detection: https://colab.research.google.com/drive/1dihyu3YT-Drnpnf4lcoY1qau8rVKvjUs?usp=sharing
- Text recognition: https://colab.research.google.com/drive/1a3oqrN1UtK1iC7VnpnbEIl5mYdEoJJ9f?usp=sharing
- End-to-end application: https://colab.research.google.com/drive/1MfcFes8dNvAqXZEI-t1btyTShPpQUXki?usp=sharing
- Training, fine-tune VietOCR: https://colab.research.google.com/drive/1G6vP14Uc8PJ6PsOwOPrquAVg930fuax5?usp=sharing
# Data
- 300 identity cards
- Finetune: 6000 text images
- Result overall:<br>
    CER: 0.0061<br>
    WER: 0.0385<br>
    Acc per char: 0.9841914772987366<br>
    Acc full seq: 0.8918918967247009<br>
