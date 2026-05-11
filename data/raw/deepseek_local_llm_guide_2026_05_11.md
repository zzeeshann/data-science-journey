# 🧠 Build Your Own AI News Analyzer: A Complete Beginner's Guide

## Part 1: The Big Picture

### The Problem We're Solving
120,000 news articles. Read each one, decide: World, Sports, Business, or Science? Weeks of work. An AI can do it in hours — for free, on your machine, no internet.

### The Three Building Blocks
| Block | What It Is | Analogy |
|-------|------------|---------|
| AI Model (Qwen) | Reads, understands, decides | The "brain" |
| Dataset (AG News) | 120K articles with labels | The "textbook" |
| Notebook (Jupyter) | Interactive code workspace | The "lab bench" |

### Why Local AI?
- Cloud AI: costs money, needs internet, limited, data goes to servers
- Your AI: free, works offline, no limits, private

## Part 2: Tools We Installed
| Tool | Purpose |
|------|---------|
| Python | Programming language |
| Jupyter | Interactive coding in browser |
| LM Studio | Runs AI models locally |
| Qwen 2.5 14B | The AI brain |
| HuggingFace Datasets | Free datasets library |
| Pandas | Data as Excel-like tables |
| Requests | Python talks to APIs |

## Part 3: The Connection (Restaurant Analogy)
- LM Studio = Kitchen (AI runs here)
- Jupyter = Waiter (sends questions)
- localhost:1234 = Order window (connection)
- Prompt + article = Order
- Qwen's answer = Dish served

## Part 4: Our Results
- 50 articles tested
- 46 correct
- 92% accuracy
- Qwen is very reliable for news classification

## Part 5: Full Setup Commands
```bash
mkdir ~/news-data-science
cd ~/news-data-science
python3 -m venv venv
source venv/bin/activate
pip install datasets jupyter requests pandas matplotlib seaborn
jupyter notebook