
const checkoxBurns = document.getElementById("check_burns");
checkoxBurns.addEventListener('click', async () => {
    const response = await fetch('/admin/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ burns: checkoxBurns.checked }),
        });

    console.log(JSON.stringify(response, null, 2))
})