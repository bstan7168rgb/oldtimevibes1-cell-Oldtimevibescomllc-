# Old-Time Vibes LLC — Master Ecosystem README (`README.md`)

**Governing Entity:** Old-Time Vibes LLC (Ponca City & McCord, Oklahoma | D-U-N-S: `14-219-7315`)  
**Founder, Principal Systems Architect & CEO:** Stanley Joseph Brown ("Kodak")  
**Primary Domains:** `https://oldtimevibes.com` | `https://genxnext.online` | `https://genx.online` | `https://online.genxnext.app`  
**Contact:** `oldtimevibes1@gmail.com`  
**Patent Priority Anchor:** November 28, 2025 (`USPTO-EXP-OTV-R2IO-2026-01` — 20-Claim Utility Patent Portfolio; Nonprovisional Conversion Deadline: **November 28, 2026**)  

---

## 1. Executive Overview

Old-Time Vibes LLC engineers sovereign, local-first edge computing hardware, humanoid robotics, privacy-hardened AI companions, and decentralized agentic commerce infrastructure. By decoupling on-device neural processing and hardware safety interlocks from continuous third-party cloud telemetry, every platform operates with deterministic low latency, strict zero-PII child and patient privacy compliance (COPPA, HIPAA, CIPA, ASTM F963-23), and automated cryptographic auditability.

---

## 2. Modular Department & Repository Architecture

All repositories, cloud environments, and hardware/software deliverables follow Old-Time Vibes LLC's four-department organizational hierarchy:

