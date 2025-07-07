"""
AI Project Charter & Configuration Tool
A Streamlit multi-page application for AI project planning and configuration
"""

import streamlit as st
import json
import os
from datetime import datetime
from typing import Dict, List, Any

# Try to import yaml, use json as fallback
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Configure the page
st.set_page_config(
    page_title="AI Project Charter Tool",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Utility functions
def save_config_to_file():
    """Save current configuration to configs directory"""
    os.makedirs("configs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"configs/project_config_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(st.session_state.project_config, f, indent=2, default=str)
    
    return filename

def load_config_from_file(filename):
    """Load configuration from file"""
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
        st.session_state.project_config.update(config)
        return True
    except Exception as e:
        st.error(f"Error loading config: {e}")
        return False

def generate_ai_response(prompt: str) -> str:
    """Generate AI-like response based on prompt keywords"""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ['problem', 'solve', 'issue']):
        return "Great! Understanding the problem is crucial. Can you be more specific about the current pain points and what metrics you'd use to measure success?"
    
    elif any(word in prompt_lower for word in ['user', 'customer', 'people']):
        return "User analysis is key! Tell me more about their technical skills and how they currently handle this process. Are they technical or non-technical users?"
    
    elif any(word in prompt_lower for word in ['interface', 'ui', 'interaction']):
        return "Interface design is important! Are you thinking of a chat interface, web dashboard, API, or something else? What would work best for your users?"
    
    elif any(word in prompt_lower for word in ['architecture', 'system', 'components']):
        return "Let's break down the system architecture. What specialized functions do you need? Think about data processing, analysis, storage, and user interface components."
    
    elif any(word in prompt_lower for word in ['budget', 'cost', 'constraint']):
        return "Constraints help guide technical decisions. What's your budget, performance requirements, and any compliance needs like GDPR or security standards?"
    
    elif any(word in prompt_lower for word in ['timeline', 'schedule', 'deadline']):
        return "Timeline planning is crucial! What's your target go-live date? Should we plan for phases like prototype, development, testing, and deployment?"
    
    else:
        return "That's an interesting point! Can you elaborate on how this fits into your overall project goals? I'm here to help you structure your AI project effectively."

def update_config_from_chat(prompt: str):
    """Update project configuration based on chat content"""
    # Simple keyword-based extraction
    prompt_lower = prompt.lower()
    
    # Extract project name
    if 'project' in prompt_lower and 'name' in prompt_lower:
        # Simple extraction - could be improved with NLP
        pass
    
    # Store chat history
    st.session_state.project_config['chat_history'].append({
        'timestamp': datetime.now().isoformat(),
        'content': prompt
    })

def validate_configuration(config: Dict) -> Dict:
    """Validate the current configuration"""
    results = {}
    
    # Project name validation
    if config.get('project_name'):
        results['Project Name'] = {'valid': True, 'message': 'Project name is set'}
    else:
        results['Project Name'] = {'valid': False, 'message': 'Project name is required'}
    
    # Problem statement validation
    if config.get('problem_statement') and len(config['problem_statement']) > 20:
        results['Problem Statement'] = {'valid': True, 'message': 'Problem statement is detailed'}
    else:
        results['Problem Statement'] = {'valid': False, 'message': 'Problem statement needs more detail'}
    
    # Users validation
    if config.get('users'):
        results['Users'] = {'valid': True, 'message': f"{len(config['users'])} user types defined"}
    else:
        results['Users'] = {'valid': False, 'message': 'User types need to be defined'}
    
    # Architecture validation
    if config.get('system_components') and len(config['system_components']) >= 3:
        results['Architecture'] = {'valid': True, 'message': 'System components are defined'}
    else:
        results['Architecture'] = {'valid': False, 'message': 'Need at least 3 system components'}
    
    return results

def generate_project_charter() -> str:
    """Generate project charter based on current configuration"""
    config = st.session_state.project_config
    
    charter = f"""# {config.get('project_name', 'AI Project')} Charter

## Project Overview
**Problem Statement:** {config.get('problem_statement', 'Not defined')}

## User Analysis
**Target Users:** {', '.join(config.get('users', []))}
**Interaction Patterns:** {', '.join(config.get('interaction_patterns', []))}

## System Architecture
**Components:** {', '.join(config.get('system_components', []))}
**Technology Stack:** {config.get('tech_stack', 'Not defined')}

## Constraints
**Budget:** €{config.get('constraints', {}).get('budget', 0)}/month
**Performance:** {config.get('constraints', {}).get('performance', 'Not defined')}
**Compliance:** {', '.join(config.get('constraints', {}).get('compliance', []))}

## Success Metrics
**Efficiency Gain:** {config.get('success_metrics', {}).get('efficiency_gain', 0)}%
**Accuracy Target:** {config.get('success_metrics', {}).get('accuracy_target', 0)}%
**User Adoption:** {config.get('success_metrics', {}).get('user_adoption', 0)} users

## Timeline
**Start Date:** {config.get('timeline', {}).get('start_date', 'Not defined')}
**End Date:** {config.get('timeline', {}).get('end_date', 'Not defined')}
**Phases:** {', '.join(config.get('timeline', {}).get('phases', []))}

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    return charter

def generate_technical_spec() -> str:
    """Generate technical specification"""
    config = st.session_state.project_config
    
    spec = f"""# {config.get('project_name', 'AI Project')} Technical Specification

## System Requirements
- **Performance:** {config.get('constraints', {}).get('performance', 'Not defined')} response time
- **Scalability:** Support for {config.get('success_metrics', {}).get('user_adoption', 0)} concurrent users
- **Availability:** 99.9% uptime target

## Architecture Components
"""
    
    for component in config.get('system_components', []):
        spec += f"- **{component}:** Implementation details to be defined\n"
    
    spec += f"""
## Technology Stack
- **Primary:** {config.get('tech_stack', 'Python + FastAPI')}
- **Database:** To be determined based on data requirements
- **Deployment:** {config.get('deployment_type', 'Cloud Platform')}

## Integration Points
"""
    
    for pattern in config.get('interaction_patterns', []):
        spec += f"- **{pattern}:** API endpoints and data flow to be defined\n"
    
    spec += f"""
## Security Requirements
- **Compliance:** {', '.join(config.get('constraints', {}).get('compliance', ['Standard security practices']))}
- **Authentication:** User authentication and authorization
- **Data Protection:** Encryption in transit and at rest

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    return spec

def generate_python_config() -> str:
    """Generate Python configuration file"""
    config = st.session_state.project_config
    
    python_config = f'''"""
Configuration file for {config.get('project_name', 'AI Project')}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProjectConfig:
    """Project configuration settings"""
    
    # Basic project info
    PROJECT_NAME: str = "{config.get('project_name', 'ai-project')}"
    PROBLEM_STATEMENT: str = "{config.get('problem_statement', '')}"
    
    # User configuration
    TARGET_USERS: List[str] = {config.get('users', [])}
    INTERACTION_PATTERNS: List[str] = {config.get('interaction_patterns', [])}
    
    # System architecture
    SYSTEM_COMPONENTS: List[str] = {config.get('system_components', [])}
    TECH_STACK: str = "{config.get('tech_stack', 'Python + FastAPI')}"
    
    # Constraints
    MONTHLY_BUDGET: float = {config.get('constraints', {}).get('budget', 500)}
    PERFORMANCE_REQUIREMENT: str = "{config.get('constraints', {}).get('performance', '< 2 sec')}"
    COMPLIANCE_REQUIREMENTS: List[str] = {config.get('constraints', {}).get('compliance', [])}
    
    # Success metrics
    EFFICIENCY_GAIN_TARGET: int = {config.get('success_metrics', {}).get('efficiency_gain', 50)}
    ACCURACY_TARGET: int = {config.get('success_metrics', {}).get('accuracy_target', 95)}
    USER_ADOPTION_TARGET: int = {config.get('success_metrics', {}).get('user_adoption', 50)}
    
    # Timeline
    START_DATE: str = "{config.get('timeline', {}).get('start_date', '')}"
    END_DATE: str = "{config.get('timeline', {}).get('end_date', '')}"
    PROJECT_PHASES: List[str] = {config.get('timeline', {}).get('phases', [])}

# Global configuration instance
config = ProjectConfig()

# Environment-specific settings
DEVELOPMENT = {{
    "DEBUG": True,
    "DATABASE_URL": "sqlite:///dev.db",
    "LOG_LEVEL": "DEBUG"
}}

PRODUCTION = {{
    "DEBUG": False,
    "DATABASE_URL": "postgresql://user:pass@localhost/prod",
    "LOG_LEVEL": "INFO"
}}

# Feature flags
FEATURES = {{
    "ENABLE_CHAT": True,
    "ENABLE_DASHBOARD": True,
    "ENABLE_API": True,
    "ENABLE_MONITORING": True
}}
'''
    
    return python_config

def generate_dockerfile() -> str:
    """Generate Dockerfile for containerization"""
    config = st.session_state.project_config
    
    dockerfile = f"""# Dockerfile for {config.get('project_name', 'AI Project')}
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["python", "main.py"]
"""
    
    return dockerfile

def generate_requirements() -> str:
    """Generate requirements.txt file"""
    config = st.session_state.project_config
    
    requirements = """# Core dependencies
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0

# Web framework
fastapi>=0.100.0
uvicorn>=0.20.0

# Database
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0

# AI/ML libraries
openai>=1.0.0
langchain>=0.1.0
huggingface-hub>=0.16.0

# Utilities
python-dotenv>=1.0.0
pydantic>=2.0.0
requests>=2.31.0
pyyaml>=6.0

# Development tools
pytest>=7.0.0
black>=23.0.0
ruff>=0.1.0

# Monitoring
prometheus-client>=0.17.0
"""
    
    return requirements

# Initialize session state
if 'project_config' not in st.session_state:
    st.session_state.project_config = {
        'project_name': '',
        'problem_statement': '',
        'users': [],
        'interaction_patterns': [],
        'system_components': [],
        'constraints': {},
        'success_metrics': {},
        'timeline': {},
        'chat_history': [],
        'current_step': 'concept',
        'completion_status': {
            'Problem Definition': False,
            'User Analysis': False,
            'Interaction Design': False,
            'Architecture': False,
            'Constraints': False,
            'Success Metrics': False,
            'Timeline': False
        }
    }

# Ensure completion_status has all required keys (for existing sessions)
required_completion_keys = [
    'Problem Definition', 'User Analysis', 'Interaction Design', 
    'Architecture', 'Constraints', 'Success Metrics', 'Timeline'
]
for key in required_completion_keys:
    if key not in st.session_state.project_config.get('completion_status', {}):
        st.session_state.project_config.setdefault('completion_status', {})[key] = False

if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []

if 'current_section' not in st.session_state:
    st.session_state.current_section = 'dashboard'

# Sidebar Navigation
with st.sidebar:
    st.title("🎯 AI Project Charter")
    
    # Navigation
    page = st.selectbox(
        "Navigate to:",
        ["Dashboard", "Interactive Chat", "Configuration", "Export & Deploy"],
        key="navigation"
    )
    
    st.divider()
    
    # Progress tracking
    st.subheader("📊 Progress")
    progress_sections = [
        "Problem Definition",
        "User Analysis", 
        "Interaction Design",
        "Architecture",
        "Constraints",
        "Success Metrics",
        "Timeline"
    ]
    
    for section in progress_sections:
        status = st.session_state.project_config.get('completion_status', {}).get(section, False)
        st.write(f"{'✅' if status else '⏳'} {section}")
    
    st.divider()
    
    # Quick actions
    st.subheader("🚀 Quick Actions")
    if st.button("Reset Project"):
        st.session_state.project_config = {
            'project_name': '',
            'problem_statement': '',
            'users': [],
            'interaction_patterns': [],
            'system_components': [],
            'constraints': {},
            'success_metrics': {},
            'timeline': {},
            'chat_history': [],
            'current_step': 'concept',
            'completion_status': {}
        }
        st.rerun()
    
    if st.button("Save Progress"):
        save_config_to_file()
        st.success("Progress saved!")

# Main content based on navigation
if page == "Dashboard":
    st.title("🎯 AI Project Dashboard")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Project Overview")
        
        # Project name input
        project_name = st.text_input(
            "Project Name",
            value=st.session_state.project_config.get('project_name', ''),
            placeholder="Enter your AI project name"
        )
        st.session_state.project_config['project_name'] = project_name
        
        # Problem statement
        problem_statement = st.text_area(
            "Problem Statement",
            value=st.session_state.project_config.get('problem_statement', ''),
            placeholder="What specific problem are you solving?",
            height=100
        )
        st.session_state.project_config['problem_statement'] = problem_statement
        
        # Mark Problem Definition completion
        if project_name and problem_statement and len(problem_statement) > 20:
            st.session_state.project_config['completion_status']['Problem Definition'] = True
        else:
            st.session_state.project_config['completion_status']['Problem Definition'] = False
        
        # Tabbed interface for different sections
        tab1, tab2, tab3, tab4 = st.tabs([
            "👥 Users & Interaction", 
            "🏗️ Architecture", 
            "📏 Constraints & Metrics",
            "📅 Timeline"
        ])
        
        with tab1:
            st.subheader("User Analysis")
            
            # User types
            user_types = st.multiselect(
                "Primary User Types",
                ["Technical Users", "Business Users", "End Customers", "Analysts", "Administrators"],
                default=st.session_state.project_config.get('users', [])
            )
            st.session_state.project_config['users'] = user_types
            
            # Interaction patterns
            interaction_patterns = st.multiselect(
                "Interaction Patterns",
                ["Chat Interface", "API Calls", "Web Dashboard", "Mobile App", "Batch Processing", "Real-time Processing"],
                default=st.session_state.project_config.get('interaction_patterns', [])
            )
            st.session_state.project_config['interaction_patterns'] = interaction_patterns
            
            # Mark completion for both User Analysis and Interaction Design
            if user_types and interaction_patterns:
                st.session_state.project_config['completion_status']['User Analysis'] = True
                st.session_state.project_config['completion_status']['Interaction Design'] = True
            else:
                st.session_state.project_config['completion_status']['User Analysis'] = False
                st.session_state.project_config['completion_status']['Interaction Design'] = False
        
        with tab2:
            st.subheader("System Architecture")
            
            # System components
            components = st.multiselect(
                "System Components",
                [
                    "Data Ingestion", "Data Processing", "ML Models", "API Gateway",
                    "User Interface", "Database", "Cache Layer", "Message Queue",
                    "Authentication", "Monitoring", "Logging", "Analytics"
                ],
                default=st.session_state.project_config.get('system_components', [])
            )
            st.session_state.project_config['system_components'] = components
            
            # Technology stack
            tech_stack = st.selectbox(
                "Primary Technology Stack",
                ["Python + FastAPI", "Python + Django", "Node.js + Express", "Python + Streamlit", "Other"],
                index=0
            )
            st.session_state.project_config['tech_stack'] = tech_stack
            
            if components:
                st.session_state.project_config['completion_status']['Architecture'] = True
            else:
                st.session_state.project_config['completion_status']['Architecture'] = False
        
        with tab3:
            st.subheader("Constraints & Success Metrics")
            
            col3, col4 = st.columns(2)
            
            with col3:
                st.write("**Constraints**")
                budget = st.number_input("Monthly Budget (€)", min_value=0, value=500)
                performance = st.selectbox("Performance Requirement", ["< 1 sec", "< 2 sec", "< 5 sec", "< 10 sec"])
                compliance = st.multiselect("Compliance Requirements", ["GDPR", "HIPAA", "SOC2", "ISO27001"])
                
                st.session_state.project_config['constraints'] = {
                    'budget': budget,
                    'performance': performance,
                    'compliance': compliance
                }
            
            with col4:
                st.write("**Success Metrics**")
                efficiency_gain = st.slider("Expected Efficiency Gain (%)", 0, 100, 50)
                accuracy_target = st.slider("Accuracy Target (%)", 0, 100, 95)
                user_adoption = st.number_input("Target Active Users", min_value=1, value=50)
                
                st.session_state.project_config['success_metrics'] = {
                    'efficiency_gain': efficiency_gain,
                    'accuracy_target': accuracy_target,
                    'user_adoption': user_adoption
                }
            
            if budget and performance:
                st.session_state.project_config['completion_status']['Constraints'] = True
                st.session_state.project_config['completion_status']['Success Metrics'] = True
            else:
                st.session_state.project_config['completion_status']['Constraints'] = False
                st.session_state.project_config['completion_status']['Success Metrics'] = False
        
        with tab4:
            st.subheader("Project Timeline")
            
            col5, col6 = st.columns(2)
            
            with col5:
                start_date = st.date_input("Project Start Date", datetime.now().date())
                end_date = st.date_input("Target Go-Live Date")
                
            with col6:
                phases = st.multiselect(
                    "Project Phases",
                    ["Discovery", "Prototype", "Development", "Testing", "Deployment", "Maintenance"],
                    default=["Discovery", "Prototype", "Development", "Testing", "Deployment"]
                )
            
            st.session_state.project_config['timeline'] = {
                'start_date': str(start_date),
                'end_date': str(end_date),
                'phases': phases
            }
            
            if start_date and end_date and phases:
                st.session_state.project_config['completion_status']['Timeline'] = True
            else:
                st.session_state.project_config['completion_status']['Timeline'] = False
    
    with col2:
        st.subheader("🎯 Project Health")
        
        # Calculate completion percentage
        total_sections = len(progress_sections)
        completed_sections = sum(1 for status in st.session_state.project_config.get('completion_status', {}).values() if status)
        completion_percentage = (completed_sections / total_sections) * 100
        
        st.metric("Completion", f"{completion_percentage:.0f}%")
        st.progress(completion_percentage / 100)
        
        st.subheader("📋 Next Steps")
        
        incomplete_sections = [
            section for section in progress_sections 
            if not st.session_state.project_config.get('completion_status', {}).get(section, False)
        ]
        
        if incomplete_sections:
            st.write("Complete these sections:")
            for section in incomplete_sections[:3]:  # Show top 3
                st.write(f"• {section}")
        else:
            st.success("All sections completed! 🎉")
            st.write("Ready to export configuration and start development.")
        
        st.subheader("🔧 Quick Config")
        
        # Load existing configs
        config_files = []
        if os.path.exists("configs"):
            config_files = [f for f in os.listdir("configs") if f.endswith('.json')]
        
        if config_files:
            selected_config = st.selectbox("Load Previous Config", ["None"] + config_files)
            if selected_config != "None" and st.button("Load Config"):
                if load_config_from_file(f"configs/{selected_config}"):
                    st.success("Configuration loaded!")
                    st.rerun()

elif page == "Interactive Chat":
    st.title("🤖 Interactive Project Planning Chat")
    
    # Chat interface for guided project planning
    chat_container = st.container()
    
    # Predefined questions based on charter template
    planning_questions = {
        "Problem Definition": [
            "What specific inefficiency are you solving?",
            "What are the current pain points in your process?",
            "What quantifiable change will this system bring?",
            "How does this align with your organizational objectives?"
        ],
        "User Analysis": [
            "Who will directly interact with the system?",
            "Are your users technical or non-technical?",
            "How do users currently solve this problem?",
            "How often will users interact with the system?"
        ],
        "Interaction Design": [
            "What should be the primary interface - chat, API, or dashboard?",
            "Do you need real-time responses or batch processing?",
            "How should results be delivered to users?",
            "What external systems need to connect?"
        ],
        "Architecture": [
            "What specialized functions are needed?",
            "What data sources will the system process?",
            "What analysis or transformation is required?",
            "How many users will the system handle?"
        ],
        "Constraints": [
            "What's the maximum monthly operational cost?",
            "What regulations must be followed?",
            "What response times are acceptable?",
            "What uptime is required?"
        ]
    }
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Display chat history
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask about your project or answer the questions..."):
            # Add user message
            st.session_state.chat_messages.append({"role": "user", "content": prompt})
            
            # Simple AI-like response based on keywords
            ai_response = generate_ai_response(prompt)
            st.session_state.chat_messages.append({"role": "assistant", "content": ai_response})
            
            # Update project config based on chat
            update_config_from_chat(prompt)
            
            st.rerun()
    
    with col2:
        st.subheader("💡 Guided Questions")
        
        selected_category = st.selectbox(
            "Question Category",
            list(planning_questions.keys())
        )
        
        st.write(f"**{selected_category} Questions:**")
        for i, question in enumerate(planning_questions[selected_category]):
            if st.button(f"Q{i+1}: {question[:30]}...", key=f"q_{selected_category}_{i}"):
                st.session_state.chat_messages.append({"role": "assistant", "content": question})
                st.rerun()
        
        st.divider()
        
        if st.button("Clear Chat"):
            st.session_state.chat_messages = []
            st.rerun()

elif page == "Configuration":
    st.title("⚙️ Advanced Configuration")
    
    # JSON editor for advanced users
    st.subheader("Configuration Editor")
    
    config_json = st.text_area(
        "Edit Configuration (JSON)",
        value=json.dumps(st.session_state.project_config, indent=2),
        height=400
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Update Configuration"):
            try:
                new_config = json.loads(config_json)
                st.session_state.project_config.update(new_config)
                st.success("Configuration updated!")
            except json.JSONDecodeError as e:
                st.error(f"Invalid JSON: {e}")
    
    with col2:
        if st.button("Reset to Default"):
            st.session_state.project_config = {
                'project_name': '',
                'problem_statement': '',
                'users': [],
                'interaction_patterns': [],
                'system_components': [],
                'constraints': {},
                'success_metrics': {},
                'timeline': {},
                'chat_history': [],
                'current_step': 'concept',
                'completion_status': {}
            }
            st.rerun()
    
    st.divider()
    
    # Configuration validation
    st.subheader("Configuration Validation")
    
    validation_results = validate_configuration(st.session_state.project_config)
    
    for category, result in validation_results.items():
        if result['valid']:
            st.success(f"✅ {category}: {result['message']}")
        else:
            st.error(f"❌ {category}: {result['message']}")

elif page == "Export & Deploy":
    st.title("📤 Export & Deploy")
    
    st.subheader("Generate Project Files")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Available Exports:**")
        
        # Generate different file formats
        if st.button("📋 Generate Project Charter"):
            charter_content = generate_project_charter()
            st.text_area("Project Charter (Markdown)", charter_content, height=300)
            
            # Save to file
            with open("docs/generated_charter.md", "w") as f:
                f.write(charter_content)
            st.success("Charter saved to docs/generated_charter.md")
        
        if st.button("⚙️ Generate Technical Spec"):
            tech_spec = generate_technical_spec()
            st.text_area("Technical Specification", tech_spec, height=300)
            
            # Save to file
            with open("docs/technical_spec.md", "w") as f:
                f.write(tech_spec)
            st.success("Technical spec saved to docs/technical_spec.md")
        
        if st.button("🐍 Generate Python Config"):
            python_config = generate_python_config()
            st.code(python_config, language="python")
            
            # Save to file
            with open("src/config.py", "w") as f:
                f.write(python_config)
            st.success("Python config saved to src/config.py")
    
    with col2:
        st.write("**Deployment Options:**")
        
        deployment_type = st.selectbox(
            "Deployment Type",
            ["Local Development", "Docker Container", "Cloud Platform", "Kubernetes"]
        )
        
        if st.button("🚀 Generate Deployment Files"):
            if deployment_type == "Docker Container":
                dockerfile_content = generate_dockerfile()
                st.code(dockerfile_content, language="dockerfile")
                
                with open("Dockerfile", "w") as f:
                    f.write(dockerfile_content)
                st.success("Dockerfile generated!")
            
            elif deployment_type == "Cloud Platform":
                requirements_content = generate_requirements()
                st.code(requirements_content, language="text")
                
                with open("requirements.txt", "w") as f:
                    f.write(requirements_content)
                st.success("Requirements.txt generated!")
        
        st.divider()
        
        st.write("**Configuration Files:**")
        
        # Save final configuration
        if st.button("💾 Save Final Configuration"):
            filename = save_config_to_file()
            st.success(f"Configuration saved to {filename}")
            
            # Also save as YAML if available
            if HAS_YAML:
                import yaml  # Import here to avoid error if not available
                yaml_filename = filename.replace('.json', '.yaml')
                with open(yaml_filename, 'w') as f:
                    yaml.dump(st.session_state.project_config, f, default_flow_style=False)
                st.success(f"YAML configuration saved to {yaml_filename}")

def generate_ai_response(prompt: str) -> str:
    """Generate AI-like response based on prompt keywords"""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ['problem', 'solve', 'issue']):
        return "Great! Understanding the problem is crucial. Can you be more specific about the current pain points and what metrics you'd use to measure success?"
    
    elif any(word in prompt_lower for word in ['user', 'customer', 'people']):
        return "User analysis is key! Tell me more about their technical skills and how they currently handle this process. Are they technical or non-technical users?"
    
    elif any(word in prompt_lower for word in ['interface', 'ui', 'interaction']):
        return "Interface design is important! Are you thinking of a chat interface, web dashboard, API, or something else? What would work best for your users?"
    
    elif any(word in prompt_lower for word in ['architecture', 'system', 'components']):
        return "Let's break down the system architecture. What specialized functions do you need? Think about data processing, analysis, storage, and user interface components."
    
    elif any(word in prompt_lower for word in ['budget', 'cost', 'constraint']):
        return "Constraints help guide technical decisions. What's your budget, performance requirements, and any compliance needs like GDPR or security standards?"
    
    elif any(word in prompt_lower for word in ['timeline', 'schedule', 'deadline']):
        return "Timeline planning is crucial! What's your target go-live date? Should we plan for phases like prototype, development, testing, and deployment?"
    
    else:
        return "That's an interesting point! Can you elaborate on how this fits into your overall project goals? I'm here to help you structure your AI project effectively."

def update_config_from_chat(prompt: str):
    """Update project configuration based on chat content"""
    # Simple keyword-based extraction
    prompt_lower = prompt.lower()
    
    # Extract project name
    if 'project' in prompt_lower and 'name' in prompt_lower:
        # Simple extraction - could be improved with NLP
        pass
    
    # Store chat history
    st.session_state.project_config['chat_history'].append({
        'timestamp': datetime.now().isoformat(),
        'content': prompt
    })

def validate_configuration(config: Dict) -> Dict:
    """Validate the current configuration"""
    results = {}
    
    # Project name validation
    if config.get('project_name'):
        results['Project Name'] = {'valid': True, 'message': 'Project name is set'}
    else:
        results['Project Name'] = {'valid': False, 'message': 'Project name is required'}
    
    # Problem statement validation
    if config.get('problem_statement') and len(config['problem_statement']) > 20:
        results['Problem Statement'] = {'valid': True, 'message': 'Problem statement is detailed'}
    else:
        results['Problem Statement'] = {'valid': False, 'message': 'Problem statement needs more detail'}
    
    # Users validation
    if config.get('users'):
        results['Users'] = {'valid': True, 'message': f"{len(config['users'])} user types defined"}
    else:
        results['Users'] = {'valid': False, 'message': 'User types need to be defined'}
    
    # Architecture validation
    if config.get('system_components') and len(config['system_components']) >= 3:
        results['Architecture'] = {'valid': True, 'message': 'System components are defined'}
    else:
        results['Architecture'] = {'valid': False, 'message': 'Need at least 3 system components'}
    
    return results

def generate_project_charter() -> str:
    """Generate project charter based on current configuration"""
    config = st.session_state.project_config
    
    charter = f"""# {config.get('project_name', 'AI Project')} Charter

## Project Overview
**Problem Statement:** {config.get('problem_statement', 'Not defined')}

## User Analysis
**Target Users:** {', '.join(config.get('users', []))}
**Interaction Patterns:** {', '.join(config.get('interaction_patterns', []))}

## System Architecture
**Components:** {', '.join(config.get('system_components', []))}
**Technology Stack:** {config.get('tech_stack', 'Not defined')}

## Constraints
**Budget:** €{config.get('constraints', {}).get('budget', 0)}/month
**Performance:** {config.get('constraints', {}).get('performance', 'Not defined')}
**Compliance:** {', '.join(config.get('constraints', {}).get('compliance', []))}

## Success Metrics
**Efficiency Gain:** {config.get('success_metrics', {}).get('efficiency_gain', 0)}%
**Accuracy Target:** {config.get('success_metrics', {}).get('accuracy_target', 0)}%
**User Adoption:** {config.get('success_metrics', {}).get('user_adoption', 0)} users

## Timeline
**Start Date:** {config.get('timeline', {}).get('start_date', 'Not defined')}
**End Date:** {config.get('timeline', {}).get('end_date', 'Not defined')}
**Phases:** {', '.join(config.get('timeline', {}).get('phases', []))}

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    return charter

def generate_technical_spec() -> str:
    """Generate technical specification"""
    config = st.session_state.project_config
    
    spec = f"""# {config.get('project_name', 'AI Project')} Technical Specification

## System Requirements
- **Performance:** {config.get('constraints', {}).get('performance', 'Not defined')} response time
- **Scalability:** Support for {config.get('success_metrics', {}).get('user_adoption', 0)} concurrent users
- **Availability:** 99.9% uptime target

## Architecture Components
"""
    
    for component in config.get('system_components', []):
        spec += f"- **{component}:** Implementation details to be defined\n"
    
    spec += f"""
## Technology Stack
- **Primary:** {config.get('tech_stack', 'Python + FastAPI')}
- **Database:** To be determined based on data requirements
- **Deployment:** {config.get('deployment_type', 'Cloud Platform')}

## Integration Points
"""
    
    for pattern in config.get('interaction_patterns', []):
        spec += f"- **{pattern}:** API endpoints and data flow to be defined\n"
    
    spec += f"""
## Security Requirements
- **Compliance:** {', '.join(config.get('constraints', {}).get('compliance', ['Standard security practices']))}
- **Authentication:** User authentication and authorization
- **Data Protection:** Encryption in transit and at rest

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    return spec

def generate_python_config() -> str:
    """Generate Python configuration file"""
    config = st.session_state.project_config
    
    python_config = f'''"""
Configuration file for {config.get('project_name', 'AI Project')}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProjectConfig:
    """Project configuration settings"""
    
    # Basic project info
    PROJECT_NAME: str = "{config.get('project_name', 'ai-project')}"
    PROBLEM_STATEMENT: str = "{config.get('problem_statement', '')}"
    
    # User configuration
    TARGET_USERS: List[str] = {config.get('users', [])}
    INTERACTION_PATTERNS: List[str] = {config.get('interaction_patterns', [])}
    
    # System architecture
    SYSTEM_COMPONENTS: List[str] = {config.get('system_components', [])}
    TECH_STACK: str = "{config.get('tech_stack', 'Python + FastAPI')}"
    
    # Constraints
    MONTHLY_BUDGET: float = {config.get('constraints', {}).get('budget', 500)}
    PERFORMANCE_REQUIREMENT: str = "{config.get('constraints', {}).get('performance', '< 2 sec')}"
    COMPLIANCE_REQUIREMENTS: List[str] = {config.get('constraints', {}).get('compliance', [])}
    
    # Success metrics
    EFFICIENCY_GAIN_TARGET: int = {config.get('success_metrics', {}).get('efficiency_gain', 50)}
    ACCURACY_TARGET: int = {config.get('success_metrics', {}).get('accuracy_target', 95)}
    USER_ADOPTION_TARGET: int = {config.get('success_metrics', {}).get('user_adoption', 50)}
    
    # Timeline
    START_DATE: str = "{config.get('timeline', {}).get('start_date', '')}"
    END_DATE: str = "{config.get('timeline', {}).get('end_date', '')}"
    PROJECT_PHASES: List[str] = {config.get('timeline', {}).get('phases', [])}

# Global configuration instance
config = ProjectConfig()

# Environment-specific settings
DEVELOPMENT = {{
    "DEBUG": True,
    "DATABASE_URL": "sqlite:///dev.db",
    "LOG_LEVEL": "DEBUG"
}}

PRODUCTION = {{
    "DEBUG": False,
    "DATABASE_URL": "postgresql://user:pass@localhost/prod",
    "LOG_LEVEL": "INFO"
}}

# Feature flags
FEATURES = {{
    "ENABLE_CHAT": True,
    "ENABLE_DASHBOARD": True,
    "ENABLE_API": True,
    "ENABLE_MONITORING": True
}}
'''
    
    return python_config

def generate_dockerfile() -> str:
    """Generate Dockerfile for containerization"""
    config = st.session_state.project_config
    
    dockerfile = f"""# Dockerfile for {config.get('project_name', 'AI Project')}
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["python", "main.py"]
"""
    
    return dockerfile

def generate_requirements() -> str:
    """Generate requirements.txt file"""
    config = st.session_state.project_config
    
    requirements = """# Core dependencies
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0

# Web framework
fastapi>=0.100.0
uvicorn>=0.20.0

# Database
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0

# AI/ML libraries
openai>=1.0.0
langchain>=0.1.0
huggingface-hub>=0.16.0

# Utilities
python-dotenv>=1.0.0
pydantic>=2.0.0
requests>=2.31.0
pyyaml>=6.0

# Development tools
pytest>=7.0.0
black>=23.0.0
ruff>=0.1.0

# Monitoring
prometheus-client>=0.17.0
"""
    
    return requirements

if __name__ == "__main__":
    # This will run when the script is executed directly
    pass
