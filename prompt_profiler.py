import argparse
import time
import torch
from models.base_model_loader import load_model
from analyzers.token_counter import analyze_tokens
from utils.printer import print_results


def main():
    parser = argparse.ArgumentParser(description="Prompt Profiler: Analyze prompt efficiency with HuggingFace models")
    parser.add_argument('--prompt', type=str, required=True, help='Prompt string to send to the model')
    parser.add_argument('--model', type=str, default='gpt2', help='HuggingFace model name (e.g., gpt2, distilgpt2)')
    args = parser.parse_args()

    tokenizer, model, device = load_model(args.model)

    # Tokenize and analyze prompt
    prompt_metrics = analyze_tokens(args.prompt)
    prompt_token_count = prompt_metrics['token_count']

    # Generate output and measure latency
    inputs = tokenizer(args.prompt, return_tensors='pt').to(device)
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
    output_token_count = output_metrics['token_count']

    # Prepare metrics
    metrics = {
        'Model': args.model,
        'Device': device,
        'Prompt': args.prompt,
        'Latency (s)': f"{latency:.3f}",
        'Output': output_text[len(args.prompt):].strip() if output_text.startswith(args.prompt) else output_text.strip(),
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
