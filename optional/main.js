// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Mobile Menu Toggle
document.querySelector('.menu-toggle').addEventListener('click', () => {
    document.querySelector('nav').classList.toggle('active');
});

// Countdown Timer
const countdown = () => {
    const finaleDate = new Date('Dec 15, 2024 00:00:00').getTime();
    const now = new Date().getTime();
    const diff = finaleDate - now;

    // Calculate days, hours, minutes
    document.getElementById('days').innerText = Math.floor(diff / (1000 * 60 * 60 * 24));
    document.getElementById('hours').innerText = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    document.getElementById('minutes').innerText = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
};

setInterval(countdown, 1000);

// Form Submission
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Application submitted! We’ll contact you soon.');
});