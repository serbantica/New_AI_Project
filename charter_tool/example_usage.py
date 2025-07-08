"""
Example usage of the AI Project Charter Tool generated configurations
This file demonstrates how to use the exported configurations in your project
"""

import json
import os
from pathlib import Path

# Example: Load and use a generated configuration
def load_project_config(config_path: str | None = None):
    """Load project configuration from the charter tool"""
    
    if config_path is None:
        # Find the most recent config file
        config_dir = Path("configs")
        if config_dir.exists():
            config_files = list(config_dir.glob("project_config_*.json"))
            if config_files:
                config_path = str(max(config_files, key=os.path.getctime))
            else:
                print("No configuration files found in configs/")
                return None
        else:
            print("No configs directory found")
            return None
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        print(f"✅ Loaded configuration from {config_path}")
        return config
    
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        return None

# Example: Use configuration in your application
def use_project_config():
    """Demonstrate how to use the loaded configuration"""
    
    config = load_project_config()
    
    if config is None:
        print("No configuration available. Please run the Streamlit charter tool first.")
        return
    
    print("\n🎯 Project Configuration Summary")
    print("=" * 50)
    
    # Basic project info
    print(f"📛 Project Name: {config.get('project_name', 'Not set')}")
    print(f"📝 Problem Statement: {config.get('problem_statement', 'Not set')}")
    
    # Users and interaction
    users = config.get('users', [])
    if users:
        print(f"👥 Target Users: {', '.join(users)}")
    
    interactions = config.get('interaction_patterns', [])
    if interactions:
        print(f"🔄 Interaction Patterns: {', '.join(interactions)}")
    
    # Architecture
    components = config.get('system_components', [])
    if components:
        print(f"🏗️ System Components: {', '.join(components)}")
    
    tech_stack = config.get('tech_stack', 'Not set')
    print(f"💻 Technology Stack: {tech_stack}")
    
    # Constraints and metrics
    constraints = config.get('constraints', {})
    if constraints:
        print(f"💰 Budget: €{constraints.get('budget', 0)}/month")
        print(f"⚡ Performance: {constraints.get('performance', 'Not set')}")
        compliance = constraints.get('compliance', [])
        if compliance:
            print(f"📋 Compliance: {', '.join(compliance)}")
    
    metrics = config.get('success_metrics', {})
    if metrics:
        print(f"📊 Efficiency Gain Target: {metrics.get('efficiency_gain', 0)}%")
        print(f"🎯 Accuracy Target: {metrics.get('accuracy_target', 0)}%")
        print(f"👥 User Adoption Target: {metrics.get('user_adoption', 0)} users")
    
    # Timeline
    timeline = config.get('timeline', {})
    if timeline:
        print(f"📅 Start Date: {timeline.get('start_date', 'Not set')}")
        print(f"🏁 End Date: {timeline.get('end_date', 'Not set')}")
        phases = timeline.get('phases', [])
        if phases:
            print(f"📊 Phases: {', '.join(phases)}")
    
    # Progress tracking
    completion_status = config.get('completion_status', {})
    completed_sections = sum(1 for status in completion_status.values() if status)
    total_sections = 7  # Total sections in the charter
    completion_percentage = (completed_sections / total_sections) * 100
    print(f"✅ Completion: {completion_percentage:.0f}% ({completed_sections}/{total_sections} sections)")
    
    return config

# Example: Initialize your application with the configuration
def initialize_app_with_config():
    """Example of how to initialize your application using the charter configuration"""
    
    config = load_project_config()
    
    if config is None:
        print("❌ No configuration found. Please run: make streamlit")
        return
    
    # Example: Set up logging based on project name
    project_name = config.get('project_name', 'ai-project')
    log_file = f"logs/{project_name.lower().replace(' ', '_')}.log"
    
    # Example: Configure database based on constraints
    constraints = config.get('constraints', {})
    budget = constraints.get('budget', 500)
    
    if budget < 100:
        db_config = "sqlite:///local.db"  # Low budget = local database
    elif budget < 500:
        db_config = "postgresql://localhost/dev"  # Medium budget = local PostgreSQL
    else:
        db_config = "postgresql://cloud-instance/prod"  # High budget = cloud database
    
    # Example: Set up performance monitoring based on requirements
    performance_req = constraints.get('performance', '< 2 sec')
    if '< 1 sec' in performance_req:
        monitoring_level = "high"
    elif '< 2 sec' in performance_req:
        monitoring_level = "medium"
    else:
        monitoring_level = "low"
    
    # Example: Configure features based on user types
    users = config.get('users', [])
    features = {
        'technical_interface': 'Technical Users' in users,
        'business_dashboard': 'Business Users' in users,
        'admin_panel': 'Administrators' in users,
        'analytics': 'Analysts' in users
    }
    
    print(f"\n🚀 Application Configuration")
    print("=" * 30)
    print(f"📝 Log File: {log_file}")
    print(f"🗄️ Database: {db_config}")
    print(f"📊 Monitoring Level: {monitoring_level}")
    print(f"🎛️ Features: {', '.join([k for k, v in features.items() if v])}")
    
    return {
        'project_name': project_name,
        'log_file': log_file,
        'database_url': db_config,
        'monitoring_level': monitoring_level,
        'features': features,
        'original_config': config
    }

# Example: Generate application structure based on configuration
def generate_app_structure():
    """Generate application structure based on the charter configuration"""
    
    config = load_project_config()
    
    if config is None:
        print("❌ No configuration found. Please run the Streamlit charter tool first.")
        return
    
    project_name = config.get('project_name', 'ai-project')
    components = config.get('system_components', [])
    
    # Create directory structure based on selected components
    directories = ['src', 'tests', 'docs', 'configs']
    
    for component in components:
        if component == 'Data Ingestion':
            directories.append('src/data_ingestion')
        elif component == 'Data Processing':
            directories.append('src/data_processing')
        elif component == 'ML Models':
            directories.append('src/models')
        elif component == 'API Gateway':
            directories.append('src/api')
        elif component == 'User Interface':
            directories.append('src/ui')
        elif component == 'Database':
            directories.append('src/database')
        elif component == 'Monitoring':
            directories.append('src/monitoring')
        elif component == 'Authentication':
            directories.append('src/auth')
    
    print(f"\n📁 Recommended Directory Structure for {project_name}")
    print("=" * 50)
    
    for directory in sorted(set(directories)):
        print(f"📂 {directory}/")
    
    return directories

if __name__ == "__main__":
    print("🎯 AI Project Charter Tool - Configuration Usage Example")
    print("=" * 60)
    
    # Load and display configuration
    use_project_config()
    
    # Initialize app with configuration
    app_config = initialize_app_with_config()
    
    # Generate recommended structure
    generate_app_structure()
    
    print("\n💡 Next Steps:")
    print("1. Run 'make streamlit' to configure your project")
    print("2. Use the generated configuration files in your application")
    print("3. Implement the features based on your charter")
    print("4. Deploy using the generated Docker/requirements files")
