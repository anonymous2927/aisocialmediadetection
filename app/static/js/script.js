// Simple JS to handle animations and form actions

// Handle the form submit button animations and actions (if you have forms)
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('mouseover', () => {
        button.style.transform = "scale(1.1)";
        button.style.transition = "transform 0.2s";
    });

    button.addEventListener('mouseout', () => {
        button.style.transform = "scale(1)";
    });
});

// Scroll to top function for smooth scrolling (optional)
window.addEventListener("scroll", () => {
    const backToTopButton = document.getElementById("backToTop");
    if (window.scrollY > 500) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
});

document.getElementById("backToTop")?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Dynamic motivational quote display (optional feature)
const motivationalQuotes = [
    "Protecting your digital life, one profile at a time.",
    "Your digital presence matters, stay safe online!",
    "Empowering users with AI-driven social media protection.",
    "Keep your accounts safe, and your data secure!",
    "Online safety starts with awareness—act now!"
];

// Change quote on page load
document.addEventListener("DOMContentLoaded", () => {
    const quoteText = document.querySelector(".quote-text");
    const randomQuote = motivationalQuotes[Math.floor(Math.random() * motivationalQuotes.length)];
    quoteText.textContent = randomQuote;
});

// Show loading spinner while page content is loading
document.addEventListener("DOMContentLoaded", function() {
    const loadingSpinner = document.querySelector('.loading-spinner');
    loadingSpinner.style.display = "none"; // Hide loading spinner when content is loaded
});

// Function to simulate backend interaction (e.g., form submission)
const signupForm = document.querySelector('form');
if (signupForm) {
    signupForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevent default form submit for demo
        
        const email = document.querySelector("input[name='email']").value;
        const password = document.querySelector("input[name='password']").value;
        
        if (email && password) {
            // Show loading spinner while making the request
            const loadingSpinner = document.querySelector('.loading-spinner');
            loadingSpinner.style.display = "block"; // Show the spinner

            // Example fetch request to backend (Flask API)
            fetch('/api/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            })
            .then(response => response.json())
            .then(data => {
                loadingSpinner.style.display = "none"; // Hide the spinner when done
                alert("Signup Successful!");
            })
            .catch(error => {
                loadingSpinner.style.display = "none"; // Hide the spinner in case of error
                alert("Error occurred. Please try again.");
            });
        } else {
            alert("Please fill in all fields.");
        }
    });
}
