const API_URL = "/run";

document.getElementById("runBtn").addEventListener("click", async () => {
    const codeInput = document.getElementById("code");
    const outputDiv = document.getElementById("output");
    const button = document.getElementById("runBtn");
    const statusDot = document.querySelector(".dot");

    // UI Loading
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> PROCESSING';
    outputDiv.style.opacity = "0.5";
    
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: codeInput.value })
        });

        // 1. Get raw text first (don't parse JSON yet)
        const rawText = await response.text();
        let data;

        // 2. Try to parse it
        try {
            data = JSON.parse(rawText);
        } catch (e) {
            // 3. If parse fails, it's a Server Crash (HTML). Show the raw text.
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