window.onload = function() {
    connection = new WebSocket(url);
    connection.onopen = WebsocketClient.onOpen;
    connection.onmessage = WebsocketClient.onMessage;
}

class WebsocketClient{
    static cnt = 1;
    static sendOrReceive = "";

    static onOpen(event) {
        console.log("[js] connected successfully");
    }
    static onMessage(event) {
        if (event.data.slice(0,4) === "[py]"){
            if (WebsocketClient.sendOrReceive === "send"){
                send(event.data);
            }else if(WebsocketClient.sendOrReceive === "receive"){
                receive(event.data);
            }
        }
    }

    static sendData(button) {
        WebsocketClient.sendOrReceive = button.value;
        connection.send("[js]" + this.cnt);
        this.cnt++;
    }
}

const contents = document.querySelector(".contents");

const receive = (message) => {
    // icon
    const figElem = document.createElement("figure");
    const image = document.createElement("img");
    image.src = ICON_FILENAME;
    figElem.appendChild(image);

    // name
    const opponentName = "Alice";
    const nameElem = document.createElement("div");
    nameElem.className = "opponent_name";
    const nameContent = document.createTextNode(opponentName);
    nameElem.appendChild(nameContent);

    // message
    const messageElem = document.createElement("div");
    messageElem.className = "message";
    const messageContent = document.createTextNode(message);
    messageElem.appendChild(messageContent);

    // unite name, message
    const nameMessageElem = document.createElement("div");
    nameMessageElem.className = "opponent_message";
    nameMessageElem.appendChild(nameElem);
    nameMessageElem.appendChild(messageElem);

    const opponentPost = document.createElement("div");
    opponentPost.className = "opponent_post";

    // unite all child elements
    opponentPost.appendChild(figElem);
    opponentPost.appendChild(nameMessageElem);
    contents.appendChild(opponentPost);

    moveToBottom();
}

const send = (message)=>{
    // message
    const messageElem = document.createElement("div");
    messageElem.className = "message";
    const messageContent = document.createTextNode(message);
    messageElem.appendChild(messageContent);

    const myMessage = document.createElement("div");
    myMessage.className = "my_message";
    myMessage.appendChild(messageElem);

    const myPost = document.createElement("div");
    myPost.className = "my_post";
    myPost.appendChild(myMessage);

    contents.appendChild(myPost);
    moveToBottom();
}

const moveToBottom = () => {
    contents.scrollTop = contents.scrollHeight;
}

;const ICON_FILENAME = 'icon.png'; const url = 'ws://localhost:5555';
