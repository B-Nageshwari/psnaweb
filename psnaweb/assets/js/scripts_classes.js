document.addEventListener('DOMContentLoaded', function() {
    // Get all containers representing the class dashboards
    var containers = document.querySelectorAll('.container');

    // Add click event listener to each container
    containers.forEach(function(container, index) {
        container.addEventListener('click', function() {
            // Determine which class dashboard was clicked based on its index
            var classIndex = index + 1;
            // Redirect to the corresponding class HTML page
            window.location.href = 'tutorclass' + classIndex + '.html';
        });
    });
});