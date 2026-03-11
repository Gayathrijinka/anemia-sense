const canvas = document.getElementById("background");
const ctx = canvas.getContext("2d");
let anemiaCells = [];

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
window.addEventListener("resize", resize);
resize();

class AnemiaCell {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * -canvas.height;
        this.size = Math.random() * 30 + 10;
        this.speed = Math.random() * 2 + 1;
        this.opacity = Math.random() * 0.5 + 0.3;
    }
    update() {
        this.y += this.speed;
        if (this.y > canvas.height) {
            this.y = 0;
            this.x = Math.random() * canvas.width;
        }
    }
    draw() {
        ctx.beginPath();
        ctx.fillStyle = `rgba(255, 0, 0, ${this.opacity})`;
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}
for (let i = 0; i < 80; i++) anemiaCells.push(new AnemiaCell());

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    anemiaCells.forEach(cell => { cell.update(); cell.draw(); });
    requestAnimationFrame(animate);
}
animate();
