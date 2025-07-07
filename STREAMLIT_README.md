# 🎯 AI Project Charter & Configuration Tool

A comprehensive Streamlit multi-page application designed to guide you through AI project planning and configuration based on the structured charter template methodology.

## 🚀 Features

### 📊 **Dashboard**
- **Project Overview**: Define project name and problem statement
- **User Analysis**: Identify target users and interaction patterns
- **System Architecture**: Select components and technology stack
- **Constraints & Metrics**: Set budget, performance, and success criteria
- **Timeline Planning**: Define phases and milestones
- **Progress Tracking**: Visual completion status and next steps

### 🤖 **Interactive Chat**
- **Guided Questions**: AI-powered questions based on charter template
- **Dynamic Responses**: Context-aware responses to user inputs
- **Project Planning**: Step-by-step guidance through planning process
- **Chat History**: Persistent conversation tracking

### ⚙️ **Configuration**
- **Advanced Editor**: JSON-based configuration editing
- **Validation**: Real-time configuration validation
- **Import/Export**: Save and load project configurations

### 📤 **Export & Deploy**
- **Project Charter**: Auto-generated markdown documentation
- **Technical Specs**: Detailed technical specifications
- **Python Config**: Generated configuration files
- **Deployment Files**: Docker, requirements.txt, and deployment scripts

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- Virtual environment (recommended)

### Quick Start

1. **Install Dependencies**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using the project's uv setup
   make setup
   make devtools
   ```

2. **Install Streamlit Dependencies**
   ```bash
   pip install streamlit pyyaml
   ```

3. **Run the Application**
   ```bash
   # Option 1: Using the script
   ./run_streamlit.sh
   
   # Option 2: Using make
   make streamlit
   
   # Option 3: Direct streamlit command
   streamlit run streamlit_app.py
   ```

4. **Access the Application**
   - Open your browser to `http://localhost:8501`
   - The application will automatically open

## 📱 How to Use

### 1. **Start with Dashboard**
- Fill in your project name and problem statement
- Navigate through the tabs to complete each section:
  - **Users & Interaction**: Define who will use your system
  - **Architecture**: Select system components and tech stack
  - **Constraints & Metrics**: Set budget and success criteria
  - **Timeline**: Plan your project phases

### 2. **Use Interactive Chat**
- Ask questions about your project
- Use guided questions to explore different aspects
- Chat responses will help clarify requirements
- Conversations are saved for reference

### 3. **Configure Advanced Settings**
- Edit the JSON configuration directly for fine-tuning
- Validate your configuration in real-time
- Load and save different project configurations

### 4. **Export Your Project**
- Generate project charter documents
- Create technical specifications
- Generate Python configuration files
- Create deployment files (Docker, requirements.txt)

## 🎯 Charter Template Integration

The application is built around the structured charter template methodology:

### **Part A: Project Concept Definition**
- Guided AI dialog to clarify project purpose
- User needs analysis
- Constraint identification

### **Part B: Detailed Q&A Checklist**
- Problem definition & goals
- User analysis
- Interaction & interface design
- System architecture & components
- Constraints & requirements
- Success metrics & KPIs
- Timeline & milestones

### **Part C: Implementation Preparation**
- Structured configuration output
- Ready-to-use technical specifications
- Deployment-ready files

## 💾 Session State Management

The application uses Streamlit's session state to maintain:

- **Project Configuration**: All form inputs and selections
- **Chat History**: Complete conversation logs
- **Progress Tracking**: Section completion status
- **Current Section**: Navigation state

Data persists throughout your session and can be saved/loaded as needed.

## 📁 Generated Files

The application can generate several types of files:

### **Documentation**
- `docs/generated_charter.md` - Complete project charter
- `docs/technical_spec.md` - Technical specifications

### **Configuration**
- `src/config.py` - Python configuration file
- `configs/project_config_*.json` - Session configurations
- `configs/project_config_*.yaml` - YAML configurations (if PyYAML available)

### **Deployment**
- `Dockerfile` - Container deployment
- `requirements.txt` - Python dependencies

## 🔧 Customization

### **Adding New Question Categories**
Edit the `planning_questions` dictionary in the Interactive Chat section:

```python
planning_questions = {
    "Your Category": [
        "Your question 1",
        "Your question 2",
        # Add more questions
    ]
}
```

### **Modifying AI Responses**
Update the `generate_ai_response()` function to add new keywords and responses.

### **Adding Export Formats**
Create new generator functions following the pattern of `generate_project_charter()`.

## 🎨 UI Components

- **Multi-page Navigation**: Sidebar-based page selection
- **Tabbed Interface**: Organized form sections
- **Progress Indicators**: Visual completion tracking
- **Chat Interface**: Interactive conversation UI
- **Code Editors**: Syntax-highlighted configuration editing

## 🚨 Troubleshooting

### **Common Issues**

1. **Streamlit not found**
   ```bash
   pip install streamlit
   ```

2. **YAML export not working**
   ```bash
   pip install pyyaml
   ```

3. **Session state not persisting**
   - Check if you're refreshing the page
   - Use the "Save Progress" button

4. **Configuration validation errors**
   - Fill in all required fields
   - Check the Configuration page for details

## 🎯 Integration with Project Structure

The Streamlit app integrates seamlessly with the project bootstrap structure:

```
AI_New_Project/
├── streamlit_app.py          # Main Streamlit application
├── run_streamlit.sh          # Quick launch script
├── requirements.txt          # Dependencies
├── configs/                  # Generated configurations
├── docs/                     # Generated documentation
├── src/                      # Source code (including generated config.py)
└── makefile                  # Build commands (make streamlit)
```

## 📚 Next Steps

After using the charter tool:

1. **Review Generated Files**: Check the exported documentation and configs
2. **Customize Configuration**: Modify `src/config.py` as needed
3. **Implement Features**: Start building based on your charter
4. **Iterate**: Return to the tool to refine your project definition

## 🎉 Benefits

- **Structured Planning**: Follow proven project charter methodology
- **Interactive Guidance**: AI-powered questions and responses
- **Visual Progress**: See completion status at a glance
- **Export Ready**: Generate professional documentation
- **Session Persistence**: Don't lose your work
- **Deployment Ready**: Get Docker and config files instantly

Perfect for AI project planning, requirements gathering, and technical specification creation!
