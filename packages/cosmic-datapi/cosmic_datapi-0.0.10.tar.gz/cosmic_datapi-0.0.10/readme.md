# Cosmic DatAPI

Basically a library to create data mods in Cosmic Reach really fast.

**Example:**
```python
from cosmic_datapi import Mod

MOD = Mod("example_mod")

# This call is wrapped with parenthesis so that we can utilize newlines
(MOD.block("example_block")
    .with_state("default")
        .with_model("model_cheese")
        .with_light(14, 13, 12)
        .build()
    .build())

MOD.build()
```
