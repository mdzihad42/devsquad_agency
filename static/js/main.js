/* ====================================
   mzify — Main JavaScript
   ==================================== */

document.addEventListener('DOMContentLoaded', function () {

    // ---- Global Elements ----
    const navbar = document.getElementById('navbar');
    const scrollTopBtn = document.getElementById('scroll-top-btn');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    // ---- Navbar & Scroll Visibility ----
    function handleScroll() {
        const scrollY = window.scrollY;

        // Navbar scrolled state
        if (navbar) {
            if (scrollY > 80) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        // Scroll-to-top visibility
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

    // ---- Mobile Menu Toggle (Sophisticated Glassy Version) ----
    if (mobileMenuBtn && mobileMenu) {
        const links = mobileMenu.querySelectorAll('a, .pt-8');

        const openMenu = () => {
            mobileMenu.classList.remove('opacity-0', 'pointer-events-none');
            mobileMenu.classList.add('opacity-100', 'pointer-events-auto');
            document.body.style.overflow = 'hidden';

            // Staggered entry
            links.forEach((link, index) => {
                setTimeout(() => {
                    link.classList.remove('translate-y-8', 'opacity-0');
                    link.classList.add('translate-y-0', 'opacity-100');
                }, 100 + (index * 80));
            });
        };

        const closeMenu = () => {
            mobileMenu.classList.remove('opacity-100', 'pointer-events-auto');
            mobileMenu.classList.add('opacity-0', 'pointer-events-none');
            document.body.style.overflow = '';

            // Reset for next time
            links.forEach((link) => {
                link.classList.add('translate-y-8', 'opacity-0');
                link.classList.remove('translate-y-0', 'opacity-100');
            });
        };

        mobileMenuBtn.addEventListener('click', openMenu);

        // Event delegation for closing
        mobileMenu.addEventListener('click', function (e) {
            if (e.target.closest('#close-menu-btn') || e.target.closest('a')) {
                closeMenu();
            }
        });
    }

    // ---- Scroll Reveal (IntersectionObserver) ----
    const revealElements = document.querySelectorAll('.scroll-reveal');

    if ('IntersectionObserver' in window && revealElements.length > 0) {
        const revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
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
                    if (toast.parentNode) {
                        toast.remove();
                    }
                    if (messageContainer && messageContainer.children.length === 0) {
                        messageContainer.remove();
                    }
                }, 500);
            }, 4000 + (index * 500));
        });
    }

    // ---- Smooth Scroll for Anchor Links ----
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });

    // ---- Optimized Video Loading ----
    const heroVideo = document.getElementById('hero-video');
    if (heroVideo) {
        const sources = heroVideo.querySelectorAll('source');
        if (sources.length > 0) {
            window.addEventListener('load', function () {
                sources.forEach(source => {
                    if (source.dataset.src) {
                        source.src = source.dataset.src;
                    }
                });
                heroVideo.load();
                heroVideo.addEventListener('canplaythrough', function () {
                    heroVideo.classList.remove('opacity-0');
                    heroVideo.classList.add('opacity-100');
                }, { once: true });
            });
        }
    }
});
