# Full code: LLM Training Explained: How LLMs Are Trained, and the Tiny One You Can Build From Scratch

The "which from-scratch path" table from this video, written from each repo's README and the course page, checked 2026-11-23. It was written from the docs, not run.

### which-from-scratch-path.md
```
# Which from-scratch path fits your hardware (facts checked 2026-11-23)
# From the video LLM Training Explained: How LLMs Are Trained, and the Tiny One You Can Build From Scratch
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as which-from-scratch-path.md.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Costs are as written on each page when checked, not quotes from a provider. Check the page again before you spend anything.

| Path | Hardware, in its own words | Cost, as written when checked | Licence | Link |
|---|---|---|---|---|
| 1. Laptop: Sebastian Raschka's LLMs-from-scratch | "designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware"; "automatically utilizes GPUs if they are available" | No cost stated for the code. The book it accompanies is sold separately. | Code: Apache 2.0 (LICENSE.txt). Books and their images are excluded. | https://github.com/rasbt/LLMs-from-scratch |
| 2. Rented machine: Andrej Karpathy's nanochat | runs/speedrun.sh "is designed to be run on an 8XH100 GPU node"; "this will take ~1.5 hours to run." | README: "for only $48 (~2 hours of 8XH100 GPU node)"; "an 8XH100 node is ~$24/hr"; on a spot instance "closer to ~$15". Tagline: "The best ChatGPT that $100 can buy." The lines don't agree. | MIT | https://github.com/karpathy/nanochat |
| 3. Depth: Stanford's Language Modeling from Scratch (Spring 2026) | "If you are following along at home, you can access GPU compute from a cloud provider to complete the assignments." | No price stated on the course page. Cloud graphics card time is paid for separately. | Not stated on the page | https://cs336.stanford.edu/ |

## Before you pick
- [ ] Python is installed. Setup help: https://github.com/rasbt/LLMs-from-scratch/tree/main/setup
- [ ] You want to start on your own laptop: path 1, chapter 2 (Working with Text Data) first.
- [ ] You're ready to rent a machine with eight H100 graphics cards and watch the clock: path 2. Check the provider's price on the day.
- [ ] Smaller rented cards (under 80GB each)? nanochat's README: "Look for --device-batch-size in the scripts and reduce it until things fit. E.g. from 32 (default) to 16, 8, 4, 2, or even 1."
- [ ] nanochat on an ordinary computer? Its README: runs/runcpu.sh is "a very simple example of running on CPU or Apple Silicon" and "You will not get strong results in this way."
- [ ] You want the full university course, and you're comfortable writing a lot of code: path 3. "The amount of code you will write will be at least an order of magnitude greater than for other classes."

## The one to skip
- nanoGPT's own README: "nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity." and "It is very likely you meant to use/find nanochat instead."

## Remember
- From scratch means the model starts from random numbers. Hugging Face's course: "Pretraining is the act of training a model from scratch: the weights are randomly initialized". Fine-tuning a ready-made model is not building one from scratch.

## Sources (all fetched 2026-11-23)
- github.com/rasbt/LLMs-from-scratch (README and LICENSE.txt)
- github.com/karpathy/nanochat (README)
- github.com/karpathy/nanoGPT (README)
- cs336.stanford.edu
- huggingface.co/learn/llm-course/chapter1/4
```
