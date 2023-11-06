import { useEffect, useState } from "react"
import useWebSocket from "react-use-websocket"

const socketUrl = "ws://127.0.0.1:8000/ws/test"

const Server = () => {
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
            console.log("Received message:", msg);
            const data = JSON.parse(msg.data)
            setNewMessage(prev_msg => [...prev_msg, data.new_message])
        }
    })

    const handleSendMessage = () => {
        console.log("Sending message:", message);
        sendJsonMessage({ type: "message", message });
    };
    
    useEffect(()=>{
        console.log(newMessage)
    }, [newMessage])

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

export default Server