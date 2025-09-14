document.addEventListener('DOMContentLoaded', () => {
    const conteudo = document.getElementById('conteudo');
    const links = document.querySelectorAll('.menu a');

    function carregarPagina(pagina) {
        fetch(`/api/${pagina}`)
            .then(res => res.json())
            .then(data => {
                conteudo.innerHTML = data.html;
            });
    }

    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            carregarPagina(link.getAttribute('data-page'));
        });
    });

    carregarPagina('home');
});
