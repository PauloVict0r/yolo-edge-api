import torch

if torch.cuda.is_available():
    print("CUDA disponível: Sim")
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("CUDA disponível: Não (Executando via CPU)")