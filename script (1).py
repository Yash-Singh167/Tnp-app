# Create the complete CSS file for the TNP Platform
css_content = '''/* TNP Platform - Complete Styles */

:root {
  /* Color Palette */
  --primary: #4F46E5;
  --primary-light: #6366F1;
  --primary-dark: #3730A3;
  --secondary: #06B6D4;
  --success: #10B981;
  --warning: #F59E0B;
  --danger: #EF4444;
  --info: #3B82F6;
  
  /* Neutral Colors */
  --white: #FFFFFF;
  --gray-50: #F9FAFB;
  --gray-100: #F3F4F6;
  --gray-200: #E5E7EB;
  --gray-300: #D1D5DB;
  --gray-400: #9CA3AF;
  --gray-500: #6B7280;
  --gray-600: #4B5563;
  --gray-700: #374151;
  --gray-800: #1F2937;
  --gray-900: #111827;
  
  /* Semantic Colors */
  --background: var(--gray-50);
  --surface: var(--white);
  --text-primary: var(--gray-900);
  --text-secondary: var(--gray-600);
  --border: var(--gray-200);
  --shadow: rgba(0, 0, 0, 0.1);
  
  /* Typography */
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: 'SF Mono', 'Monaco', 'Inconsolata', 'Roboto Mono', monospace;
  
  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  
  /* Border Radius */
  --radius-sm: 0.375rem;
  --radius: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* Dark theme variables */
[data-theme="dark"] {
  --background: var(--gray-900);
  --surface: var(--gray-800);
  --text-primary: var(--gray-100);
  --text-secondary: var(--gray-400);
  --border: var(--gray-700);
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-sans);
  background-color: var(--background);
  color: var(--text-primary);
  line-height: 1.6;
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* Utility Classes */
.hidden { display: none !important; }
.flex { display: flex; }
.grid { display: grid; }
.relative { position: relative; }
.absolute { position: absolute; }
.fixed { position: fixed; }
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }
.w-full { width: 100%; }
.h-full { height: 100%; }
.min-h-screen { min-height: 100vh; }

/* Welcome Screen */
.welcome-container {
  min-height: 100vh;
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
}

.welcome-content {
  text-align: center;
  color: white;
  max-width: 600px;
}

.welcome-hero h1 {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: var(--space-4);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.welcome-subtitle {
  font-size: 1.5rem;
  font-weight: 300;
  margin-bottom: var(--space-8);
  opacity: 0.9;
}

.welcome-features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-8);
}

.feature-item {
  background: rgba(255, 255, 255, 0.2);
  padding: var(--space-4);
  border-radius: var(--radius-lg);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  font-weight: 500;
}

.demo-info {
  margin-top: var(--space-6);
  opacity: 0.8;
  font-size: 0.9rem;
}

/* Role Selection */
.role-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
  background-color: var(--background);
}

.role-content {
  text-align: center;
  max-width: 800px;
  width: 100%;
}

.role-content h2 {
  font-size: 2.5rem;
  margin-bottom: var(--space-8);
  color: var(--text-primary);
}

.role-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.role-card {
  background: var(--surface);
  padding: var(--space-8);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.role-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
  border-color: var(--primary);
}

.role-icon {
  font-size: 3rem;
  margin-bottom: var(--space-4);
}

.role-card h3 {
  font-size: 1.5rem;
  margin-bottom: var(--space-2);
  color: var(--text-primary);
}

.role-card p {
  color: var(--text-secondary);
}

/* Authentication */
.auth-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
  background-color: var(--background);
}

.auth-card {
  background: var(--surface);
  padding: var(--space-8);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);
  width: 100%;
  max-width: 500px;
}

.auth-card h2 {
  text-align: center;
  margin-bottom: var(--space-6);
  color: var(--text-primary);
}

.auth-tabs {
  display: flex;
  margin-bottom: var(--space-6);
  background: var(--gray-100);
  border-radius: var(--radius);
  padding: var(--space-1);
}

.auth-tab {
  flex: 1;
  padding: var(--space-3);
  border: none;
  background: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
}

.auth-tab.active {
  background: var(--primary);
  color: white;
}

/* Forms */
.form-group {
  margin-bottom: var(--space-4);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

.form-label {
  display: block;
  margin-bottom: var(--space-2);
  font-weight: 500;
  color: var(--text-primary);
}

.form-control {
  width: 100%;
  padding: var(--space-3);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  font-size: 1rem;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  background: var(--surface);
  color: var(--text-primary);
}

.form-control:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-3) var(--space-6);
  border: none;
  border-radius: var(--radius);
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  gap: var(--space-2);
}

.btn--primary {
  background: var(--primary);
  color: white;
}

.btn--primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
}

.btn--secondary {
  background: var(--gray-200);
  color: var(--text-primary);
}

.btn--secondary:hover {
  background: var(--gray-300);
}

.btn--success {
  background: var(--success);
  color: white;
}

.btn--warning {
  background: var(--warning);
  color: white;
}

.btn--danger {
  background: var(--danger);
  color: white;
}

.btn--icon {
  padding: var(--space-2);
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.btn--sm {
  padding: var(--space-2) var(--space-4);
  font-size: 0.875rem;
}

.btn--lg {
  padding: var(--space-4) var(--space-8);
  font-size: 1.125rem;
}

.btn--full-width {
  width: 100%;
}

/* Main Application Layout */
.main-container {
  display: grid;
  grid-template-areas: 
    "header header"
    "sidebar content";
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
}

/* Header */
.app-header {
  grid-area: header;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: var(--space-4) var(--space-6);
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}

.header-left {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.app-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
}

.breadcrumb {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.header-right {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.user-info {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.user-stats {
  display: flex;
  gap: var(--space-3);
  font-size: 0.875rem;
  font-weight: 500;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.user-profile img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid var(--primary);
}

/* Sidebar */
.sidebar {
  grid-area: sidebar;
  background: var(--surface);
  border-right: 1px solid var(--border);
  padding: var(--space-6) 0;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-6);
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.2s ease;
  border-right: 3px solid transparent;
}

.nav-item:hover {
  background: var(--gray-100);
  color: var(--text-primary);
}

.nav-item.active {
  background: rgba(79, 70, 229, 0.1);
  color: var(--primary);
  border-right-color: var(--primary);
}

.nav-icon {
  font-size: 1.25rem;
}

/* Main Content */
.main-content {
  grid-area: content;
  padding: var(--space-6);
  overflow-y: auto;
}

.page {
  display: none;
}

.page.active {
  display: block;
}

.page-header {
  margin-bottom: var(--space-8);
}

.page-header h2 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: var(--space-2);
  color: var(--text-primary);
}

.page-header p {
  color: var(--text-secondary);
  font-size: 1.1rem;
}

/* Dashboard */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.stat-card {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  display: flex;
  align-items: center;
  gap: var(--space-4);
  transition: transform 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
}

.stat-icon {
  font-size: 2.5rem;
  background: rgba(79, 70, 229, 0.1);
  padding: var(--space-4);
  border-radius: var(--radius-lg);
}

.stat-content h3 {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--space-1);
}

.stat-content p {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

/* Charts */
.charts-section {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.chart-card {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.chart-card h3 {
  margin-bottom: var(--space-4);
  color: var(--text-primary);
}

/* Activity */
.activity-section {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.activity-section h3 {
  margin-bottom: var(--space-4);
  color: var(--text-primary);
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.activity-item {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-4);
  background: var(--gray-50);
  border-radius: var(--radius);
}

.activity-icon {
  font-size: 1.5rem;
  background: rgba(79, 70, 229, 0.1);
  padding: var(--space-2);
  border-radius: var(--radius);
}

.activity-content {
  flex: 1;
}

.activity-title {
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: var(--space-1);
}

.activity-time {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

.activity-points {
  color: var(--success);
  font-weight: 500;
}

/* Resume Page */
.resume-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-8);
}

.upload-card, .analysis-card {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.upload-area {
  text-align: center;
  padding: var(--space-8);
  border: 2px dashed var(--border);
  border-radius: var(--radius-lg);
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-area:hover {
  border-color: var(--primary);
  background: rgba(79, 70, 229, 0.05);
}

.upload-icon {
  font-size: 3rem;
  margin-bottom: var(--space-4);
  color: var(--text-secondary);
}

.upload-area h3 {
  margin-bottom: var(--space-2);
  color: var(--text-primary);
}

.upload-area p {
  color: var(--text-secondary);
  margin-bottom: var(--space-4);
}

.analysis-score {
  display: flex;
  align-items: center;
  gap: var(--space-6);
  margin-bottom: var(--space-6);
}

.score-circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: conic-gradient(var(--primary) 0deg, var(--gray-200) 0deg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
}

.score-details h4 {
  margin-bottom: var(--space-2);
  color: var(--text-primary);
}

.skills-analysis {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-6);
  margin-bottom: var(--space-6);
}

.skills-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.skill-tag {
  padding: var(--space-1) var(--space-3);
  background: var(--gray-100);
  border-radius: var(--radius);
  font-size: 0.875rem;
  color: var(--text-primary);
}

.skill-tag.matched {
  background: rgba(16, 185, 129, 0.1);
  color: var(--success);
}

.skill-tag.missing {
  background: rgba(239, 68, 68, 0.1);
  color: var(--danger);
}

/* Jobs Page */
.search-section {
  margin-bottom: var(--space-8);
}

.search-filters {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr auto;
  gap: var(--space-4);
  padding: var(--space-6);
  background: var(--surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.jobs-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.job-card {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  transition: transform 0.2s ease;
  cursor: pointer;
}

.job-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.job-header {
  display: flex;
  justify-content: between;
  align-items: start;
  margin-bottom: var(--space-4);
}

.job-company {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  flex: 1;
}

.company-logo {
  width: 50px;
  height: 50px;
  border-radius: var(--radius);
  background: var(--gray-100);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}

.job-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--space-1);
}

.job-company-name {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.job-match {
  background: rgba(16, 185, 129, 0.1);
  color: var(--success);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius);
  font-size: 0.875rem;
  font-weight: 500;
}

.job-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-4);
}

.job-detail {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.job-detail strong {
  color: var(--text-primary);
}

.job-skills {
  margin-bottom: var(--space-4);
}

.job-actions {
  display: flex;
  gap: var(--space-3);
}

/* Challenges Page */
.challenges-section {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.challenge-filters {
  display: flex;
  gap: var(--space-2);
}

.filter-btn {
  padding: var(--space-2) var(--space-4);
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--text-primary);
  border-radius: var(--radius);
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn.active,
.filter-btn:hover {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

.challenges-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--space-6);
}

.challenge-card {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  transition: transform 0.2s ease;
  cursor: pointer;
}

.challenge-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.challenge-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: var(--space-4);
}

.challenge-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}

.difficulty-badge {
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius);
  font-size: 0.875rem;
  font-weight: 500;
}

.difficulty-badge.easy {
  background: rgba(16, 185, 129, 0.1);
  color: var(--success);
}

.difficulty-badge.medium {
  background: rgba(245, 158, 11, 0.1);
  color: var(--warning);
}

.difficulty-badge.hard {
  background: rgba(239, 68, 68, 0.1);
  color: var(--danger);
}

.challenge-description {
  color: var(--text-secondary);
  margin-bottom: var(--space-4);
  line-height: 1.5;
}

.challenge-stats {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.875rem;
  color: var(--text-secondary);
}

.challenge-points {
  color: var(--primary);
  font-weight: 500;
}

/* Challenge Solver */
.solver-header {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--border);
}

.solver-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-8);
  height: calc(100vh - 200px);
}

.problem-section {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  overflow-y: auto;
}

.problem-description {
  margin-bottom: var(--space-6);
  line-height: 1.6;
}

.problem-examples,
.problem-constraints {
  margin-bottom: var(--space-6);
}

.problem-examples h4,
.problem-constraints h4 {
  margin-bottom: var(--space-3);
  color: var(--text-primary);
}

.example-block,
.constraint-block {
  background: var(--gray-50);
  padding: var(--space-4);
  border-radius: var(--radius);
  font-family: var(--font-mono);
  font-size: 0.9rem;
  white-space: pre-wrap;
}

.code-section {
  display: flex;
  flex-direction: column;
}

.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4);
  background: var(--surface);
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  border-bottom: 1px solid var(--border);
}

.code-editor {
  flex: 1;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  padding: var(--space-4);
  border: none;
  border-radius: 0 0 var(--radius-lg) var(--radius-lg);
  background: var(--surface);
  color: var(--text-primary);
  resize: none;
  outline: none;
}

.code-output {
  margin-top: var(--space-4);
  padding: var(--space-4);
  background: var(--gray-900);
  color: var(--gray-100);
  border-radius: var(--radius);
  font-family: var(--font-mono);
  font-size: 0.9rem;
}

/* Courses Page */
.courses-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: var(--space-6);
}

.course-card {
  background: var(--surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: transform 0.2s ease;
  cursor: pointer;
}

.course-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.course-thumbnail {
  height: 200px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  font-weight: 600;
}

.course-content {
  padding: var(--space-6);
}

.course-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.course-instructor {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-bottom: var(--space-3);
}

.course-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-4);
  font-size: 0.875rem;
  color: var(--text-secondary);
}

.course-rating {
  display: flex;
  align-items: center;
  gap: var(--space-1);
}

.course-description {
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: var(--space-4);
}

.course-price {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: var(--space-4);
}

/* Interview Page */
.interview-section {
  max-width: 800px;
  margin: 0 auto;
}

.interview-setup {
  text-align: center;
  background: var(--surface);
  padding: var(--space-8);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.interview-setup h3 {
  margin-bottom: var(--space-6);
  color: var(--text-primary);
}

.interview-types {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-8);
}

.interview-type {
  padding: var(--space-6);
  border: 2px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
}

.interview-type:hover,
.interview-type.selected {
  border-color: var(--primary);
  background: rgba(79, 70, 229, 0.05);
}

.type-icon {
  font-size: 2rem;
}

.type-name {
  font-weight: 500;
  color: var(--text-primary);
}

.interview-session {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.interview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--border);
}

.timer {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--primary);
}

.interview-content {
  display: grid;
  gap: var(--space-6);
}

.question-section {
  padding: var(--space-6);
  background: var(--gray-50);
  border-radius: var(--radius-lg);
}

.question-text {
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--text-primary);
}

.response-section textarea {
  min-height: 150px;
  margin-bottom: var(--space-4);
}

.interview-controls {
  display: flex;
  justify-content: space-between;
}

.interview-results {
  background: var(--surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

/* Profile Page */
.profile-section {
  max-width: 600px;
  margin: 0 auto;
}

.profile-card {
  background: var(--surface);
  padding: var(--space-8);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: var(--space-6);
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-6);
  border-bottom: 1px solid var(--border);
}

.profile-header img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 4px solid var(--primary);
}

.profile-info h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.profile-info p {
  color: var(--text-secondary);
  margin-bottom: var(--space-1);
}

.profile-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.stat {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 2rem;
  font-weight: 700;
  color: var(--primary);
}

.stat-label {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.skills-section,
.achievements-section {
  margin-bottom: var(--space-6);
}

.skills-section h4,
.achievements-section h4 {
  margin-bottom: var(--space-4);
  color: var(--text-primary);
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: var(--space-4);
}

.achievement-badge {
  text-align: center;
  padding: var(--space-4);
  background: var(--gray-50);
  border-radius: var(--radius-lg);
}

.achievement-icon {
  font-size: 2rem;
  margin-bottom: var(--space-2);
}

.achievement-title {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-primary);
}

/* Notifications */
.notifications-container {
  position: fixed;
  top: var(--space-4);
  right: var(--space-4);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.notification {
  background: var(--surface);
  padding: var(--space-4);
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
  border-left: 4px solid var(--primary);
  max-width: 400px;
  animation: slideIn 0.3s ease;
}

.notification.success {
  border-left-color: var(--success);
}

.notification.warning {
  border-left-color: var(--warning);
}

.notification.error {
  border-left-color: var(--danger);
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Chatbot */
.chatbot-container {
  position: fixed;
  bottom: var(--space-4);
  right: var(--space-4);
  z-index: 1000;
}

.chatbot-toggle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  box-shadow: var(--shadow-lg);
  transition: transform 0.2s ease;
}

.chatbot-toggle:hover {
  transform: scale(1.1);
}

.chatbot-window {
  position: absolute;
  bottom: 80px;
  right: 0;
  width: 350px;
  height: 500px;
  background: var(--surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  display: flex;
  flex-direction: column;
}

.chatbot-header {
  padding: var(--space-4);
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--primary);
  color: white;
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
}

.chatbot-header button {
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
}

.chatbot-messages {
  flex: 1;
  padding: var(--space-4);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.chat-message {
  max-width: 80%;
  padding: var(--space-3);
  border-radius: var(--radius);
  font-size: 0.9rem;
}

.chat-message.user {
  align-self: flex-end;
  background: var(--primary);
  color: white;
}

.chat-message.bot {
  align-self: flex-start;
  background: var(--gray-100);
  color: var(--text-primary);
}

.chatbot-input {
  padding: var(--space-4);
  border-top: 1px solid var(--border);
  display: flex;
  gap: var(--space-2);
}

.chatbot-input input {
  flex: 1;
  padding: var(--space-2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  font-size: 0.9rem;
}

.chatbot-input button {
  padding: var(--space-2) var(--space-4);
  background: var(--primary);
  color: white;
  border: none;
  border-radius: var(--radius);
  cursor: pointer;
  font-size: 0.9rem;
}

/* Loading */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  color: white;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s ease-in-out infinite;
  margin-bottom: var(--space-4);
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .main-container {
    grid-template-areas: 
      "header"
      "content";
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    display: none;
  }
  
  .welcome-hero h1 {
    font-size: 2.5rem;
  }
  
  .welcome-features {
    grid-template-columns: 1fr;
  }
  
  .role-grid {
    grid-template-columns: 1fr;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .charts-section {
    grid-template-columns: 1fr;
  }
  
  .resume-section {
    grid-template-columns: 1fr;
  }
  
  .search-filters {
    grid-template-columns: 1fr;
  }
  
  .solver-content {
    grid-template-columns: 1fr;
    height: auto;
  }
  
  .challenges-list {
    grid-template-columns: 1fr;
  }
  
  .courses-list {
    grid-template-columns: 1fr;
  }
  
  .interview-types {
    grid-template-columns: 1fr;
  }
  
  .chatbot-window {
    width: calc(100vw - 2rem);
    right: var(--space-4);
    left: var(--space-4);
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .app-header {
    padding: var(--space-3);
  }
  
  .user-stats {
    display: none;
  }
  
  .main-content {
    padding: var(--space-4);
  }
  
  .page-header h2 {
    font-size: 1.5rem;
  }
}

/* Print Styles */
@media print {
  .sidebar,
  .chatbot-container,
  .notifications-container {
    display: none;
  }
  
  .main-container {
    grid-template-areas: "content";
    grid-template-columns: 1fr;
  }
  
  .main-content {
    padding: 0;
  }
}'''

# Save the CSS file
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ Created complete CSS file (style.css)")
print(f"📄 File size: {len(css_content)} characters")