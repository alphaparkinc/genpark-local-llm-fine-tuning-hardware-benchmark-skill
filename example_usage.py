from client import LocalLlmFineTuningHardwareBenchmarkClient

def main():
    client = LocalLlmFineTuningHardwareBenchmarkClient()
    res = client.benchmark_fine_tuning("Llama-3.1-8B-Instruct", 10000)
    print(f"VRAM Required: {res['vram_usage_gb']} GB")
    print(f"Speed: {res['tokens_per_sec']} tokens/sec")

if __name__ == "__main__":
    main()
