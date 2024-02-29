function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
        sidebar.style.display = 'block';
        document.addEventListener('click', closeSidebarOutsideClick);
    } else {
        sidebar.style.display = 'none';
        document.removeEventListener('click', closeSidebarOutsideClick);
    }
}

function closeSidebarOutsideClick(event) {
    var sidebar = document.getElementById('sidebar');
    var menuBtn = document.querySelector('.menu-btn');
    if (!sidebar.contains(event.target) && event.target !== menuBtn) {
        sidebar.style.display = 'none';
        document.removeEventListener('click', closeSidebarOutsideClick);
    }
}
