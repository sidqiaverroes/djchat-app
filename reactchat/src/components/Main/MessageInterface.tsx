import { useState } from "react"
import useWebSocket from "react-use-websocket"
import {HOST_URL} from "../../config"

const socketUrl = `ws://${HOST_URL}/ws/test`

const MessageInterface = () => {
    const [newMessage, setNewMessage] = useState<string[]>([])
    const [message, setMessage] = useState("")

    const { sendJsonMessage } = useWebSocket(socketUrl, {
        onOpen: () => {
            console.log("Connected!")
        },
        onClose: () => {
            console.log("Closed!")
        },
        onError: () => {
            console.log("Error!")
        },
        onMessage: (msg) => {
            const data = JSON.parse(msg.data)
            setNewMessage(prev_msg => [...prev_msg, data.new_message])
        }
    })

    const handleSendMessage = () => {
        sendJsonMessage({ type: "message", message });
        setMessage("");
    };

    return (
        <div>
            CHAT ROOM
            {newMessage.map((msg, index) => {
                console.log(msg)
                return(
                    <div key={index}>
                        <p>{msg}</p>
                    </div>
                );
            })}
            <form onSubmit={(e) => e.preventDefault()}>
                <label>Enter Message:
                    <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
                </label>
            <button onClick={handleSendMessage}>Send Message</button>
            </form>
        </div>
    )
}

export default MessageInterface