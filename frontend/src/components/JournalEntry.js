import React from 'react';

const JournalEntry = ({ entry }) => {
    return (
        <div className="journal-entry">
            <h2>{entry.title}</h2>
            <p>{entry.content}</p>
            <small>{new Date(entry.timestamp).toLocaleString()}</small>
        </div>
    );
};

export default JournalEntry;