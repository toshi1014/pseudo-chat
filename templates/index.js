window.onload = function() {
    connection = new WebSocket(url);
    connection.onopen = WebsocketClient.onOpen;
    connection.onmessage = WebsocketClient.onMessage;
    document.querySelector("div.title").innerText = OPPONENT_NAME;
}

class WebsocketClient{
    static sendOrReceive = "";

    static onOpen(event) {
        console.log("[js] connected successfully");
    }
    static onMessage(event) {
        if (event.data.slice(0,4) === "[py]"){
            const message = event.data.slice(4)       // remove prefix [py]
            if (WebsocketClient.sendOrReceive === "send"){
                send(message);
            }else if(WebsocketClient.sendOrReceive === "receive"){
                receive(message);
            }
        }
    }

    static sendData(button) {
        WebsocketClient.sendOrReceive = button.value;
        connection.send("[js]" + WebsocketClient.sendOrReceive);
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
    const opponentName = OPPONENT_NAME;
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

    const timeElem = document.createElement("span");
    timeElem.className = "time";
    const currentDate = new Date();
    const time = currentDate.getHours() + ":" + currentDate.getMinutes();
    timeElem.innerHTML = "read<br>" + time;

    myMessage.appendChild(messageElem);
    myMessage.appendChild(timeElem);

    const myPost = document.createElement("div");
    myPost.className = "my_post";
    myPost.appendChild(myMessage);

    contents.appendChild(myPost);
    moveToBottom();
}

const moveToBottom = () => {
    contents.scrollTop = contents.scrollHeight;
}

;const ICON_FILENAME = 'icon.png'; const url = 'ws://localhost:5555'; const OPPONENT_NAME = '内城勇太'
