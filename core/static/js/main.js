const openaside = document.getElementById("open_aside-btn");
const aside = document.getElementById("aside");



document.onclick = function (e) {
  if (e.target.id !== 'aside' && e.target.id !== 'open_aside-btn'  ) 
  {
        openaside.classList.remove('active');
        aside.classList.remove('active');
        document.body.classList.remove('active');
  }
}


openaside.onclick = function () {
  openaside.classList.toggle('active')
  aside.classList.toggle('active')
  document.body.classList.toggle('active')
}