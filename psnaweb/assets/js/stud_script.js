document.getElementById('menuBtn').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    var content = document.getElementById('content');
    
    if (sidebar.style.width === '250px') {
        sidebar.style.width = '0';
        content.style.marginLeft = '0';
    } else {
        sidebar.style.width = '250px';
        content.style.marginLeft = '270px'; /* Adjusted to create space between sidebar and containers */
    }
});

// Open sidebar when clicking any icon in the sidebar
var sidebarLinks = document.querySelectorAll('#sidebar a');
sidebarLinks.forEach(function(link) {
    link.addEventListener('click', function() {
        var sidebar = document.getElementById('sidebar');
        var content = document.getElementById('content');
        sidebar.style.width = '250px';
        content.style.marginLeft = '270px'; /* Adjusted to create space between sidebar and containers */
    });
});
