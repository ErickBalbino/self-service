function abrirModal(id) {
    document.getElementById('modal').style.display = 'block';

    document.getElementById('dashboard').style.filter = 'blur(2px)';
    document.getElementById('dashboard').style.pointerEvents = 'none';

    document.getElementById('panel').style.filter = 'blur(2px)';
    document.getElementById('panel').style.pointerEvents = 'none';
}

function fecharModal(id) {
    document.getElementById('modal').style.display = 'none';

    document.getElementById('dashboard').style.filter = 'blur(0px)';
    document.getElementById('dashboard').style.pointerEvents = 'inherit';

    document.getElementById('panel').style.filter = 'blur(0px)';
    document.getElementById('panel').style.pointerEvents = 'inherit';

}

window.addEventListener("click", () => {
    let abrirModal = document.getElementById('btn-abrir-modal');
    abrirModal.setAttribute("onclick", "abrirModal('modal');");

    let fecharModal = document.getElementById('btn-fechar-modal');
    fecharModal.setAttribute("onclick", "fecharModal('modal');");
});


