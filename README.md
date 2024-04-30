# My Project

This is a sample Gage project. Use it as a starting point for your own
evaluations.

Run [`eval.py`](eval.py) to see what it does. Don't worry it just
prints some sample data and writes `summary.json` to the directory.

```shell
python eval.py
```

Use Gage to generate a run.

Install Gage if it's not available.

```shell
pip install gage
```

List available operations.

```shell
gage ops
```

Operations are defined in the Gage file [`gage.toml`](gage.toml).

Run `eval`.

```shell
gage run eval --label "My first run"
```

Press `Enter`. This runs `eval.py` in a newly created *run directory*.

Show available runs.

```shell
gage runs
```

View the default board.

```shell
gage board
```

View a custom board.

```shell
gage board --config board.toml
```

Modify `eval.py` as needed to perform your own evaluations.

For more information, visit [Gage Chat](https://www.gage.chat).
