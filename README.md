
# 🛠 AI Maintenance Log Summarizer

This is a **Streamlit web app** that uses Ollama AI models to summarize maintenance logs. It allows you to upload log files, generate concise summaries, and download the results.

---

## Features

- Upload one or more `.txt` log files.
- AI-powered summarization using Ollama LLMs.
- Groups incidents by severity: High, Medium, Low.
- Shows raw logs and AI-generated summary in the web app.
- Download the summarized logs as a `.txt` file.
- Supports multiple models: DeepSeek R1, Gemma, LLaMA 2, and GTE-Large.

---

## Requirements

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [Ollama CLI](https://ollama.com/docs)
- Windows OS (tested), but works on macOS/Linux with adjustments.

---

## Installation

1. **Clone the repository** (or copy the code to a folder):

```bash
git clone <repo-url>
cd <project-folder>
```

2. **Install Python dependencies**:

```bash
pip install streamlit
```

3. **Install Ollama**  
   Download and install from: [https://ollama.com/download](https://ollama.com/download)

4. **Pull a model**:

```powershell
& "C:\Users\<YourUser>\AppData\Local\Programs\Ollama\ollama.exe" pull deepseek-r1
```

> Replace `<YourUser>` with your Windows username. You can also pull `gemma`, `llama2`, or `gte-large`.

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run main.py
```

2. Open the app in your browser (usually opens automatically).  
3. Upload `.txt` log files.  
4. Select an AI model.  
5. Click **Summarize Logs**.  
6. View the summary and download it if needed.

---

## Example Dummy Logs

```
2025-09-01 08:12:01 | Database | High | Database connection timeout | Restarted DB service and verified connectivity
2025-09-01 09:05:15 | Server | Medium | CPU usage spiked above 90% | Optimized running processes, load stabilized
...
```

---

## Generated Output 
<img width="1914" height="794" alt="Screenshot 2025-09-03 155058" src="https://github.com/user-attachments/assets/81a619e5-6e26-43e5-adf0-ca1c2eca704a" />

## Notes

- Make sure Ollama CLI is installed and accessible via full path in the code.  
- `gte-large` is not ideal for summarization; prefer `deepseek-r1` or `gemma`.  
- Supports multiple uploaded files; all logs are combined for summarization.  

---

## License

MIT License
