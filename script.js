
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target){
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple animation on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });

    // Cookie Banner Logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-cookies');
    const necessaryBtn = document.getElementById('necessary-cookies');
    
    const cookiesAccepted = localStorage.getItem('cookiesAccepted');
    
    if (!cookiesAccepted) {
        // Show banner with a small delay for smoother entrance
        setTimeout(() => {
            cookieBanner.style.display = 'block';
        }, 1000);
    }
    
    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.style.display = 'none';
        });
    }

    if (necessaryBtn) {
        necessaryBtn.addEventListener('click', () => {
             // Treat "Necessary Only" as accepted for the purpose of hiding the banner
             // In a real implementation, this would handle consent status differently
            localStorage.setItem('cookiesAccepted', 'necessary');
            cookieBanner.style.display = 'none';
        });
    }

    // Elements to animate
    const cards = document.querySelectorAll('.card');
    const steps = document.querySelectorAll('.step');
    const faqItems = document.querySelectorAll('.faq-item');
    const formGroups = document.querySelectorAll('.form-group');

    [...cards, ...steps, ...faqItems, ...formGroups].forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});
