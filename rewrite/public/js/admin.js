const checkoxBurns = document.getElementById("check_burns");
checkoxBurns.addEventListener('click', async () => {
    const response = await fetch('/admin/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({burns: checkoxBurns.checked}),
    });

    console.log(JSON.stringify(response, null, 2))
})


const addEmployeeBtn = document.getElementById('addEmployeeBtn');

addEmployeeBtn.addEventListener('click', async (event) => {
    event.preventDefault();
    const first_name = document.getElementById('employeeFirstName').value;
    const last_name = document.getElementById('employeeLastName').value;
    const password = document.getElementById('employeePassword').value;

    if (first_name.trim() === '' || password.trim() === '' || last_name.trim() === '') {
        alert('All fields are required.');
        return;
    }

    await fetch('/admin/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
                first_name,
                last_name,
                password
            }
        ),
    }).then(async response => {
        const jsonResponse = await response.json();
        console.log(jsonResponse);
        if (jsonResponse.success) {
            document.getElementById('employeeFirstName').value = '';
            document.getElementById('employeeLastName').value = '';
            document.getElementById('employeePassword').value = '';
            document.querySelector('.status').innerText = jsonResponse.success;

        } else if (jsonResponse.error)
            document.querySelector('.status').innerText = jsonResponse.error;
    });
});