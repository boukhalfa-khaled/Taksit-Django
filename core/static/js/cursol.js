// landingPage
// Grab wrapper nodes
const rootNode = document.querySelector(".embla");
const viewportNode = rootNode.querySelector(".embla__viewport");

const options = { loop: true };
const plugins = [
  EmblaCarouselAutoplay({ stopOnInteraction: false, delay: 5000 }),
];

// Grab button nodes
const prevButtonNode = rootNode.querySelector(".embla__prev");
const nextButtonNode = rootNode.querySelector(".embla__next");

// Initialize the carousel
const embla = EmblaCarousel(viewportNode, options, plugins);

// Initialize AOS
AOS.init({
  duration:"1200",
  once: false,
});

// Function to handle slide change
const handleSlideChange = () => {
  // Get the current slide index
  const currentIndex = embla.selectedScrollSnap();

  // Get all slide items
  const slideItems = Array.from(viewportNode.querySelectorAll(".embla__slide"));

  // Loop through each slide item
  slideItems.forEach((slide, index) => {
  // Check if the slide is in view
  if (index === currentIndex) {
    const content = slide.querySelector('.content');
    content.setAttribute("data-aos", "fade-left");
    content.style.opacity= "1";
    content.classList.add('.active')
  } else {
    const content = slide.querySelector('.content');
    content.removeAttribute("data-aos");
    content.style.opacity= "0";
  }
  });


  // Refresh AOS to apply animations
  AOS.refreshHard();
};


// Listen for slide change events
embla.on("select", handleSlideChange);

// Add click listeners for prev and next buttons
prevButtonNode.addEventListener("click", () => {
  embla.scrollPrev();
});

nextButtonNode.addEventListener("click", () => {
  embla.scrollNext();
});
console.log('django')
