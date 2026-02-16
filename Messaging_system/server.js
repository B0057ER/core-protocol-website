const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;
const messagesFile = path.join(__dirname, 'messages.json');

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// Load messages from file
function loadMessages() {
    if (fs.existsSync(messagesFile)) {
        return JSON.parse(fs.readFileSync(messagesFile, 'utf8'));
    }
    return [];
}

// Save messages to file
function saveMessages(messages) {
    fs.writeFileSync(messagesFile, JSON.stringify(messages, null, 2));
}

// GET all messages
app.get('/api/messages', (req, res) => {
    const messages = loadMessages();
    res.json(messages);
});

// POST a new message
app.post('/api/messages', (req, res) => {
    const { text } = req.body;
    if (!text || text.trim() === '') {
        return res.status(400).json({ error: 'Message cannot be empty' });
    }

    const messages = loadMessages();
    const newMessage = {
        id: Date.now(),
        type: 'user',
        text: text.trim(),
        timestamp: new Date().toISOString()
    };
    messages.push(newMessage);
    saveMessages(messages);
    res.json(newMessage);
});

// DELETE all messages
app.delete('/api/messages', (req, res) => {
    saveMessages([]);
    res.json({ success: true });
});

// DELETE a specific message
app.delete('/api/messages/:id', (req, res) => {
    const { id } = req.params;
    let messages = loadMessages();
    messages = messages.filter(msg => msg.id !== parseInt(id));
    saveMessages(messages);
    res.json({ success: true });
});

app.listen(PORT, () => {
    console.log(`Messaging server running on http://localhost:${PORT}`);
    console.log('Messages will be shared across all devices on your network!');
});
