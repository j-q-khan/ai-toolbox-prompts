# Pick a local model that fits your memory: checklist (facts checked 2026-11-16)

## 1. Know your memory
- [ ] Mac (Apple's M-series chip): Apple menu, About This Mac, Memory. Apple calls it one "single pool", so this one number is the one to match.
- [ ] Windows: Ctrl+Shift+Esc, Task Manager, Performance. Memory is your RAM. If you have a graphics card, GPU, Dedicated GPU memory is its VRAM.

## 2. Read a model's name
- [ ] The B is billions of parameters: Qwen3.5-9B has about 9 billion.
- [ ] A3B means 3 billion active parameters. Qwen3.6-35B-A3B still needs room for all 35 billion (Hugging Face's MoE explainer: "all experts are loaded in memory").
- [ ] Q4, Q8 (or 4bit, 8bit for Mac MLX copies) is the quantisation: the lower the number, the smaller the file. LM Studio's docs: "Choose a 4-bit option or higher if your machine is capable enough for running it."
- [ ] Sizes on Ollama's library page for Qwen3.5 9B: 19GB (bf16), 10GB (q8_0), 6.6GB (q4_K_M).

## 3. Check what it needs
- [ ] Go to lmstudio.ai/models, open the model, read "Minimum system memory".
- [ ] Qwen3.5-2B: 2 GB. Qwen3.5-4B: 4 GB. Qwen3.5-9B: 7 GB. Qwen3.6-27B: 16 GB. Qwen3.6-35B-A3B: 20 GB. (Checked 2026-11-16.)
- [ ] Rule of thumb from the video (not LM Studio's): keep about a quarter of your memory free for your system and apps. On 8 GB start with the 4B; on 16 GB the 9B leaves room.
- [ ] LM Studio's docs on 8GB Macs: "stick to smaller models and modest context sizes".

## 4. Download it in LM Studio
- [ ] Discover tab (Ctrl+2 on Windows, Cmd+2 on a Mac). Search for the model, for example Qwen3.5 9B.
- [ ] Pick a 4-bit download option (Q4_K_M, or 4bit on a Mac), click download.
- [ ] Chat tab: load it from the bar that says Select a model to load. A steady reply usually means it fits; a crawl usually means it's too big.
- [ ] Mid level: after downloading, `lms load --estimate-only <model_key>` (key from `lms ls`) prints LM Studio's memory estimate without loading the model.

## 5. Download safely from Hugging Face (mid level)
- [ ] Use the maker's own page: huggingface.co/Qwen for Qwen. The Qwen3.5 and Qwen3.6 sizes above are safetensors files under Apache-2.0.
- [ ] LM Studio's GGUF and MLX copies come from huggingface.co/lmstudio-community; each model page on lmstudio.ai/models names its copy under Sources.
- [ ] Prefer safetensors over pickle files. Hugging Face: "There are dangerous arbitrary code execution attacks that can be perpetrated when you load a pickle file."
- [ ] The verified badge is a domain setting, not a safety rating. When checked, deepseek-ai had it; Qwen and lmstudio-community didn't.
- [ ] Shortcut: LM Studio's Discover search box takes a full Hugging Face link.

Sources: lmstudio.ai/models/qwen/qwen3.5-9b (and the other model pages) ; lmstudio.ai/docs/app/basics/download-model ; lmstudio.ai/docs/app/system-requirements ; lmstudio.ai/docs/cli/local-models/load ; ollama.com/library/qwen3.5/tags ; huggingface.co/docs/hub/security-pickle ; huggingface.co/docs/safetensors ; huggingface.co/docs/hub/enterprise-advanced-security ; huggingface.co/blog/moe ; apple.com/newsroom/2020/11/apple-unleashes-m1
