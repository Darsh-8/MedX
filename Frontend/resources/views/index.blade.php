<!DOCTYPE html>
<html lang="en" data-wf-domain="www.withcoherence.com" data-wf-page="6462990f476598b6fd0c9cd4" data-wf-site="6462990f476598b6fd0c9cd1">
    <head>
        <meta charset="utf-8"/>
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <title>MedAI</title>
        <link href="{{ asset('styles.css') }}" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com" rel="preconnect"/>
        <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="anonymous"/>
        <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
        <script type="text/javascript">
            WebFont.load({
                google: {
                    families: ["Inconsolata:400,700"]
                }
            });
        </script>
        <link href="https://cdn.prod.website-files.com/6462990f476598b6fd0c9cd1/65e61bf0c65e59df927db44b_logo256.png" rel="apple-touch-icon"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
    </head>
    <body class="body">
        <!-- Main Wrapper -->
        <div class="wrapper">
            <!-- Alert Banner -->
            <div class="alert_banner">
                <div class="container w-container">
                    <a href="#" target="_blank" class="link-block alert_link w-inline-block">
                        <div class="tag mr-1 banner">Innovation</div>
                        <div class="alter-text">Drag and drop your X-rays, MRIs, etc., and get the results in seconds</div>
                    </a>
                </div>
                <div class="black-divider-small"></div>
            </div>
            
            <!-- Navigation -->
            <div class="navigation conversion">
                <div class="container container__nav w-container">
                    <div class="navbar w-nav">
                        <div class="logo_wrapper">
                            <a href="/" class="brand w-nav-brand">
                                <img src="https://cdn.prod.website-files.com/6462990f476598b6fd0c9cd1/66ce22ac9ddb66ca0b9bcf43_logo_dark.svg" alt="MedAI Logo" class="image"/>
                                <img src="https://cdn.prod.website-files.com/6462990f476598b6fd0c9cd1/66d0c06a70298ddd4f307c17_20.svg" alt="MedAI Icon" class="image-37"/>
                            </a>
                        </div>
                        <!-- Add navigation links here if you have them -->
                    </div>
                </div>
            </div>
            
            <!-- Hero Section -->
            <div class="section hero-section">
                <div class="container w-container">
                    <div class="eyebrow-promo">
                        <div class="eyebrow-inner">
                            <div>Powered by</div>
                            <a href="https://cncframework.com/" class="eyebrow-icon w-inline-block">
                                <img src="https://cdn.prod.website-files.com/6462990f476598b6fd0c9cd1/665dcf92bb2e05ed64281d22_cnc_white.svg" alt="CNC Framework"/>
                            </a>
                        </div>
                    </div>
                    <h1 class="heading usp_header usp_non-mobile">
                        Medical Analysis<br/>
                        <span class="purple-accent">Made Easy</span>
                    </h1>
                    
                    <!-- USP Container -->
                    <div class="usp-container">
                        <!-- Navigation Buttons -->
                        <div class="nav-buttons">
                            <select class="dropdown-button" onchange="location = this.value;">
                                <option value="" disabled selected>Choose Disease</option>
                                <option value="/disease1">Disease 1</option>
                                <option value="/disease2">Disease 2</option>
                                <option value="/disease3">Disease 3</option>
                                <!-- Add more options as needed -->
                            </select>
                        </div>
                        <!-- File Upload Area -->
                        <div class="upload-area" id="uploadArea" onclick="fileInput.click();">
                            <p>Drag and drop your X-ray image here or click to upload</p>
                        </div>
                        <input type="file" id="fileInput" accept="image/*" style="display: none;">
                        
                        <!-- Progress Bar -->
                        <div class="progress-container" style="display: none;">
                            <div class="progress-bar" id="progressBar" style="width: 0%;"></div>
                        </div>
                        
                        <!-- Output Area -->
                        <div class="output-area">
                            <h2>Output:</h2>
                            <div class="output" id="outputTextBox">Results will be displayed here...</div>
                            <!-- Submit Button -->
                            <button class="button" id="submitButton">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Chatbot Widget -->
        <!-- BotMan Widget Styles -->
        <style>
            /* BotMan Widget Button */
            .botman-button {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: #5C6BC0;
                color: white;
                border: none;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                cursor: pointer;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                z-index: 1000;
                font-size: 24px;
            }
        
            /* BotMan Widget Chat Window */
            .botman-chat-container {
                position: fixed;
                bottom: 90px;
                right: 20px;
                width: 350px;
                max-height: 500px;
                background: white;
                border: 1px solid #ddd;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                display: none;
                flex-direction: column;
                z-index: 1000;
                overflow: hidden;
            }
        
            .botman-header {
                background-color: #5C6BC0;
                color: white;
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
        
            .botman-messages {
                padding: 10px;
                overflow-y: auto;
                flex-grow: 1;
            }
        
            .botman-input {
                padding: 10px;
                border-top: 1px solid #ddd;
            }
        
            .botman-input input {
                width: 100%;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        
            .close-button {
                background: transparent;
                border: none;
                color: white;
                font-size: 20px;
                cursor: pointer;
            }
        
            /* Styles for messages */
            .bot-message {
                background-color: #e0e0e0;
                padding: 10px;
                margin: 5px 0;
                border-radius: 10px;
                align-self: flex-start;
                max-width: 80%;
            }
        
            .user-message {
                background-color: #5C6BC0;
                color: white;
                padding: 10px;
                margin: 5px 0;
                border-radius: 10px;
                align-self: flex-end;
                max-width: 80%;
            }
        
            .botman-messages {
                display: flex;
                flex-direction: column;
            }

            /* Chatbot Responsiveness */
            @media (max-width: 600px) {
                .botman-chat-container {
                    width: 90%;
                    right: 5%;
                }
            }
        </style>
        
        <!-- BotMan Widget HTML -->
        <button class="botman-button" id="botmanButton">💬</button>
        
        <div class="botman-chat-container" id="botmanChat">
            <div class="botman-header">
                <span>MedAI Chatbot</span>
                <button class="close-button" id="closeChat">&times;</button>
            </div>
            <div class="botman-messages" id="botmanMessages">
                <!-- Messages will appear here -->
            </div>
            <div class="botman-input">
                <input type="text" id="botmanInput" placeholder="Type your message..." />
            </div>
        </div>
        
        <!-- Axios for AJAX requests -->
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        
        <script>
            // Axios set to include the CSRF token in the headers
            axios.defaults.headers.common['X-CSRF-TOKEN'] = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        </script>
        
        <!-- Chatbot Functionality -->
        <script>
            const botmanButton = document.getElementById('botmanButton');
            const botmanChat = document.getElementById('botmanChat');
            const closeChat = document.getElementById('closeChat');
            const botmanInput = document.getElementById('botmanInput');
            const botmanMessages = document.getElementById('botmanMessages');
        
            // Toggle Chat Window
            botmanButton.addEventListener('click', () => {
                botmanChat.style.display = botmanChat.style.display === 'flex' ? 'none' : 'flex';
            });
        
            closeChat.addEventListener('click', () => {
                botmanChat.style.display = 'none';
            });
        
            // Function to append messages
            function appendMessage(message, sender = 'bot') {
                const messageDiv = document.createElement('div');
                messageDiv.classList.add(sender === 'bot' ? 'bot-message' : 'user-message');
                messageDiv.textContent = message;
                botmanMessages.appendChild(messageDiv);
                botmanMessages.scrollTop = botmanMessages.scrollHeight;
            }
        
            // Handle user input
            botmanInput.addEventListener('keydown', function(event) {
                if (event.key === 'Enter' && botmanInput.value.trim() !== '') {
                    const userMessage = botmanInput.value.trim();
                    appendMessage(userMessage, 'user');
                    sendMessage(userMessage);
                    botmanInput.value = '';
                }
            });
        
            // Send message to backend
            function sendMessage(message) {
                axios.post('/botman', {
                    query: message
                })
                .then(response => {
                    if(response.data.answer){
                        const botReply = response.data.answer;
                        appendMessage(botReply, 'bot');
                    } else {
                        appendMessage("I'm sorry, something went wrong. Please try again later.", 'bot');
                    }
                })
                .catch(error => {
                    console.error('Error communicating with chatbot:', error);
                    appendMessage("Sorry, something went wrong. Please try again later.", 'bot');
                });
            }
        </script>
        <!-- script.js for additional functionality -->
        <script src="{{ asset('script.js') }}"></script>

        <!-- Footer Image -->
        <img src="https://cdn.prod.website-files.com/6462990f476598b6fd0c9cd1/66d083930e529a0e7a7e62d0_footergrad.png" alt="Footer Gradient" class="responsive-footer-image">
    </body>
</html>