# Full code: How to Install ComfyUI (Windows and Mac)

These commands come from ComfyUI's official docs (docs.comfy.org), checked 2026-11-04. They only look at your computer; none of them change anything.

### Windows with an NVIDIA card: your card, memory use and driver
```
nvidia-smi
nvidia-smi --query-gpu=driver_version --format=csv
```

### Mac with Apple Silicon, after a manual install: check that Metal works
```
python -c "import torch; print(torch.backends.mps.is_available())"
```

### extra_model_paths.yaml: copy extra_model_paths.yaml.example to this name in the ComfyUI folder (on Desktop, the install's own ComfyUI folder), remove the # from the a1111 block, set base_path, then restart ComfyUI
```
a1111:
    base_path: path/to/stable-diffusion-webui/
    checkpoints: models/Stable-diffusion
    configs: models/Stable-diffusion
    vae: models/VAE
    loras: |
         models/Lora
         models/LyCORIS
    upscale_models: |
                  models/ESRGAN
                  models/RealESRGAN
                  models/SwinIR
    embeddings: embeddings
    hypernetworks: models/hypernetworks
    controlnet: models/ControlNet
```
