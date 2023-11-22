window.addEventListener('scroll',()=>{
    const {scrollTop,clientHeight,scrollHeight} = document.documentElement;
    if ((scrollTop+clientHeight)>=scrollHeight) {
      getContent((current_page));
    }
  });
  
  if (document.getElementById('Home')) {
    document.getElementById('Home').addEventListener('click', () => {
      document.getElementById('Header').scrollIntoView({behavior: "smooth"})
    })
  }

  if (document.getElementById('Contact')) {
    document.getElementById('Contact').addEventListener('click', () => {
      document.getElementById('Contact-us').scrollIntoView({behavior: "smooth"})
    })
  }
  


  function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }
  