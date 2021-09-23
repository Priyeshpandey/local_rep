// function animate(canvas,num,N,ctx) {
//     num--; if (num == 0) {
//         // ctx.clearRect(0, 0, canvas.width, canvas.height);    
//         num = N;
//         let x = Math.floor(Math.random() * canvas.width);
//         let y = Math.floor(Math.random() * canvas.height);
//         ctx.beginPath();
//         ctx.arc(x, y, 50, 0, 2 * Math.PI);
//         let color = "#"+Math.floor((Math.random() * 0xFFFFF * 10000)).toString(16);
//         // console.log(color);
//         ctx.fillStyle = color;
//         ctx.fill();
//     } else if (num == N/2) {
//         // ctx.clearRect(0, 0, canvas.width, canvas.height);    
//         let x = Math.floor(Math.random() * canvas.width);
//         let y = Math.floor(Math.random() * canvas.height);
//         ctx.beginPath();
//         ctx.rect(x,y, 100,100);
//         let color = "#"+Math.floor((Math.random() * 0xFFFFF * 10000)).toString(16);
//         // console.log(color);
//         ctx.fillStyle = color;
//         ctx.fill();
//     }
//     window.requestAnimationFrame(() => animate(canvas,num,N,ctx));
// }


class Canvas{
    constructor(canvas){
        this.canvas = canvas;
        this.ctx = this.canvas.getContext('2d');
        this.RENDER = 10;
        this.speed = this.RENDER;
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    get getSpeed(){
        return this.speed;
    }

    set decSpeed(x){
        this.speed--;
    }

    set resetSpeed(x){
        this.speed = this.RENDER;
    }

    animate() {
        decSpeed; let curspeed = this.getSpeed(); if (curspeed == 0) {
            // ctx.clearRect(0, 0, canvas.width, canvas.height);    
            // this.speed = this.RENDER;
            this.resetSpeed;
            let x = Math.floor(Math.random() * this.canvas.width);
            let y = Math.floor(Math.random() * this.canvas.height);
            this.ctx.beginPath();
            this.ctx.arc(x, y, 50, 0, 2 * Math.PI);
            let color = "#"+Math.floor((Math.random() * 0xFFFFF * 10000)).toString(16);
            // console.log(color);
            this.ctx.fillStyle = color;
            this.ctx.fill();
        } else if (curspeed == this.RENDER/2) {
            // ctx.clearRect(0, 0, canvas.width, canvas.height);    
            let x = Math.floor(Math.random() * this.canvas.width);
            let y = Math.floor(Math.random() * this.canvas.height);
            this.ctx.beginPath();
            this.ctx.rect(x,y, 100,100);
            let color = "#"+Math.floor((Math.random() * 0xFFFFF * 10000)).toString(16);
            // console.log(color);
            this.ctx.fillStyle = color;
            this.ctx.fill();
        }
        window.requestAnimationFrame(this.animate);
    }

    draw() {
        window.requestAnimationFrame(this.animate);
    }



}

function draw(){
    const canvas = document.getElementById('gameCanvas');
    let animator = new Canvas(canvas);
    console.log(animator.getSpeed)
    animator.draw();
    // canvas.width = window.innerWidth;
    // canvas.height = window.innerHeight;
    // let ctx = canvas.getContext('2d');
    // const N = 4;
    // let num = N;
    // window.requestAnimationFrame(() => animate(canvas,num,N,ctx));
    
}


