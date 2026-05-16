/* ====================================
   DevSquad — Main JavaScript
   ==================================== */

document.addEventListener('DOMContentLoaded', function () {

    // ---- Navbar Scroll Behavior ----
    const navbar = document.getElementById('navbar');
    const scrollTopBtn = document.getElementById('scroll-top-btn');

    const navbarInner = document.getElementById('navbar-inner');
    function handleScroll() {
        const scrollY = window.scrollY;

        // Navbar: transparent → glass
        if (scrollY > 50) {
            navbar.classList.add('scrolled');
            if (navbarInner) navbarInner.classList.replace('h-20', 'h-16');
        } else {
            navbar.classList.remove('scrolled');
            if (navbarInner) navbarInner.classList.replace('h-16', 'h-20');
        }

        // Scroll-to-top button visibility
        if (scrollTopBtn) {
            if (scrollY > 500) {
                scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none');
                scrollTopBtn.classList.add('opacity-100', 'pointer-events-auto');
            } else {
                scrollTopBtn.classList.add('opacity-0', 'pointer-events-none');
                scrollTopBtn.classList.remove('opacity-100', 'pointer-events-auto');
            }
        }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Initial check

    // Scroll-to-top click
    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ---- Mobile Menu Toggle ----
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });

        // Close menu when clicking a link
        mobileMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // ---- Scroll Reveal (IntersectionObserver) ----
    const revealElements = document.querySelectorAll('.scroll-reveal');

    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    // Respect animation-delay from inline styles
                    const delay = entry.target.style.animationDelay;
                    if (delay) {
                        const ms = parseFloat(delay) * (delay.includes('ms') ? 1 : 1000);
                        setTimeout(function () {
                            entry.target.classList.add('revealed');
                        }, ms);
                    } else {
                        entry.target.classList.add('revealed');
                    }
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(function (el) {
            revealObserver.observe(el);
        });
    } else {
        // Fallback for old browsers
        revealElements.forEach(function (el) {
            el.classList.add('revealed');
        });
    }

    // ---- Auto-dismiss Toast Messages ----
    const messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        const toasts = messageContainer.querySelectorAll('.message-toast');
        toasts.forEach(function (toast, index) {
            setTimeout(function () {
                toast.style.transition = 'all 0.5s ease';
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(100px)';
                setTimeout(function () {
                    toast.remove();
                    // Remove container if empty
                    if (messageContainer.children.length === 0) {
                        messageContainer.remove();
                    }
                }, 500);
            }, 4000 + (index * 500));
        });
    }

    // ---- Smooth Scroll for Anchor Links ----
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ---- Optimized Video Loading ----
    const heroVideo = document.getElementById('hero-video');
    if (heroVideo) {
        const sources = heroVideo.querySelectorAll('source');
        if (sources.length > 0) {
            // Wait for window load to ensure everything else is ready
            window.addEventListener('load', function() {
                sources.forEach(source => {
                    if (source.dataset.src) {
                        source.src = source.dataset.src;
                    }
                });
                heroVideo.load();
                
                heroVideo.addEventListener('canplaythrough', function() {
                    heroVideo.classList.remove('opacity-0');
                    heroVideo.classList.add('opacity-100');
                }, { once: true });
            });
        }
    }

});
