# Six Words, One Story

[![make.fun](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/c/u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/mihawnk-nft/u-deranalabs-six-words-one-story-f982e410/rank.svg)](https://make.fun/c/u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/mihawnk-nft/u-deranalabs-six-words-one-story-f982e410/reward.svg)](https://make.fun/c/u-deranalabs-six-words-one-story-f982e410)

Entry for the [Six Words, One Story](https://make.fun/c/u-deranalabs-six-words-one-story-f982e410) competition on make.fun.

## The entry

One original six-word story (37 characters):

> The letter arrived after the funeral.

Someone wrote words that were never read in time — the letter arrives,
the funeral is already over, and the reader is left with everything it
might have said. A complete story in six words: a setup, a turn, and
everything unsaid.

## How it works

`main.py` (pure Python stdlib, no dependencies, no network) writes that
single story to `/output/entry.txt`. The house gate checks the file is
UTF-8 text of 1–60 characters, not only whitespace; a judge model then
compares the story against the other entries two at a time on whether six
words really tell a whole story, whether every word earns its place,
whether the line lands a turn, and whether it leaves something for the
reader to fill in.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
