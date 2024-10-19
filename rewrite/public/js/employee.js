document.addEventListener('DOMContentLoaded', () => {
    const recipientId = document.getElementById('recipientId').value;

    const commentBtn = document.getElementById('commentBtn');
    commentBtn.addEventListener('click', async (event) => {
        event.preventDefault();
        const comment = document.getElementById('comment').value;
        if (comment.trim() === '') {
            alert('Comment cannot be empty.');
            return;
        }
        await fetch('/comments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ comment, recipientId }),
        });
        document.getElementById('comment').value = '';
        fetchComments(); // Refresh comments
    });

    const commentContainer = document.getElementById('comments-con');

    async function fetchComments() {
        const response = await fetch(`/comments/${recipientId}`);
        const comments = await response.json();
        commentContainer.innerHTML = ''; // Clear previous comments
        comments["comments"].forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.classList.add('comment');
            commentElement.innerHTML = `<strong>${comment.name}:</strong> ${comment.comment}`;
            commentContainer.appendChild(commentElement);
        });
    }

    // Fetch comments on page load
    fetchComments();
});
