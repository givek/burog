if (document.documentElement.clientWidth > 550) {
	
    const track = document.querySelector('.post-div');
    const slides = Array.from(track.children);

    const nextBtn = document.querySelector('.right-btn');
    const prevBtn = document.querySelector('.left-btn');

    const dotsNav = document.querySelector('.nav-btns');
    const dots = Array.from(dotsNav.children)

    const slideSize = slides[0].clientWidth;
    const slideWidth = (slideSize+65);


    slides.forEach((slide, index) => {
        slide.style.left = (slideWidth*index)+'px';
    });


    const moveToSlide = (track, currentPost, targetPost) => {
        track.style.transform = 'translateX(-'+targetPost.style.left+')';
        currentPost.classList.remove('current-post');
        targetPost.classList.add('current-post');
    }

    const updateDots = (currentDot, targetDot) => {
        currentDot.classList.remove('current-slide');
        targetDot.classList.add('current-slide');
    }


    prevBtn.addEventListener('click', e => {
        const currentPost = track.querySelector('.current-post');
        let prevPost = currentPost.previousElementSibling;
        currentDot = dotsNav.querySelector('.current-slide');
        let prevDot = currentDot.previousElementSibling;
        const postIndex = slides.findIndex(post => post===currentPost);
        
        if(postIndex===0){
            prevDot= dots[(slides.length)-1];
            prevPost = slides[(slides.length)-1]
            
            moveToSlide(track, currentPost, prevPost);
            updateDots(currentDot, prevDot);
        }
        moveToSlide(track, currentPost, prevPost);
        updateDots(currentDot, prevDot);    
    });


    nextBtn.addEventListener('click', e => {
        const currentPost = track.querySelector('.current-post')
        let nextPost = currentPost.nextElementSibling;
        currentDot = dotsNav.querySelector('.current-slide');
        let nextDot = currentDot.nextElementSibling;
        const postIndex = slides.findIndex(post => post===currentPost);

        if(postIndex===((slides.length)-1)){
            nextDot= dots[0];
            nextPost = slides[0];
            moveToSlide(track, currentPost, nextPost); 
            updateDots(currentDot, nextDot);
        }
        moveToSlide(track, currentPost, nextPost); 
        updateDots(currentDot, nextDot); 
    
    });


    setInterval(function(){
        setTimeout(document.querySelector('.right-btn').click(),0);
    }, 7000);


    dotsNav.addEventListener('click', e => {
        const targetDot = e.target.closest('button');

        if(!targetDot) return;

        currentPost = track.querySelector('.current-post');
        currentDot = dotsNav.querySelector('.current-slide');
        const targetIndex = dots.findIndex(dot => dot===targetDot)
        const targetPost = slides[targetIndex];

        moveToSlide(track, currentPost, targetPost);
        updateDots(currentDot, targetDot);   
    });

}