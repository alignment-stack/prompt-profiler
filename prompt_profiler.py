
import os
import sys
import argparse
import time
import torch

# Ensure local imports work when run as a CLI or module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.base_model_loader import load_model
from analyzers.token_counter import analyze_tokens
from utils.printer import print_results


def main():
    parser = argparse.ArgumentParser(description="Prompt Profiler: Analyze prompt efficiency with HuggingFace models")
    parser.add_argument('--model', type=str, default=None, help='HuggingFace model name (e.g., gpt2, distilgpt2) or path to local model')
    parser.add_argument('--prompt', type=str, default=None, help="Text prompt to analyze")
    args = parser.parse_args()

    # Ask for model first, then prompt
    model_name = args.model or input("Enter model name (e.g., gpt2) or path to local model: ").strip()
    prompt = args.prompt or input("Enter prompt: ").strip()

    tokenizer, model, device = load_model(model_name)

    # Tokenize and analyze prompt
    prompt_metrics = analyze_tokens(prompt)

    # Generate output and measure latency
    inputs = tokenizer(prompt, return_tensors='pt').to(device)
    start_time = time.time()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2
        )
    latency = time.time() - start_time
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Tokenize and analyze output
    output_metrics = analyze_tokens(output_text)

    # Post-process output for readability
    cleaned_output = output_text[len(prompt):] if output_text.startswith(prompt) else output_text
    cleaned_output = cleaned_output.strip()

    # Prepare metrics
    metrics = {
        'Model': model_name,
        'Device': device,
        'Prompt': prompt,
        'Latency (s)': f"{latency:.3f}",
        'Output': cleaned_output,
    }
    # Add prompt metrics with prefix
    for k, v in prompt_metrics.items():
        if k != 'words':
            metrics[f'Prompt {k.replace("_", " ").title()}'] = v
    # Add output metrics with prefix
    for k, v in output_metrics.items():
        if k != 'words':
            metrics[f'Output {k.replace("_", " ").title()}'] = v
    print_results(metrics)


if __name__ == "__main__":
    main()
