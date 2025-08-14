# Create the complete HTML file for the TNP Platform
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TNP Platform - Advanced Training & Placement Portal</title>
    <meta name="description" content="Advanced Training & Placement Portal with AI-powered features">
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎓</text></svg>">
</head>
<body>
    <!-- Welcome Screen -->
    <div id="welcome-screen" class="welcome-container">
        <div class="welcome-content">
            <div class="welcome-hero">
                <h1>🎓 TNP Platform</h1>
                <p class="welcome-subtitle">Advanced Training & Placement Portal</p>
                <div class="welcome-features">
                    <div class="feature-item">🎯 Smart Job Matching</div>
                    <div class="feature-item">💻 Interactive Coding</div>
                    <div class="feature-item">🎤 Mock Interviews</div>
                    <div class="feature-item">📚 Personalized Learning</div>
                </div>
                <button id="get-started-btn" class="btn btn--primary btn--lg">Get Started</button>
                <div class="demo-info">
                    <p>Demo Login: student@college.edu / password123</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Role Selection -->
    <div id="role-selection" class="role-container hidden">
        <div class="role-content">
            <h2>Choose Your Role</h2>
            <div class="role-grid">
                <div class="role-card" data-role="student">
                    <div class="role-icon">🎓</div>
                    <h3>Student</h3>
                    <p>Access learning resources, apply for jobs, practice coding</p>
                </div>
                <div class="role-card" data-role="faculty">
                    <div class="role-icon">👨‍🏫</div>
                    <h3>Faculty</h3>
                    <p>Monitor student progress, manage courses, provide guidance</p>
                </div>
                <div class="role-card" data-role="company">
                    <div class="role-icon">🏢</div>
                    <h3>Company HR</h3>
                    <p>Find talented candidates, manage recruitment process</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Login/Registration -->
    <div id="auth-section" class="auth-container hidden">
        <div class="auth-card">
            <h2>Login to TNP Platform</h2>
            <div class="auth-tabs">
                <button id="login-tab" class="auth-tab active">Login</button>
                <button id="register-tab" class="auth-tab">Register</button>
            </div>
            
            <!-- Login Form -->
            <form id="login-form" class="auth-form">
                <div class="form-group">
                    <label class="form-label">Email</label>
                    <input type="email" id="login-email" class="form-control" value="student@college.edu" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Password</label>
                    <input type="password" id="login-password" class="form-control" value="password123" required>
                </div>
                <button type="submit" class="btn btn--primary btn--full-width">Login</button>
            </form>
            
            <!-- Registration Form -->
            <form id="register-form" class="auth-form hidden">
                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label">Full Name</label>
                        <input type="text" id="reg-name" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Email</label>
                        <input type="email" id="reg-email" class="form-control" required>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label">Roll Number</label>
                        <input type="text" id="reg-roll" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Department</label>
                        <select id="reg-dept" class="form-control" required>
                            <option value="">Select Department</option>
                            <option value="Computer Science">Computer Science</option>
                            <option value="Information Technology">Information Technology</option>
                            <option value="Electronics">Electronics</option>
                            <option value="Mechanical">Mechanical</option>
                        </select>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label">Year</label>
                        <select id="reg-year" class="form-control" required>
                            <option value="">Select Year</option>
                            <option value="1">1st Year</option>
                            <option value="2">2nd Year</option>
                            <option value="3">3rd Year</option>
                            <option value="4">4th Year</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Phone</label>
                        <input type="tel" id="reg-phone" class="form-control" required>
                    </div>
                </div>
                <div class="form-group">
                    <label class="form-label">Password</label>
                    <input type="password" id="reg-password" class="form-control" required>
                </div>
                <button type="submit" class="btn btn--primary btn--full-width">Register</button>
            </form>
        </div>
    </div>

    <!-- Main Application -->
    <div id="main-app" class="main-container hidden">
        <!-- Header -->
        <header class="app-header">
            <div class="header-left">
                <h1 class="app-title">🎓 TNP Platform</h1>
                <div class="breadcrumb">
                    <span id="current-page">Dashboard</span>
                </div>
            </div>
            <div class="header-right">
                <button id="theme-toggle" class="btn btn--icon">🌙</button>
                <div class="user-info">
                    <div class="user-stats">
                        <span class="points">🏆 <span id="user-points">0</span></span>
                        <span class="level">⭐ Level <span id="user-level">1</span></span>
                        <span class="streak">🔥 <span id="user-streak">0</span></span>
                    </div>
                    <div class="user-profile">
                        <img id="user-avatar" src="https://randomuser.me/api/portraits/men/1.jpg" alt="Profile">
                        <span id="user-name">Student</span>
                        <button id="logout-btn" class="btn btn--secondary btn--sm">Logout</button>
                    </div>
                </div>
            </div>
        </header>

        <!-- Sidebar -->
        <aside class="sidebar">
            <nav class="sidebar-nav">
                <a href="#" class="nav-item active" data-page="dashboard">
                    <span class="nav-icon">📊</span>
                    <span class="nav-text">Dashboard</span>
                </a>
                <a href="#" class="nav-item" data-page="resume">
                    <span class="nav-icon">📄</span>
                    <span class="nav-text">Resume</span>
                </a>
                <a href="#" class="nav-item" data-page="jobs">
                    <span class="nav-icon">💼</span>
                    <span class="nav-text">Jobs</span>
                </a>
                <a href="#" class="nav-item" data-page="challenges">
                    <span class="nav-icon">🎯</span>
                    <span class="nav-text">Challenges</span>
                </a>
                <a href="#" class="nav-item" data-page="courses">
                    <span class="nav-icon">📚</span>
                    <span class="nav-text">Courses</span>
                </a>
                <a href="#" class="nav-item" data-page="interview">
                    <span class="nav-icon">🎤</span>
                    <span class="nav-text">Mock Interview</span>
                </a>
                <a href="#" class="nav-item" data-page="profile">
                    <span class="nav-icon">👤</span>
                    <span class="nav-text">Profile</span>
                </a>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Dashboard Page -->
            <div id="dashboard-page" class="page active">
                <div class="page-header">
                    <h2>Dashboard</h2>
                    <p>Welcome back! Here's your progress overview.</p>
                </div>
                
                <!-- Stats Grid -->
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-icon">🎯</div>
                        <div class="stat-content">
                            <h3 id="challenges-completed">0</h3>
                            <p>Challenges Completed</p>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">📝</div>
                        <div class="stat-content">
                            <h3 id="applications-submitted">0</h3>
                            <p>Applications Submitted</p>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">🎤</div>
                        <div class="stat-content">
                            <h3 id="interviews-attended">0</h3>
                            <p>Interviews Attended</p>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">📚</div>
                        <div class="stat-content">
                            <h3 id="courses-completed">0</h3>
                            <p>Courses Completed</p>
                        </div>
                    </div>
                </div>

                <!-- Charts Section -->
                <div class="charts-section">
                    <div class="chart-card">
                        <h3>Progress Over Time</h3>
                        <canvas id="progressChart"></canvas>
                    </div>
                    <div class="chart-card">
                        <h3>Skills Distribution</h3>
                        <canvas id="skillsChart"></canvas>
                    </div>
                </div>

                <!-- Recent Activity -->
                <div class="activity-section">
                    <h3>Recent Activity</h3>
                    <div id="activity-list" class="activity-list">
                        <!-- Activity items will be populated by JavaScript -->
                    </div>
                </div>
            </div>

            <!-- Resume Page -->
            <div id="resume-page" class="page">
                <div class="page-header">
                    <h2>Resume Management</h2>
                    <p>Upload and analyze your resume for better job matching.</p>
                </div>
                
                <div class="resume-section">
                    <div class="upload-card">
                        <div class="upload-area" id="resume-upload">
                            <div class="upload-icon">📄</div>
                            <h3>Upload Resume</h3>
                            <p>Drag and drop your PDF resume or click to browse</p>
                            <input type="file" id="resume-file" accept=".pdf" hidden>
                            <button class="btn btn--primary" onclick="document.getElementById('resume-file').click()">
                                Choose File
                            </button>
                        </div>
                    </div>
                    
                    <div id="resume-analysis" class="analysis-card hidden">
                        <h3>Resume Analysis</h3>
                        <div class="analysis-score">
                            <div class="score-circle">
                                <span id="resume-score">0</span>%
                            </div>
                            <div class="score-details">
                                <h4>Overall Match Score</h4>
                                <p id="score-description">Upload a resume to see analysis</p>
                            </div>
                        </div>
                        
                        <div class="skills-analysis">
                            <div class="matched-skills">
                                <h4>✅ Matched Skills</h4>
                                <div id="matched-skills-list" class="skills-tags"></div>
                            </div>
                            <div class="missing-skills">
                                <h4>❌ Missing Skills</h4>
                                <div id="missing-skills-list" class="skills-tags"></div>
                            </div>
                        </div>
                        
                        <div class="suggestions">
                            <h4>💡 Improvement Suggestions</h4>
                            <ul id="suggestions-list"></ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Jobs Page -->
            <div id="jobs-page" class="page">
                <div class="page-header">
                    <h2>Job Search</h2>
                    <p>Find your dream job with AI-powered matching.</p>
                </div>
                
                <div class="search-section">
                    <div class="search-filters">
                        <input type="text" id="job-search" placeholder="Search jobs..." class="form-control">
                        <select id="location-filter" class="form-control">
                            <option value="">All Locations</option>
                            <option value="Bangalore">Bangalore</option>
                            <option value="Mumbai">Mumbai</option>
                            <option value="Hyderabad">Hyderabad</option>
                            <option value="Chennai">Chennai</option>
                        </select>
                        <select id="experience-filter" class="form-control">
                            <option value="">Any Experience</option>
                            <option value="0-1">0-1 years</option>
                            <option value="1-3">1-3 years</option>
                            <option value="3-5">3-5 years</option>
                        </select>
                        <button id="search-jobs" class="btn btn--primary">Search</button>
                    </div>
                </div>
                
                <div id="jobs-list" class="jobs-list">
                    <!-- Job listings will be populated by JavaScript -->
                </div>
            </div>

            <!-- Challenges Page -->
            <div id="challenges-page" class="page">
                <div class="page-header">
                    <h2>Coding Challenges</h2>
                    <p>Practice coding and earn points to level up!</p>
                </div>
                
                <div class="challenges-section">
                    <div class="challenge-filters">
                        <button class="filter-btn active" data-difficulty="all">All</button>
                        <button class="filter-btn" data-difficulty="Easy">Easy</button>
                        <button class="filter-btn" data-difficulty="Medium">Medium</button>
                        <button class="filter-btn" data-difficulty="Hard">Hard</button>
                    </div>
                    
                    <div id="challenges-list" class="challenges-list">
                        <!-- Challenges will be populated by JavaScript -->
                    </div>
                </div>
            </div>

            <!-- Challenge Solver -->
            <div id="challenge-solver" class="page">
                <div class="solver-header">
                    <button id="back-to-challenges" class="btn btn--secondary">← Back</button>
                    <h2 id="challenge-title">Challenge Title</h2>
                </div>
                
                <div class="solver-content">
                    <div class="problem-section">
                        <div id="problem-description" class="problem-description"></div>
                        <div id="problem-examples" class="problem-examples"></div>
                        <div id="problem-constraints" class="problem-constraints"></div>
                    </div>
                    
                    <div class="code-section">
                        <div class="code-header">
                            <select id="language-select" class="form-control">
                                <option value="javascript">JavaScript</option>
                                <option value="python">Python</option>
                                <option value="java">Java</option>
                                <option value="cpp">C++</option>
                            </select>
                            <button id="run-code" class="btn btn--secondary">Run Code</button>
                            <button id="submit-code" class="btn btn--primary">Submit</button>
                        </div>
                        <textarea id="code-editor" class="code-editor" placeholder="// Write your solution here..."></textarea>
                        <div id="code-output" class="code-output hidden"></div>
                    </div>
                </div>
            </div>

            <!-- Courses Page -->
            <div id="courses-page" class="page">
                <div class="page-header">
                    <h2>Course Recommendations</h2>
                    <p>Enhance your skills with personalized course suggestions.</p>
                </div>
                
                <div id="courses-list" class="courses-list">
                    <!-- Courses will be populated by JavaScript -->
                </div>
            </div>

            <!-- Interview Page -->
            <div id="interview-page" class="page">
                <div class="page-header">
                    <h2>Mock Interview</h2>
                    <p>Practice interviews with AI feedback and improve your skills.</p>
                </div>
                
                <div class="interview-section">
                    <div class="interview-setup">
                        <h3>Select Interview Type</h3>
                        <div class="interview-types">
                            <button class="interview-type" data-type="technical">
                                <span class="type-icon">💻</span>
                                <span class="type-name">Technical</span>
                            </button>
                            <button class="interview-type" data-type="behavioral">
                                <span class="type-icon">🧠</span>
                                <span class="type-name">Behavioral</span>
                            </button>
                            <button class="interview-type" data-type="hr">
                                <span class="type-icon">🤝</span>
                                <span class="type-name">HR Round</span>
                            </button>
                        </div>
                        <button id="start-interview" class="btn btn--primary btn--lg">Start Interview</button>
                    </div>
                    
                    <div id="interview-session" class="interview-session hidden">
                        <div class="interview-header">
                            <div class="timer">
                                <span>⏰</span>
                                <span id="interview-timer">00:00</span>
                            </div>
                            <button id="end-interview" class="btn btn--secondary">End Interview</button>
                        </div>
                        
                        <div class="interview-content">
                            <div class="question-section">
                                <h3>Question <span id="question-number">1</span> of <span id="total-questions">5</span></h3>
                                <div id="current-question" class="question-text"></div>
                            </div>
                            
                            <div class="response-section">
                                <textarea id="response-text" placeholder="Type your response here..." class="form-control"></textarea>
                                <div class="interview-controls">
                                    <button id="prev-question" class="btn btn--secondary">Previous</button>
                                    <button id="next-question" class="btn btn--primary">Next Question</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div id="interview-results" class="interview-results hidden">
                        <h3>Interview Feedback</h3>
                        <div class="feedback-section">
                            <!-- Feedback will be populated by JavaScript -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- Profile Page -->
            <div id="profile-page" class="page">
                <div class="page-header">
                    <h2>Profile</h2>
                    <p>Manage your profile and preferences.</p>
                </div>
                
                <div class="profile-section">
                    <div class="profile-card">
                        <div class="profile-header">
                            <img id="profile-avatar" src="https://randomuser.me/api/portraits/men/1.jpg" alt="Profile">
                            <div class="profile-info">
                                <h3 id="profile-name">Student Name</h3>
                                <p id="profile-email">student@college.edu</p>
                                <p id="profile-department">Computer Science</p>
                            </div>
                        </div>
                        
                        <div class="profile-stats">
                            <div class="stat">
                                <span class="stat-value" id="profile-points">0</span>
                                <span class="stat-label">Points</span>
                            </div>
                            <div class="stat">
                                <span class="stat-value" id="profile-level">1</span>
                                <span class="stat-label">Level</span>
                            </div>
                            <div class="stat">
                                <span class="stat-value" id="profile-streak">0</span>
                                <span class="stat-label">Streak</span>
                            </div>
                        </div>
                        
                        <div class="skills-section">
                            <h4>Skills</h4>
                            <div id="profile-skills" class="skills-tags"></div>
                        </div>
                        
                        <div class="achievements-section">
                            <h4>Achievements</h4>
                            <div id="profile-achievements" class="achievements-grid"></div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <!-- Notifications -->
    <div id="notifications" class="notifications-container"></div>

    <!-- Chat Bot -->
    <div id="chatbot" class="chatbot-container">
        <button id="chatbot-toggle" class="chatbot-toggle">💬</button>
        <div id="chatbot-window" class="chatbot-window hidden">
            <div class="chatbot-header">
                <h4>AI Assistant</h4>
                <button id="chatbot-close">×</button>
            </div>
            <div id="chatbot-messages" class="chatbot-messages"></div>
            <div class="chatbot-input">
                <input type="text" id="chatbot-input" placeholder="Ask me anything...">
                <button id="chatbot-send">Send</button>
            </div>
        </div>
    </div>

    <!-- Loading Overlay -->
    <div id="loading-overlay" class="loading-overlay hidden">
        <div class="spinner"></div>
        <p>Loading...</p>
    </div>

    <script src="app.js"></script>
</body>
</html>'''

# Save the HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Created complete HTML file (index.html)")
print(f"📄 File size: {len(html_content)} characters")