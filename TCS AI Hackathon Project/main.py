import streamlit as st
import subprocess

# ✅ Full path to Ollama executable on Windows
OLLAMA_PATH = r"C:\Users\SHRINIVAS HUNNUR\AppData\Local\Programs\Ollama\ollama.exe"

# --- Function to summarize logs using Ollama ---
def summarize_logs(log_text, model):
    prompt = f"""
You are an AI assistant that summarizes maintenance logs.

Instructions:
- Summarize incidents from the logs below.
- Group them under: High Severity, Medium Severity, Low Severity.
- For each incident, include:
  • Issue: <short description, professional and concise>
  • Resolution: <what was done / status, professional wording>
- Keep the original formatting of bullet points.
- Use a professional, clear, and concise tone.
- Do not add recommendations or analysis beyond the logs.

Logs:
{log_text}
"""

    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", model],  # use full path
            input=prompt.encode("utf-8"),
            capture_output=True,
            check=True
        )
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Error calling Ollama: {e.stderr.decode('utf-8')}"

# --- Streamlit UI ---
st.set_page_config(page_title="Maintenance Log Summarizer", layout="wide")
st.title("🛠 AI Maintenance Log Summarizer")
st.write("Upload one or more log files and get concise AI-generated summaries.")

# File uploader
uploaded_files = st.file_uploader(
    "Choose log file(s)", type=["txt"], accept_multiple_files=True
)

# Model choices
model_options = {
    "deepseek-r1": "DeepSeek R1 (Reasoning & Summarization)",
}

model_display = st.selectbox("Select LLM Model", list(model_options.values()))
selected_model = [k for k, v in model_options.items() if v == model_display][0]

if uploaded_files:
    combined_logs = ""
    for file in uploaded_files:
        log_text = file.read().decode("utf-8")
        combined_logs += f"\n\n--- {file.name} ---\n{log_text}"

    # Show raw logs
    st.subheader("📜 Raw Logs")
    st.text_area("Log Preview", combined_logs, height=250)

    if st.button("🔍 Summarize Logs"):
        with st.spinner(f"Summarizing logs using {selected_model}..."):
            summary = summarize_logs(combined_logs, model=selected_model)
        st.success("✅ Summary Generated!")

        st.subheader("📝 Summary")
        st.text_area("Summary Output", summary, height=300)

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="log_summary.txt",
            mime="text/plain"
        )
