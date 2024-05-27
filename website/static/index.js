function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = '/';
    });
}
function shareNote(noteId) {
    var email = document.getElementById('shareNote').value; // Módosítás: 'shareEmail' id-t használunk
    fetch('/share-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId, email: email }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            alert('A jegyzet megosztva a(z) ' + email + ' email címmel.');
        } else {
            alert('A jegyzet megosztása sikertelen.');
        }
    });
}