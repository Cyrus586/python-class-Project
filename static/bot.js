const chatbox = document.getElementById("chatbox");
const userInput = document.getElementById("message");
const sendBtn = document.getElementById("send-btn")

sendBtn.addEventListener("click", () => {
    const userMessage = userInput.value.trim();
    if (userMessage !== "") {
        addMessage(userMessage, "user");
        userInput.value = "";

        // bot

        setTimeout(() => {
            addMessage("This is bot response", "bot")
        }, 1000);
    }
});

function addMessage(message, sender) {z
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("user", "message", "text-gray-700");
    if (sender === "user") {
        messageDiv.classList.add("text-right");

    }
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
}
