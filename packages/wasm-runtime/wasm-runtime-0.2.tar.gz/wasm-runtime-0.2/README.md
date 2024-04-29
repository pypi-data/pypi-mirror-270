# wasm-runtime

WebAssembly-powered, sandboxed implementation of Python runtime for safely `exec()`-cuting dynamic Python code.

This is an active version of [wasm_exec](https://github.com/Jflick58/wasm_exec) created by [Justin Flick](https://github.com/Jflick58).<br />See [Jflick58/wasm_exec/LICENSE](https://github.com/Jflick58/wasm_exec/blob/main/LICENSE) and [● wasm_runtime/LICENSE](https://github.com/AWeirdDev/wasm_runtime).

<div align="center">

`$ pip install wasm-runtime`

</div>

<br />

## Use

```python
from wasm_runtime import WasmRuntime

runtime = WasmRuntime()
result = runtime.exec("print('Hi, Mom!')")

print(result)
# Result(stdout='Hi, Mom!\n', stderr='', ...)
```

## <kbd>class</kbd> WasmRuntime

```python
__init__(
    self, 
    use_fuel: bool = False, 
    fuel: int = 400_000_000, 
    runtime_path: str = ""
)
```

Creates a new instance of WebAssembly runtime.

Original code by Justin Flick.

**Args:**
- use_fuel (`bool`): Whether to use fuel.
- fuel (`int`): Fuel.
- runtime_path (`str`): Runtime path. If not specified, the runtime will be downloaded automatically.

### <kbd>def</kbd> exec

```python
exec(self, code: str) -> Result
```

Execute Python code.

**Args:**
- code (`str`): Python code.

## <kbd>dataclass</kbd> Result

```python
stdout: str
stderr: str
memory_size: int
data_len: int
fuel_consumed: int
```
