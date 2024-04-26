This is a Cython module with bindings to the [crcany](https://github.com/madler/crcany) library. It supports calculating CRC hashes of arbitary sizes as well as updating a crc hash over time. It takes advantage of crcany's ability to efficiently combine multiple CRCs to parallelize the CRC's calculation.

## Installation

`pip install anycrc`

## Usage

Use an existing model:

```python
>>> import anycrc
>>> crc32 = anycrc.Model('CRC32')
>>> crc32.calc(b'Hello World!')
472456355
```

Read the data in chunks:

```python
>>> crc32.update(b'Hello ')
3928882368
>>> crc32.update(b'World!')
472456355
```

The `update` method changes the internally stored CRC value, while `calc` doesn't. To go back to the initial value, use:

```python
>>> crc32.reset()
```

Specify the starting CRC value:

```python
>>> crc32.set(3928882368)
>>> crc32.calc('World!')
472456355
```

Specify your own CRC parameters:

```python
>>> # width, poly, init, refin, refout, xorout
>>> my_crc = anycrc.CRC(10, 0b0101010101, 0x3ff, True, False, 0)
>>> my_crc.calc('Hello World!')
35
```

The CRC will be computed in parallel when the input is large enough. If you want to disable parallelism, use:

```python
>>> anycrc.set_parallel(False)
```

The CRC's width cannot exceed your system's maximum integer width.

For a list of pre-built models, check [models.py](https://github.com/marzooqy/anycrc/blob/main/src/anycrc/models.py). To get a list of the models at any time, use the following command:

`python -m anycrc models`

## Benchmarks

Calculating the CRC32 for lorem ipsum 1 million times:

| Module | Time Elapsed (s) | Speed (GiB/s) | Relative |
|---|:-:|:-:|:-:|
| anycrc | 0.22 | 1.91 | 1.00 |
| zlib | 0.28 | 1.47 | 1.28 |
| fastcrc | 0.80 | 0.52 | 3.66 |
| crcmod-plus | 0.91 | 0.46 | 4.13 |


Calculating the CRC32 for the text of lorem ipsum repeated 1 million times in a single pass:

| Module | Time Elapsed (s) | Speed (GiB/s) | Relative |
|---|:-:|:-:|:-:|
| anycrc (parallel) | 0.02 | 23.16 | 1.00 |
| anycrc (serial) | 0.20 | 2.08 | 11.15 |
| zlib | 0.22 | 1.92 | 12.05 |
| fastcrc | 0.68 | 0.61 | 37.89 |
| crcmod-plus | 0.67 | 0.62 | 37.40 |

Tested on a 12th generation Intel i7 processor. Parallel performance will depend on your system.

#### Notes

\- Parallelism is disabled when the length of the input data is under 20k, as the serial method is faster in that case.

\- The macOS build only supports the serial version.
