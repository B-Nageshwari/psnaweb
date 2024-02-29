document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('personalInfoForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        // Fetch form data
        const fullName = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const address = document.getElementById('address').value;

        // Perform validation if needed

        // Here, you can send the data to the server for processing or update local storage, etc.
        console.log('Full Name:', fullName);
        console.log('Email:', email);
        console.log('Phone:', phone);
        console.log('Address:', address);

        // Optionally, you can display a success message or perform other actions
        alert('Personal information updated successfully!');
    });
});
