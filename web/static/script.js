// ===== SIDEBAR TOGGLE (future ready) =====
function toggleSidebar() {
    const sidebar = document.querySelector(".sidebar");
    const main = document.querySelector(".main");

    if (sidebar.style.width === "60px") {
        sidebar.style.width = "240px";
        main.style.marginLeft = "260px";
    } else {
        sidebar.style.width = "60px";
        main.style.marginLeft = "80px";
    }
}

// ===== TABLE SEARCH FILTER =====
function filterTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const filter = input.value.toLowerCase();
    const table = document.getElementById(tableId);
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        let txt = rows[i].textContent || rows[i].innerText;
        rows[i].style.display = txt.toLowerCase().includes(filter)
            ? ""
            : "none";
    }
}

// ===== TOAST NOTIFICATION =====
function showToast(message) {
    let toast = document.createElement("div");
    toast.className = "toast";
    toast.innerText = message;

    document.body.appendChild(toast);

    toast.style.display = "block";

    setTimeout(() => {
        toast.style.display = "none";
        document.body.removeChild(toast);
    }, 3000);
}

// ===== CONFIRM DELETE =====
function confirmAction(message) {
    return confirm(message);
}
