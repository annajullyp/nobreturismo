
(function () {
    var dados = document.getElementById('experiencias-data');

    // Encerra se não houver dados do Django.
    if (!dados) return;

    var slides = JSON.parse(dados.textContent);

    var image = document.getElementById('slideImage');
    var tag = document.getElementById('slideTag');
    var title = document.getElementById('slideTitle');
    var text = document.getElementById('slideText');
    var current = document.getElementById('slideCurrent');
    var total = document.getElementById('slideTotal');
    var dotsContainer = document.getElementById('dots');
    var prev = document.getElementById('prevSlide');
    var next = document.getElementById('nextSlide');

    // Cria um indicador para cada experiência.
    dotsContainer.innerHTML = '';

    slides.forEach(function (slide, index) {
        var dot = document.createElement('button');

        dot.className = 'dots__item';
        dot.type = 'button';
        dot.setAttribute('aria-label', 'Slide ' + (index + 1));

        dot.addEventListener('click', function () {
            i = index;
            render();
        });

        dotsContainer.appendChild(dot);
    });

    var dots = dotsContainer.querySelectorAll('.dots__item');
    var i = 0;

    // Formata números: 01, 02, 03...
    function formatNumber(number) {
        return String(number).padStart(2, '0');
    }

    function render() {
        if (slides.length === 0) return;

        var slide = slides[i];

        image.style.backgroundImage = slide.foto
            ? "url('" + slide.foto + "')"
            : 'none';

        tag.textContent = slide.tag || 'Experiência';
        title.textContent = slide.nome;
        text.textContent = slide.descricao;

        current.textContent = formatNumber(i + 1);
        total.textContent = formatNumber(slides.length);

        dots.forEach(function (dot, index) {
            dot.classList.toggle('is-active', index === i);
        });

        // Com uma única experiência, não há necessidade de navegar.
        prev.disabled = slides.length <= 1;
        next.disabled = slides.length <= 1;
    }

    prev.addEventListener('click', function () {
        if (slides.length <= 1) return;

        i = (i - 1 + slides.length) % slides.length;
        render();
    });

    next.addEventListener('click', function () {
        if (slides.length <= 1) return;

        i = (i + 1) % slides.length;
        render();
    });

    render();
})();
