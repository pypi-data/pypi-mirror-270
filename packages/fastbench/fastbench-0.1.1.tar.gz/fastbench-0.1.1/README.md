<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/itsmeadarsh2008/fastbench/main/truebench.svg" width="200" height="200">
  <br>
  TrueBench
  
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/fastbench">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/itsmeadarsh2008/fastbench">
  <br>
</h1>

TrueBench is a high-performance Python package for benchmarking code execution time, CPU usage, and memory usage. It's implemented in Python for simplicity and provides a simple API for measuring the performance of your Python code.

## ✨ Features

- 🕰️ Measure the execution time of a function or code block
- 🖥️ Track CPU usage during code execution
- 💾 Monitor memory usage during code execution
- ⚡ Lightweight and fast
- 🤏 Simple and easy-to-use API

## 📦 Installation

You can install TrueBench via pip:

```bash
pip install truebench
```

## 🔧 Usage

Here's an example of how to use TrueBench to benchmark Python code:

```python
from truebench import mt, mc, mm

# Define a sample function for testing
def sample_function(n):
    return sum(range(n))

# Test the mt function (measure execution time)
time_taken = mt(sample_function, n=1000000)
print("Time taken:", time_taken)

# Test the mc function (measure CPU usage)
cpu_usage = mc(sample_function, n=1000000)
print("CPU usage:", cpu_usage)

# Test the mm function (measure memory usage)
memory_usage = mm(sample_function, n=1000000)
print("Memory usage:", memory_usage)
```

## 🤝 Contributing

Contributions are welcome! Check out the [Contribution Guidelines](https://github.com/itsmeadarsh2008/fastbench/blob/main/CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/itsmeadarsh2008/fastbench?tab=MIT-1-ov-file) file for details.