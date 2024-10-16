const commentBtn = document.getElementById('commentBtn');
commentBtn.addEventListener('click', async (event) => {
    event.preventDefault();

    const comment = document.getElementById('comment').value;

    await fetch('/comments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comment }),
    });

    window.location.reload();
});