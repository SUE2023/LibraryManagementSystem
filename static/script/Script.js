function handleRoleChange() {
    var role = document.getElementById('role').value;
    var vendorFields = document.getElementById('vendorFields');
    if (role === 'vendor') {
        vendorFields.style.display = 'block';
    } else {
        vendorFields.style.display = 'none';
    }
}
