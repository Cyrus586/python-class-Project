const sidebar = document.querySelector("#sidebar");
const hide_sidebar = document.querySelector(".hide-sidebar");
const new_chat_button = document.querySelector(".new-chat");

hide_sidebar.addEventListener("click", function () {
    sidebar.classList.toggle("hidden");
});

const user_menu = document.querySelector(".user-menu ul");
const show_user_menu = document.querySelector(".user-menu button");

show_user_menu.addEventListener("click", function () {
    if (user_menu.classList.contains("show")) {
        user_menu.classList.toggle("show");
        setTimeout(function () {
            user_menu.classList.toggle("show-animate");
        }, 200);
    } else {
        user_menu.classList.toggle("show-animate");
        setTimeout(function () {
            user_menu.classList.toggle("show");
        }, 50);
    }
});

const models = document.querySelectorAll(".model-selector button");

for (const model of models) {
    model.addEventListener("click", function () {
        document.querySelector(".model-selector button.selected")?.classList.remove("selected");
        model.classList.add("selected");
    });
}

const message_box = document.querySelector("#message");

message_box.addEventListener("keyup", function () {
    message_box.style.height = "auto";
    let height = message_box.scrollHeight + 2;
    if (height > 200) {
        height = 200;
    }
    message_box.style.height = height + "px";
});

function show_view(view_selector) {
    document.querySelectorAll(".view").forEach(view => {
        view.style.display = "none";
    });

    document.querySelector(view_selector).style.display = "flex";
}

new_chat_button.addEventListener("click", function () {
    show_view(".new-chat-view");
});

document.querySelectorAll(".conversation-button").forEach(button => {
    button.addEventListener("click", function () {
        show_view(".conversation-view");
    })
});


/*
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

function addMessage(message, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("user", "message", "text-gray-700");
    if (sender === "user") {
        messageDiv.classList.add("text-right");

    }
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
}


*/

document.addEventListener("DOMContentLoaded", function () {
    var chatbox = document.getElementById("chatbox");
    var userInput = document.getElementById("message");
    var sendBtn = document.getElementById("send-btn");
    var chatContainer = document.querySelector(".chat-container");

    function appendMessage(message, sender) {
        var messageDiv = document.createElement("div");
        messageDiv.className = `u`,`message ${sender}`;
        messageDiv.innerHTML = `
            <div class="user message">
                <div class="identity">
                    <i class="user-icon">${sender}</i>
                </div>
                <div class="content">
                    <p>${message}</p>
                </div>
            </div>
        `;
        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    function generateBotResponse(userMessage) {
        var responses = [
            "Hello! How can i assist you?",
            "Iam here to help. what can i do for you",
            "Nice to meet you, How can i help you"
        ];
        var randomIndex = Math.floor(Math.random() * responses.length);
        return responses[randomIndex];
    }

    sendBtn.addEventListener("click", () => {
        const userMessage = userInput.value.trim();
        if (userMessage !== "") {
            appendMessage(userMessage, "u");
            
            userInput.value = "";
            setTimeout(function(){
                var botResponse = generateBotResponse(userMessage);
                appendMessage(botResponse, "b");

            }, 1000)
    
        }
    });

    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendBtn.click();
        }
    } )

})