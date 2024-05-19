const rootNode = document.querySelector(".embla");
const viewportNode = rootNode.querySelector(".embla__viewport");

const options = { loop: true};
const plugins = [];

const prevButtonNode = rootNode.querySelector(".embla__prev");
const nextButtonNode = rootNode.querySelector(".embla__next");

const embla = EmblaCarousel(viewportNode, options,plugins);

prevButtonNode.addEventListener("click", embla.scrollPrev, false);
nextButtonNode.addEventListener("click", embla.scrollNext, false);

// price cards
const cards = document.querySelectorAll('.card');
const orderButton = document.querySelector('.order');

cards.forEach(card => {
  card.addEventListener('click', () => {
    cards.forEach(card => {
      card.classList.remove('clicked');
    });

    card.classList.add('clicked');
  });
});

orderButton.addEventListener('click', () => {
  const clickedCard = document.querySelector('.card.clicked');
    const cardId = clickedCard.dataset.cardId;
    const url = `card/${cardId}`;
    window.location.href = url;
});