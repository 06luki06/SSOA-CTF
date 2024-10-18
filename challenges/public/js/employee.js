const pathSegments = window.location.pathname.split('/');
const recipientId = pathSegments[pathSegments.length - 1];
console.log(recipientId);

const commentBtn = document.getElementById('commentBtn');
commentBtn.addEventListener('click', async (event) => {
    event.preventDefault();
    const comment = document.getElementById('comment').value;
    await fetch('/comments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comment, recipientId }),
    });
    window.location.reload();
});

const commentContainer = document.getElementById('comments-con');
fetch(`/comments/${recipientId}`)
    .then(response => response.json())
    .then(result => commentContainer.innerHTML = JSON.stringify(result, null, 2));