```text
old-time-vibes-ecosystem/
├── 01_hardware/
│   ├── cad_models/          # OpenSCAD, FreeCAD TechDraw & Onshape assemblies (R2IO, Barnaby capsule)
│   ├── bom/                 # Verified bills of materials & manufacturer RFQ specs (platform_parts_manifest.csv)
│   └── firmware/            # ESP32-S3 bare-metal RTOS (ESP-IDF/ADF), RK3588 C++20 enclaves, eFuse & QA jigs
├── 02_software/
│   ├── edge_ai/             # Quantized SLMs (GGUF/INT4), <300 KB LiteRT KWS/VAD, Software LOTO, PTT listener
│   ├── orchestration/       # FastMCP servers (:8000/:8080), Express MCP Gateway, Cloudflare Workers, UCP/A2A
│   └── interfaces/          # Web storefronts (oldtimevibes.com, genxnext.online), Android 16 app, MV3 extension
├── 03_operations/
│   ├── corporate_legal/     # Form C Reg CF disclosures, Mutual NDAs, LICENSE.md, NOTICE.md, TERMS.md, PRIVACY.md
│   ├── treasury/            # Stripe Connect UCP settlement hooks, Addendum V3 waterfall, Base L2 contracts
│   └── patents/             # USPTO 20-claim DOCX specs, formal vector drawings, DTSA trade-secret walls
└── 04_creative/
    ├── publishing/          # White papers (OTV-WP-2026-004-REV2), The Gemini Tales, Human-AI Collaboration series
    ├── audio_production/    # Workshop playlists, Suno stems, ISRC/ISWC audio POD middleware
    └── media_assets/        # Barnaby's Animals & Agents episodes, XR 3D apparel assets, Merchant Center feeds
git remote add origin https://github.com/bstan7168rgb/oldtimevibes1-cell-Oldtimevibescomllc-.git
git branch -M main
git push -u origin maindocker run --rm -it gradle/develocityctldocker pull gradle/develocityctl[https://console.developers.google.com/apis/api/drivemcp.googleapis.com/overview?project=426476471325](https://console.developers.google.com/apisecho "# oldtimevibes1-cell-Oldtimevibescomllc-" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/bstan7168rgb/oldtimevibes1-cell-Oldtimevibescomllc-.git
git push -u origin main<!DOCTYPE html>
<html>
  <head>
    <title>Hello, World!</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
      <h1 class="title">Hello World!</h1>
      <p id="currentTime"></p>
      <script src="script.js"></script>
  </body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Old-Time Vibes | Music Store, Media & AI</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script async src="https://js.stripe.com/v3/buy-button.js"></script>
    <script src="https://unpkg.com/imagekit-javascript/dist/imagekit.min.js"></script>
    <link q="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-functions-compat.js"></script>
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'vintage-gold': '#CC8847',
                        'deep-wood': '#5e352d',
                        'forest-green': '#385b3b',
                        'cream-bg': '#f4f0e6',
                        'dark-bg': '#1a1a1a',
                        'dark-card': '#2d2d2d'
                    }
                }
            }
        }

        const firebaseConfig = {
            apiKey: "YOUR_FIREBASE_API_KEY", 
            authDomain: "oldtimevibes-d14bd.firebaseapp.com",
            databaseURL: "https://oldtimevibes-d14bd-default-rtdb.firebaseio.com",
            projectId: "oldtimevibes-d14bd",
            storageBucket: "oldtimevibes-d14bd.firebasestorage.app",
            messagingSenderId: "637974675702",
            appId: "1:637974675702:web:838ba1ccb1cf676486ecd7",
            measurementId: "G-2SB8R4434G"
        };
        firebase.initializeApp(firebaseConfig);
        const functions = firebase.functions();
    </script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
        
        body { 
            font-family: 'Inter', sans-serif; 
            background-color: #1a1a1a; 
            color: white; 
            background-image: 
                linear-gradient(rgba(26, 26, 26, 0.92), rgba(26, 26, 26, 0.96)),
                url('https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763540953617.jpg'); 
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
        }
        
        .btn-primary { background-color: #CC8847; color: #1a1a1a; transition: all 0.3s ease; }
        .btn-primary:hover { background-color: white; transform: translateY(-2px); }
        
        .nav-link { color: #d1d5db; cursor: pointer; transition: all 0.3s ease; white-space: nowrap; }
        .nav-link:hover { color: #CC8847; }
        .nav-link.active { color: #CC8847; border-bottom: 2px solid #CC8847; }
        
        .page-section { display: none; animation: fadeIn 0.5s ease-in-out; min-height: calc(100vh - 200px); }
        .page-section.active { display: block; }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .admin-edit-overlay {
            position: absolute; inset: 0; background-color: rgba(0,0,0,0.7);
            display: flex; align-items: center; justify-content: center;
            opacity: 0; transition: opacity 0.2s; cursor: pointer;
        }
        .group:hover .admin-edit-overlay { opacity: 1; }
        
        .header-hidden { transform: translateY(-100%); }
        #main-header { transition: transform 0.3s ease-in-out; }
        
        .chat-bubble { padding: 10px 15px; border-radius: 15px; margin-bottom: 10px; max-width: 80%; font-size: 0.95rem; }
        .chat-user { background-color: #385b3b; color: white; align-self: flex-end; margin-left: auto; border-bottom-right-radius: 2px; }
        .chat-ai { background-color: #2d2d2d; color: #d1d5db; border: 1px solid #CC8847; align-self: flex-start; border-bottom-left-radius: 2px; }
        
        .custom-scrollbar::-webkit-scrollbar { width: 8px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #2d2d2d; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background-color: #CC8847; border-radius: 4px; }
        
        .parental-control-form {
            background: linear-gradient(135deg, #2d1b10 0%, #4a2c1a 100%);
            border: 1px solid #8b4513;
            box-shadow: 0 0 20px rgba(139, 69, 19, 0.5);
        }
        .control-item {
            background-color: rgba(45, 45, 45, 0.7);
            border: 1px solid #5d4037;
            transition: all 0.3s ease;
        }
        .control-item:hover {
            background-color: rgba(70, 50, 30, 0.8);
            transform: translateY(-3px);
        }
        
        .toggle-switch { position: relative; display: inline-block; width: 50px; height: 24px; }
        .toggle-switch input { opacity: 0; width: 0; height: 0; }
        .slider-switch {
            position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
            background-color: #ccc; transition: .4s; border-radius: 24px;
        }
        .slider-switch:before {
            position: absolute; content: ""; height: 16px; width: 16px; left: 4px; bottom: 4px;
            background-color: white; transition: .4s; border-radius: 50%;
        }
        input:checked + .slider-switch { background-color: #CC8847; }
        input:checked + .slider-switch:before { transform: translateX(26px); }
    </style>
</head>
<body class="bg-dark-bg min-h-screen flex flex-col">
    
    <header id="main-header" class="bg-deep-wood shadow-2xl sticky top-0 z-50 border-b border-vintage-gold">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col md:flex-row justify-between items-center">
            <div class="flex justify-between w-full md:w-auto items-center mb-2 md:mb-0 gap-4">
                <a href="#" onclick="showPage('home')" class="flex items-center gap-2 group">
                    <img src="https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763540953617.jpg" alt="OTV Logo" class="h-12 w-12 rounded-full border-2 border-vintage-gold shadow-lg group-hover:scale-105 transition">
                    <span class="font-bold text-xl tracking-wide hidden sm:block text-white">Old-Time Vibes</span>
                </a>
                <button onclick="toggleCart()" class="md:hidden bg-vintage-gold text-dark-bg font-bold py-1 px-3 rounded-full shadow-lg">
                    <i class="fas fa-shopping-cart"></i> <span id="cart-count-mobile" class="ml-1 text-xs">0</span>
                </button>
            </div>
            <nav class="flex flex-wrap justify-center gap-4 text-sm font-medium">
                <a onclick="showPage('home')" class="nav-link active" id="nav-home">Home</a>
                <a onclick="showPage('shop')" class="nav-link" id="nav-shop">Music Store</a>
                <a onclick="showPage('media')" class="nav-link" id="nav-media">Media</a>
                <a onclick="showPage('ai-assistant')" class="nav-link text-vintage-gold" id="nav-ai"><i class="fas fa-robot mr-1"></i> Ask Barnaby</a>
                <a onclick="showPage('contact')" class="nav-link" id="nav-contact">Contact</a>
                <a onclick="showPage('admin')" class="nav-link text-red-400" id="nav-admin">Admin</a>
                <a onclick="showPage('parental-controls')" class="nav-link text-purple-400" id="nav-parental">Parental Controls</a>
            </nav>
            <div class="hidden md:block ml-4">
                <button onclick="toggleCart()" class="bg-vintage-gold hover:bg-white text-dark-bg font-bold py-2 px-4 rounded-full shadow-lg transition transform hover:-translate-y-1">
                    <i class="fas fa-shopping-cart mr-2"></i> Cart
                    <span id="cart-count" class="ml-2 bg-dark-bg text-white text-xs px-2 py-1 rounded-full">0</span>
                </button>
            </div>
        </div>
    </header>

    <main class="flex-grow container mx-auto p-4 sm:p-8 relative">
        
        <!-- Home Page -->
        <section id="home-page" class="page-section active">
            <div class="text-center pt-10 pb-12">
                <img src="https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763540953617.jpg" alt="Logo" class="h-56 w-56 rounded-full border-4 border-vintage-gold shadow-2xl mx-auto mb-6">
                <h1 class="text-5xl md:text-6xl font-extrabold text-white mb-6">Old-Time Vibes <span class="text-vintage-gold">Supply</span></h1>
                <p class="text-gray-400 mb-10 text-xl max-w-2xl mx-auto">Authentic gear, vintage apparel, and master-crafted instruments.</p>
                <div class="flex justify-center gap-4 flex-wrap">
                    <button onclick="showPage('shop')" class="bg-forest-green hover:bg-vintage-gold text-white font-bold py-3 px-8 rounded-lg shadow-lg transition transform hover:scale-105">Shop Gear</button>
                    <button onclick="showPage('ai-assistant')" class="bg-dark-card border border-vintage-gold text-vintage-gold hover:bg-vintage-gold hover:text-black font-bold py-3 px-8 rounded-lg shadow-lg">Talk to Barnaby</button>
                </div>
            </div>
        </section>

        <!-- Music Store -->
        <section id="shop-page" class="page-section">
            <h2 class="text-4xl font-bold text-vintage-gold mb-8 border-b border-gray-700 pb-4">Music Equipment & Store</h2>
            <div id="store-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6"></div>
        </section>

        <!-- Media Lounge -->
        <section id="media-page" class="page-section">
            <h2 class="text-4xl font-bold text-white mb-8 border-b border-gray-700 pb-4">Media Lounge</h2>
            <div class="grid md:grid-cols-2 gap-8 text-gray-300">
                <div class="bg-dark-card p-6 rounded-lg shadow-xl border-t-4 border-vintage-gold">
                    <h3 class="text-2xl font-bold text-white mb-2"><i class="fas fa-music mr-2 text-vintage-gold"></i>Shop Playlist</h3>
                    <audio id="audio-player" controls class="w-full rounded shadow-lg mb-4 bg-gray-700"></audio>
                    <div class="flex justify-between items-center bg-black/40 p-3 rounded border border-gray-700">
                        <p class="text-sm italic truncate mr-2">Now Playing: <span id="current-track-name" class="text-vintage-gold font-bold">Waiting...</span></p>
                        <button onclick="nextTrack()" class="text-xs bg-gray-700 hover:bg-vintage-gold hover:text-black px-3 py-1 rounded transition">Skip >></button>
                    </div>
                </div>
                <div class="bg-dark-card p-6 rounded-lg shadow-xl border-t-4 border-forest-green">
                    <h3 class="text-2xl font-bold text-white mb-4"><i class="fas fa-video mr-2 text-forest-green"></i>Featured Video</h3>
                    <div class="aspect-w-16 aspect-h-9 bg-black rounded overflow-hidden">
                        <video controls class="w-full rounded shadow-lg" preload="metadata">
                            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                            Your browser does not support video.
                        </video>
                    </div>
                </div>
            </div>
        </section>

        <!-- AI Assistant -->
        <section id="ai-assistant-page" class="page-section">
            <h2 class="text-4xl font-bold text-white mb-8 border-b border-gray-700 pb-4">Barnaby - AI Luthier</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="md:col-span-2 bg-dark-card p-6 rounded-xl border border-vintage-gold shadow-2xl flex flex-col h-[500px]">
                    <div id="chat-history" class="flex-grow bg-black/30 rounded border border-gray-700 p-4 overflow-y-auto flex flex-col gap-2 mb-4 custom-scrollbar">
                        <div class="chat-bubble chat-ai">Hello! I'm Barnaby. Ask me about guitar wiring, wood types, or vintage history.</div>
                    </div>
                    <div class="flex gap-2">
                        <input type="text" id="genkit-input" class="bg-gray-800 border border-gray-600 text-white p-3 rounded flex-grow focus:border-vintage-gold focus:outline-none" placeholder="Type your question...">
                        <button onclick="callGenkitLuthier()" class="btn-primary px-4 rounded font-bold"><i class="fas fa-paper-plane"></i></button>
                    </div>
                </div>
                <div class="md:col-span-1 bg-dark-card p-6 rounded-xl border border-forest-green shadow-2xl h-fit">
                    <h3 class="text-2xl font-bold text-forest-green mb-4">Capabilities</h3>
                    <ul class="list-disc list-inside text-gray-400 space-y-2 mb-4">
                        <li>Identify wood types.</li>
                        <li>Suggest wiring modifications.</li>
                        <li>Explain vintage history.</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Contact -->
        <section id="contact-page" class="page-section">
            <h2 class="text-4xl font-bold text-white mb-8 border-b border-gray-700 pb-4">Contact</h2>
            <div class="bg-dark-card p-8 rounded-xl shadow-lg max-w-2xl mx-auto text-center border border-gray-700">
                <p class="text-2xl mb-6 text-white"><i class="fas fa-envelope text-vintage-gold mr-2"></i> oldtimevibes1@gmail.com</p>
                <p class="text-2xl mb-8 text-white"><i class="fas fa-phone text-vintage-gold mr-2"></i> (580) 485-9474</p>
                <div class="border-t border-gray-600 pt-6">
                    <p class="text-vintage-gold font-bold text-lg">Old-Time Vibes LLC</p>
                    <p class="text-gray-400 italic">McCord, Oklahoma</p>
                </div>
            </div>
        </section>

        <!-- Parental Controls -->
        <section id="parental-controls-page" class="page-section">
            <div class="max-w-4xl mx-auto parental-control-form p-8 rounded-xl shadow-2xl mt-8">
                <h2 class="text-4xl font-bold text-white mb-8 text-center border-b border-gray-600 pb-4">Parental Controls</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="control-item p-6 rounded-xl">
                        <h3 class="text-2xl font-bold text-vintage-gold mb-4 flex items-center">
                            <i class="fas fa-user-shield mr-2"></i> Content Filtering
                        </h3>
                        <div class="space-y-4">
                            <div class="flex justify-between items-center">
                                <span>Music Library Access</span>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="music-access" checked>
                                    <span class="slider-switch"></span>
                                </label>
                            </div>
                            <div class="flex justify-between items-center">
                                <span>Video Content</span>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="video-content">
                                    <span class="slider-switch"></span>
                                </label>
                            </div>
                        </div>
                    </div>
                    
                    <div class="control-item p-6 rounded-xl">
                        <h3 class="text-2xl font-bold text-forest-green mb-4 flex items-center">
                            <i class="fas fa-clock mr-2"></i> Time Restrictions
                        </h3>
                        <div class="space-y-4">
                            <div>
                                <label class="block text-gray-400 mb-2">Maximum Daily Usage (hours)</label>
                                <input type="range" id="usage-range" min="0" max="24" value="12" class="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer">
                                <div class="flex justify-between text-sm text-gray-400 mt-1">
                                    <span>0</span>
                                    <span id="usage-value">12</span>
                                    <span>24</span>
                                </div>
                            </div>
                            
                            <div>
                                <label class="block text-gray-400 mb-2">Allowed Hours</label>
                                <div class="grid grid-cols-4 gap-2" id="day-buttons">
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Mon</button>
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Tue</button>
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Wed</button>
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Thu</button>
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Fri</button>
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Sat</button>
                                    <button type="button" class="day-btn bg-gray-800 text-white py-2 rounded transition">Sun</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-8 control-item p-6 rounded-xl">
                    <h3 class="text-2xl font-bold text-purple-400 mb-4 flex items-center">
                        <i class="fas fa-lock mr-2"></i> Password Protection
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-gray-400 mb-2">New Password</label>
                            <input type="password" id="parent-pass" class="w-full p-3 rounded bg-gray-900 border border-gray-600 text-white" placeholder="Create password">
                        </div>
                        <div>
                            <label class="block text-gray-400 mb-2">Confirm Password</label>
                            <input type="password" id="parent-pass-confirm" class="w-full p-3 rounded bg-gray-900 border border-gray-600 text-white" placeholder="Confirm password">
                        </div>
                    </div>
                    
                    <div class="mt-6 flex flex-col sm:flex-row justify-between items-center gap-4">
                        <p id="parental-status" class="text-sm font-medium"></p>
                        <button onclick="saveParentalSettings()" class="bg-vintage-gold hover:bg-white text-dark-bg font-bold py-3 px-8 rounded-lg shadow-lg transition">
                            Save Settings
                        </button>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Cart Modal -->
    <div id="cart-modal" class="fixed inset-0 z-50 hidden items-center justify-center p-4 bg-black/80 backdrop-blur-sm">
        <div class="bg-white rounded-xl w-full max-w-md p-6 shadow-2xl relative text-left border border-gray-200">
            <div class="flex justify-between items-center border-b pb-4 mb-4">
                <h2 class="text-2xl font-bold text-dark-bg">Your Cart</h2>
                <button onclick="toggleCart()" class="text-gray-500 hover:text-red-500 font-bold text-2xl transition">&times;</button>
            </div>
            <div id="cart-items-container" class="space-y-4 max-h-64 overflow-y-auto mb-4 text-black custom-scrollbar"></div>
            <div class="border-t pt-4 bg-gray-50 -mx-6 px-6 -mb-6 pb-6 rounded-b-xl">
                <div class="flex justify-between text-xl font-bold text-dark-bg mb-4">
                    <span>Total:</span> <span id="cart-total">$0.00</span>
                </div>
                <button onclick="window.location.href='https://buy.stripe.com/28E14oaGv8Sn2ow8M29Ve0o'" class="bg-vintage-gold hover:bg-gray-800 hover:text-white w-full font-bold py-3 rounded-lg text-dark-bg shadow-md transition">
                    Checkout with Stripe
                </button>
            </div>
        </div>
    </div>

    <footer class="bg-black text-center p-6 text-sm text-gray-500 border-t border-gray-800">
        &copy; 2026 Old-Time Vibes LLC. All rights reserved.
    </footer>

    <script>
        const stripePublicKey = "pk_live_51SX2E1IBMzln5OyFhNDFITa7IzBbg2KTXfGv8GQsaxXIQ7gXjKX4b7I2AdESOh0E6rk4btLdpGhYPNSo60A1LZdN00WvjfTKoM";
        let cart = [];
        let isAdmin = false;
        let products = [
            { id: 1, name: "Ernie Ball Slinky Strings", price: 7.99, category: "music", image: "https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763835000076.jpg" },
            { id: 2, name: "Snark Clip-on Tuner", price: 19.99, category: "music", image: "https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763833120649.jpg" },
            { id: 3, name: "Boss SD-1 Overdrive", price: 64.99, category: "music", image: "https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763831585495.jpg" },
            { id: 4, name: "Vintage Acoustic 1970", price: 450.00, category: "music", stripeBuyId: "buy_btn_1SZZVkIBMzln5OyFQRCqV3vc", image: "https://uploads.onecompiler.io/444vq9uft/445yt2ydr/1763833868666.jpg" }
        ];

        function showPage(pageId) {
            document.querySelectorAll('.page-section').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            
            let targetId = pageId + '-page';
            const target = document.getElementById(targetId);
            if(target) target.classList.add('active');
            
            const activeLink = document.getElementById('nav-' + pageId) || document.querySelector(`.nav-link[onclick*="${pageId}"]`);
            if(activeLink) activeLink.classList.add('active');
            if(pageId === 'shop') renderInventory();
            document.getElementById('cart-modal').style.display = 'none';
        }

        function renderInventory() {
            const storeGrid = document.getElementById('store-grid');
            if(storeGrid) {
                storeGrid.innerHTML = products.map(item => `
                    <div class="bg-dark-card rounded-lg p-4 shadow-lg relative group border border-transparent hover:border-vintage-gold transition h-full flex flex-col">
                        <div class="h-48 w-full bg-gray-800 rounded mb-4 overflow-hidden relative">
                            <img src="${item.image}" class="w-full h-full object-cover group-hover:scale-110 transition duration-500">
                        </div>
                        <h3 class="text-white font-bold text-lg leading-tight flex-grow">${item.name}</h3>
                        <p class="text-vintage-gold font-bold text-xl mt-2">$${item.price.toFixed(2)}</p>
                        <button onclick="addToCart('${item.name}', ${item.price})" class="mt-4 w-full bg-gray-700 text-white font-bold py-2 rounded hover:bg-vintage-gold hover:text-dark-bg transition">Add to Cart</button>
                    </div>
                `).join('');
            }
        }

        function addToCart(name, price) {
            cart.push({name, price});
            updateCart();
            document.getElementById('cart-modal').style.display = 'flex';
        }

        function updateCart() {
            document.getElementById('cart-count').innerText = cart.length;
            document.getElementById('cart-count-mobile').innerText = cart.length;
            const container = document.getElementById('cart-items-container');
            if(cart.length === 0) {
                container.innerHTML = '<p class="text-gray-500 italic text-center py-4">Your cart is empty.</p>';
                document.getElementById('cart-total').innerText = '$0.00';
            } else {
                let total = 0;
                container.innerHTML = cart.map(i => {
                    total += i.price;
                    return `<div class="flex justify-between border-b border-gray-200 py-2"><span class="medium">${i.name}</span><span>$${i.price.toFixed(2)}</span></div>`;
                }).join('');
                document.getElementById('cart-total').innerText = '$' + total.toFixed(2);
            }
        }

        function toggleCart() {
            const m = document.getElementById('cart-modal');
            m.style.display = (m.style.display === 'flex') ? 'none' : 'flex';
        }

        function checkAdmin() {
            if(document.getElementById('admin-pass').value === 'The1One.Sb') {
                isAdmin = true;
                document.getElementById('admin-login').classList.add('hidden');
                document.getElementById('admin-panel-content').classList.remove('hidden');
            } else {
                document.getElementById('login-error').classList.remove('hidden');
            }
        }

        let audioPlaylist = [
            { name: "Vintage Blues - Track 1", url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" }
        ];
        const player = document.getElementById('audio-player');
        if(player && audioPlaylist.length > 0) {
            player.src = audioPlaylist[0].url;
            document.getElementById('current-track-name').innerText = audioPlaylist[0].name;
        }

        async function callGenkitLuthier() {
            const input = document.getElementById('genkit-input');
            const history = document.getElementById('chat-history');
            const question = input.value.trim();
            if(!question) return;
            history.innerHTML += `<div class="chat-bubble chat-user">${question}</div>`;
            input.value = '';
            
            try {
                const luthierFlow = firebase.functions().httpsCallable('luthierFlow');
                const result = await luthierFlow({ prompt: question });
                const aiResponse = result.data.text || "I'm tuning up right now, ask again later.";
                history.innerHTML += `<div class="chat-bubble chat-ai">${aiResponse}</div>`;
            } catch (error) {
                history.innerHTML += `<div class="chat-bubble chat-ai" style="color:#f87171;">Backend Note: Ensure Firebase Functions are deployed for full AI responses.</div>`;
            }
            history.scrollTop = history.scrollHeight;
        }

        // Parental Controls Interactive Listeners
        document.getElementById('usage-range').addEventListener('input', (e) => {
            document.getElementById('usage-value').innerText = e.target.value;
        });

        document.querySelectorAll('.day-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                btn.classList.toggle('bg-vintage-gold');
                btn.classList.toggle('text-dark-bg');
                btn.classList.toggle('bg-gray-800');
                btn.classList.toggle('text-white');
                btn.classList.toggle('font-bold');
            });
        });

        function saveParentalSettings() {
            const p1 = document.getElementById('parent-pass').value;
            const p2 = document.getElementById('parent-pass-confirm').value;
            const status = document.getElementById('parental-status');

            if(p1 && p1 !== p2) {
                status.className = "text-sm font-medium text-red-400";
                status.innerText = "Passwords do not match!";
                return;
            }

            status.className = "text-sm font-medium text-green-400";
            status.innerText = "Settings saved successfully!";
            localStorage.setItem('parental_controls_saved', 'true');
        }

        document.addEventListener('DOMContentLoaded', () => {
            showPage('home');
            let lastScroll = 0;
            window.addEventListener('scroll', () => {
                const current = window.scrollY;
                const header = document.getElementById('main-header');
                if(current > lastScroll && current > 50) header.classList.add('header-hidden');
                else header.classList.remove('header-hidden');
                lastScroll = current;
            });
        });
    </script>
</body>
</html>+-----------------------------------------------------------------------------------+
|                                  Clients                                          |
|                     ADK Web UI (Browser)  |  HTTP Callers                         |
+------------------------------------------+----------------------------------------+
                                           | (HTTP / Web UI)
                                           v
+-----------------------------------------------------------------------------------+
| travel_agent (Port 8082 / Cloud Run)                                              |
| - Orchestrating ADK Agent serving the ADK Web UI                                  |
|                                                                                   |
|   +--> [Local AgentTool] weather_agent (travel_agent/subagents/)                  |
|        - Directly wrapped as AgentTool (no A2A network overhead)                  |
|        - Live weather tool via wttr.in API with fallback                          |
|   +--> [Remote AgentTool] currency_agent                                          |
|        - Communicates over A2A protocol                                           |
+------------------------------------------+----------------------------------------+
                                           | (A2A Protocol / JSON-RPC)
                                           v
+-----------------------------------------------------------------------------------+
| currency_agent (Port 8081 / Cloud Run)                                            |
| - Specialized ADK Agent exposed via A2A                                           |
| - Consumes get_exchange_rate tool via MCP Streamable HTTP client                  |
+------------------------------------------+----------------------------------------+
                                           | (MCP Streamable HTTP /mcp)
                                           v
+-----------------------------------------------------------------------------------+
| currency_mcp_server (Port 8080 / Cloud Run)                                       |
| - MCP server providing real-time exchange rates via Frankfurter API               |
+-----------------------------------------------------------------------------------+https://idotvdashboard.oneapp.dev/callback](https://idotvdashboard.oneapp.dev/callbackhttps://github.com/CypherpunkArmory/UserLAnd.wiki.gitpkg update && pkg install openssh -y
glpat-_8-brH0bJhDFE3VQgO7a3mM6MQpvOjEKdTprb2J0cQ8.01.171qc8o7tssh-keygen -t ed25519 -C "your-gitlab-email@example.com"
otv-memory-bank/
├── README.md                 # Bootloader index: instructs agents which files to load first
├── context/
│   ├── core-identity.md      # Old-Time Vibes LLC charter, zero-cloud constraints, tech stack
│   ├── active-sprint.md      # Current priorities, blockers, and immediate next actions
│   └── decision-log.md       # Append-only chronological record of architectural decisions
├── projects/
│   ├── project-barnaby.md    # ESP32-S3 specs, local voice orchestration, COPPA/FERPA rules
│   ├── r2io-moonwalker.md    # 6061-T6 chassis specs, rib-cage battery layout, joint kinematics
│   ├── beast-tv.md           # RK3588 SoM dual-chip architecture & OS specs
│   └── genxnext-store.md     # Express/SQLite storefront, Stripe UCP, Cloudflare Tunnel routes
└── schemas/
    └── context-packet.json   # Canonical JSON schema for MCP tool responses
---
project: Project Barnaby
owner: Stanley Joseph Brown (Old-Time Vibes LLC)
status: Prototyping / RFQ Stage
last_updated: 2026-11-18
---

## Hardware & Edge Constraints
- **MCU:** ESP32-S3 (local wake-word & inference, zero cloud telemetry)
- **Compliance:** Strict COPPA and FERPA isolation; no external analytics

## Settled Decisions
- Capsule housing finalized for plush integration; bulk silicon RFQs issued.

## Open Next Steps
- Complete firmware power-profile test on battery pack.
# Old-Time Vibes LLC — Shared Agent Memory Bank

## Boot Protocol (Mandatory for All Agents)
1. Read `context/core-identity.md` and `context/active-sprint.md` before answering.
2. Load only the specific file in `projects/` matching the active task.
3. Never generate placeholders or cloud-dependent external telemetry defaults.

## Write-Back Protocol
When an architectural decision, hardware revision, or deployment state changes:
1. Append a dated entry to `context/decision-log.md`.
2. Update the status header in the relevant `projects/*.md` file.
# Adding a theme to your GitHub Pages site using Jekyll

You can personalize your Jekyll site by adding and customizing a theme.

> [!NOTE] While the `github-pages` gem remains supported for some workflows, GitHub Actions is now the recommended approach for deploying and automating GitHub Pages sites.

People with write permissions for a repository can add a theme to a GitHub Pages site using Jekyll.

If you are publishing from a branch, changes to your site are published automatically when the changes are merged into your site's publishing source. If you are publishing from a custom GitHub Actions workflow, changes are published whenever your workflow is triggered (typically by a push to the default branch). If you want to preview your changes first, you can make the changes locally instead of on GitHub. Then, test your site locally. For more information, see [Testing your GitHub Pages site locally with Jekyll](/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).

## Supported themes

Out of the box, the following themes are supported:

* [Architect](https://github.com/pages-themes/architect)
* [Cayman](https://github.com/pages-themes/cayman)
* [Dinky](https://github.com/pages-themes/dinky)
* [Hacker](https://github.com/pages-themes/hacker)
* [Leap day](https://github.com/pages-themes/leap-day)
* [Merlot](https://github.com/pages-themes/merlot)
* [Midnight](https://github.com/pages-themes/midnight)
* [Minima](https://github.com/jekyll/minima)
* [Minimal](https://github.com/pages-themes/minimal)
* [Modernist](https://github.com/pages-themes/modernist)
* [Slate](https://github.com/pages-themes/slate)
* [Tactile](https://github.com/pages-themes/tactile)
* [Time machine](https://github.com/pages-themes/time-machine)

The [`jekyll-remote-theme`](https://github.com/benbalter/jekyll-remote-theme) Jekyll plugin is also available and lets you load other themes.

## Adding a theme

1. On GitHub, navigate to your site's repository.

2. Navigate to the publishing source for your site. For more information, see [Configuring a publishing source for your GitHub Pages site](/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

3. Navigate to `_config.yml`.

4. In the upper right corner of the file view, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-pencil" aria-label="Edit file" role="img"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg> to open the file editor.
   ![Screenshot of a file. In the header, a button, labeled with a pencil icon, is outlined in dark orange.](/assets/images/help/repository/edit-file-edit-button.png)

   > [!NOTE]
   > Instead of editing and committing the file using the default file editor, you can optionally choose to use the [github.dev code editor](/en/codespaces/the-githubdev-web-based-editor) by selecting the <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-triangle-down" aria-label="More edit options" role="img"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg> dropdown menu and clicking **github.dev**. You can also clone the repository and edit the file locally via GitHub Desktop by clicking **GitHub Desktop**.
   >
   > ![Screenshot of a file. In the header, a downwards-facing triangle icon is outlined in dark orange.](/assets/images/help/repository/edit-file-edit-dropdown.png)

5. Add a new line to the file for the theme name.
   * To use a supported theme, type `theme: THEME-NAME`, replacing THEME-NAME with the name of the theme as shown in the `_config.yml` of the theme's repository (most themes follow a `jekyll-theme-NAME` naming convention). For a list of supported themes, see [Supported themes](/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#supported-themes) on the GitHub Pages site. For example, to select the Minimal theme, type `theme: jekyll-theme-minimal`.
   * To use any other Jekyll theme hosted on GitHub, type `remote_theme: THEME-NAME`, replacing THEME-NAME with the name of the theme as shown in the README of the theme's repository.

6. Click **Commit changes...**

7. In the "Commit message" field, type a short, meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message. For more information, see [Creating a commit with multiple authors or on behalf of an organization](/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors).

8. If you have more than one email address associated with your account on GitHub, click the email address drop-down menu and select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then a no-reply will be the default commit author email address. For more information about the exact form the no-reply email address can take, see [Setting your commit email address](/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

   ![Screenshot of a GitHub pull request showing a dropdown menu with options to choose the commit author email address. octocat@github.com is selected.](/assets/images/help/repository/choose-commit-email-address.png)

9. Below the commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit and then create a pull request. For more information, see [Creating a pull request](/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).

   ![Screenshot of a GitHub pull request showing a radio button to commit directly to the main branch or to create a new branch. New branch is selected.](/assets/images/help/repository/choose-commit-branch.png)

10. Click **Commit changes** or **Propose changes**.

## Customizing your theme's CSS

These instructions work best with themes that are officially supported by GitHub Pages. For a complete list of supported themes, see [Supported themes](/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#supported-themes) on the GitHub Pages site.

Your theme's source repository may offer some help in customizing your theme. For example, see [Minimal's README](https://github.com/pages-themes/minimal#customizing).

1. On GitHub, navigate to your site's repository.

2. Navigate to the publishing source for your site. For more information, see [Configuring a publishing source for your GitHub Pages site](/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

3. Create a new file called `/assets/css/style.scss`.

4. Add the following content to the top of the file:

   ```scss
   ---
   ---

   @import "{{ site.theme }}";
   ```

5. Add any custom CSS or Sass (including imports) you'd like immediately after the `@import` line.

## Customizing your theme's HTML layout

These instructions work best with themes that are officially supported by GitHub Pages. For a complete list of supported themes, see [Supported themes](/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#supported-themes) on the GitHub Pages site.

Your theme's source repository may offer some help in customizing your theme. For example, see [Minimal's README](https://github.com/pages-themes/minimal#customizing).

1. On GitHub, navigate to your theme's source repository. For example, the source repository for Minimal is `https://github.com/pages-themes/minimal`.
2. In the `_layouts` folder, navigate to your theme's `_default.html` file.
3. Copy the contents of the file.
4. On GitHub, navigate to your site's repository.
5. Navigate to the publishing source for your site. For more information, see [Configuring a publishing source for your GitHub Pages site](/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
6. Create a file called `_layouts/default.html`.brew install --cask copilot-cli

7. Paste the default layout content you copied earlier.
8. Customize the layout as you'd like.

## Further reading

* [Creating new files](/en/repositories/working-with-files/managing-files/creating-new-files)npm install -g @github/copilot
winget install GitHub.Copilot
brew install --cask copilot-cli
