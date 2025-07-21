import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model(model_name):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model = model.to(device)
    model.eval()
    return tokenizer, model, device
