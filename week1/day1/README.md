# Day 1: Variables, Data Types & String Operations

## 📚 Learning Objectives

- Understand Python variables and naming conventions
- Master the four fundamental data types
- Manipulate strings using built-in methods
- Format professional output with f-strings
- Handle user input effectively

## 📖 Concepts Covered

### 1. Variables
Variables store data values using descriptive names in `snake_case` format.
```python
server_name = "web-server-01"
port = 8080
cpu_usage = 67.5
is_active = True
```

### 2. Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text data | `"web-01"` |
| `int` | Whole numbers | `8080` |
| `float` | Decimal numbers | `67.5` |
| `bool` | True/False | `True` |

### 3. String Operations

Essential methods for DevOps work:
- `.upper()`, `.lower()` - Change case
- `.split()` - Split string into parts
- `.replace()` - Replace text
- `.strip()` - Remove whitespace
- `f""` - Format strings

### 4. Professional Output

Using f-strings for formatted output:
```python
print(f"Server {name} is running on port {port}")
```

## 💻 Exercises

All exercises are in the [`exercises/`](./exercises/) directory:

1. **`01_server_info.py`** - Display server information professionally
2. **`02_name_parser.py`** - Parse and extract server name components
3. **`03_log_generator.py`** - Generate formatted log messages
4. **`04_config_parser.py`** - Parse configuration strings
5. **`05_resource_calculator.py`** - Calculate resource percentages
6. **`06_server_card.py`** - Interactive server information card (Mini Project)

## ✅ Solutions

Complete solutions with explanations: [`solutions.py`](./solutions.py)

## 🎯 Key Takeaways

- Variables use `snake_case` naming
- f-strings are the modern way to format output
- String methods are essential for parsing configs and logs
- Professional output matters in production scripts
- Always validate and clean user input

## 🔗 Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 8 Style Guide](https://pep8.org/)
- [f-string formatting](https://realpython.com/python-f-strings/)

## 📝 Notes

Personal notes and observations: [`notes/concepts.md`](./notes/concepts.md)

---

**Time Spent:** ~2 hours  
**Difficulty:** ⭐☆☆☆☆  
**Status:** ✅ Completed
