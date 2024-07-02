
document.addEventListener('click', function(event) {
    const checkbox = document.getElementById('hamburger');
    const menu = document.querySelector('nav div div div');
    const isClickInsideMenu = menu.contains(event.target);
    const isClickHamburger = event.target === checkbox || event.target.closest('label[for="hamburger"]');
    
    if (!isClickInsideMenu && !isClickHamburger) {
        checkbox.checked = false;
    }
});
