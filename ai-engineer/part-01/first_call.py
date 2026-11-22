# first_call.py: one call to Anthropic's Messages API, written from Anthropic's quickstart (checked 2026-11-22).
# Before you run it: set ANTHROPIC_API_KEY in your terminal, as the quickstart shows. Never put the key in this file.
# Install the package first, in a virtual environment: pip install anthropic
# Each call is billed to your account by its tokens. Not run for this video.
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "One tip for naming files?"}],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
