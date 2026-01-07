import { CodeJar } from 'https://cdn.jsdelivr.net/npm/codejar@3.7.0/codejar.min.js';

const highlight = (editor) => {
    let code = editor.textContent;
    code = code
        .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
        .replace(/(\/\/.*)/g, '<span class="comment">$1</span>')
        .replace(/\b(function|return|print|if|else)\b/g, '<span class="keyword">$1</span>')
        .replace(/\b(Int|String|Void|Bool)\b/g, '<span class="type">$1</span>')
        .replace(/\b(\d+)\b/g, '<span class="number">$1</span>')
        .replace(/(\| \>|\-\>)/g, '<span class="operator">$1</span>');
    editor.innerHTML = code;
};

const editorElement = document.querySelector("#editor");
const jar = CodeJar(editorElement, highlight);

const API_URL = "/run";

document.getElementById("runBtn").addEventListener("click", async () => {
    const outputDiv = document.getElementById("output");
    const button = document.getElementById("runBtn");
    const statusDot = document.querySelector(".dot");

    button.disabled = true;
    button.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> PROCESSING';
    outputDiv.style.opacity = "0.5";
    
    try {
        const codeContent = jar.toString();

        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: codeContent })
        });

        const rawText = await response.text();
        let data;

        try {
            data = JSON.parse(rawText);
        } catch (e) {
            throw new Error("Server Crash (Not JSON): " + rawText.substring(0, 100) + "...");
        }

        outputDiv.style.opacity = "1";
        
        if (data.status === "error") {
            outputDiv.style.color = "#f38ba8"; 
            outputDiv.innerText = "❌ RUNTIME ERROR:\n" + data.output;
            statusDot.style.backgroundColor = "#f38ba8";
        } else {
            outputDiv.style.color = "#a6e3a1"; 
            outputDiv.innerText = data.output;
            statusDot.style.backgroundColor = "#a6e3a1";
        }

    } catch (error) {
        outputDiv.style.opacity = "1";
        outputDiv.style.color = "#f38ba8";
        outputDiv.innerText = "🔥 API ERROR:\n" + error.message;
        statusDot.style.backgroundColor = "#f38ba8";
    } finally {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-play"></i> EXECUTE';
    }
});