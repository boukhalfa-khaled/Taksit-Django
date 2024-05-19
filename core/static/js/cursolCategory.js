// landingPage Category
// Grab wrapper nodes

const rootNodeCategory = document.querySelector(".emblaCategory ");
const viewportNodeCategory = rootNodeCategory.querySelector(
  ".emblaCategory__viewport"
);

const optionsCategory = { loop: false };
const pluginsCategory = [];

// Grab button nodes
const prevButtonNodeCategory = rootNodeCategory.querySelector(
  ".emblaCategory__prev"
);
const nextButtonNodeCategory = rootNodeCategory.querySelector(
  ".emblaCategory__next"
);

// Initialize the carousel
const emblaCategory = EmblaCarousel(
  viewportNodeCategory,
  optionsCategory,
  pluginsCategory
);

// Add click listeners
prevButtonNodeCategory.addEventListener(
  "click",
  emblaCategory.scrollPrev,
  false
);
nextButtonNodeCategory.addEventListener(
  "click",
  emblaCategory.scrollNext,
  false
);
