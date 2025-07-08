#!/bin/bash

# 🎯 AI Project Charter Tool Demo
# This script demonstrates the complete workflow from setup to deployment

set -e  # Exit on any error

echo "🎯 AI Project Charter Tool - Complete Demo"
echo "=========================================="
echo ""

# Function to print section headers
print_section() {
    echo ""
    echo "🔥 $1"
    echo "$(printf '=%.0s' {1..50})"
}

# Function to pause for user input
pause_for_user() {
    echo ""
    echo "⏸️  Press Enter to continue..."
    read
}

# Check if we're in the project directory
if [ ! -f "streamlit_app.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    echo "   (The directory containing streamlit_app.py)"
    exit 1
fi

print_section "Step 1: Environment Setup"
echo "📋 Checking Python environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+' | head -1)
echo "✅ Python version: $python_version"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "🔧 Creating virtual environment..."
    make setup
else
    echo "✅ Virtual environment already exists"
fi

# Install dependencies
echo "📦 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    . .venv/bin/activate && pip install -r requirements.txt
else
    . .venv/bin/activate && pip install streamlit pyyaml
fi

echo "✅ Environment setup complete!"
pause_for_user

print_section "Step 2: Project Structure"
echo "📁 Current project structure:"
echo ""
ls -la | grep -E "(streamlit|config|docs|src|tests|makefile|README)" | head -10
echo ""

echo "🏗️ Key files for the charter tool:"
echo "   📄 streamlit_app.py        - Main Streamlit application"
echo "   📄 run_streamlit.sh        - Quick launch script"
echo "   📄 requirements.txt        - Dependencies"
echo "   📄 STREAMLIT_README.md     - Detailed documentation"
echo "   📄 example_usage.py        - Usage examples"
echo "   📁 configs/                - Generated configurations (will be created)"
echo "   📁 docs/                   - Generated documentation"

pause_for_user

print_section "Step 3: Launch Charter Tool"
echo "🚀 Starting the AI Project Charter Tool..."
echo ""
echo "The Streamlit application will:"
echo "   🎯 Guide you through project planning"
echo "   📊 Track your progress with a visual dashboard"
echo "   🤖 Provide AI-powered planning assistance"
echo "   📤 Export configuration files and documentation"
echo ""
echo "📱 The app will open in your browser at http://localhost:8501"
echo "🛑 Press Ctrl+C in the terminal to stop the application"
echo ""

echo "⚡ Starting in 3 seconds..."
sleep 1 && echo "3..." && sleep 1 && echo "2..." && sleep 1 && echo "1..." && sleep 1

# Launch Streamlit
echo "🎯 Launching Charter Tool..."
echo ""
. .venv/bin/activate && streamlit run streamlit_app.py --server.port=8501 &
STREAMLIT_PID=$!

echo "🔥 Streamlit is running with PID: $STREAMLIT_PID"
echo ""
echo "📖 Usage Instructions:"
echo "   1. Open http://localhost:8501 in your browser"
echo "   2. Fill out the Dashboard sections"
echo "   3. Use the Interactive Chat for guidance"
echo "   4. Export your configuration when complete"
echo "   5. Press Ctrl+C here to stop the application"
echo ""

# Wait for user to stop
wait $STREAMLIT_PID

print_section "Step 4: Post-Charter Analysis"
echo "🔍 Analyzing generated files..."

# Check for generated configs
if [ -d "configs" ] && [ "$(ls -A configs)" ]; then
    echo "✅ Configuration files generated:"
    ls -la configs/ | head -5
else
    echo "ℹ️  No configuration files found (yet)"
    echo "   💡 Run the Streamlit app and export a configuration first"
fi

# Check for generated docs
if [ -d "docs" ] && [ "$(ls -A docs)" ]; then
    echo "✅ Documentation files generated:"
    ls -la docs/ | head -5
else
    echo "ℹ️  No documentation files found (yet)"
    echo "   💡 Use the Export & Deploy page to generate documentation"
fi

# Check for Python config
if [ -f "src/config.py" ]; then
    echo "✅ Python configuration file generated:"
    echo "   📄 src/config.py"
else
    echo "ℹ️  No Python config file found (yet)"
    echo "   💡 Use the Export & Deploy page to generate Python config"
fi

pause_for_user

print_section "Step 5: Usage Examples"
echo "🎓 Running usage examples..."

if [ -f "example_usage.py" ]; then
    echo "📋 Example output:"
    echo ""
    . .venv/bin/activate && python example_usage.py
else
    echo "❌ Example file not found"
fi

pause_for_user

print_section "Step 6: Next Steps"
echo "🚀 Your AI project charter tool is ready!"
echo ""
echo "📚 What you can do next:"
echo "   1. 🎯 Re-run the charter tool: make streamlit"
echo "   2. 📖 Read the documentation: cat STREAMLIT_README.md"
echo "   3. 🔧 Customize the configuration: edit src/config.py"
echo "   4. 🏗️ Build your project: make run"
echo "   5. 📤 Deploy your application: docker build -t your-app ."
echo ""
echo "📁 Key directories:"
echo "   📂 configs/    - Your saved project configurations"
echo "   📂 docs/       - Generated documentation and specs"
echo "   📂 src/        - Application source code"
echo "   📂 tests/      - Test files"
echo ""
echo "🎯 Charter Tool Commands:"
echo "   make streamlit      - Run the charter tool"
echo "   make help          - Show all available commands"
echo "   ./run_streamlit.sh - Alternative launch method"
echo ""
echo "🎉 Demo complete! Happy project planning!"
echo ""
echo "💡 Pro Tips:"
echo "   • Save your progress frequently using the sidebar"
echo "   • Use the Interactive Chat for guidance"
echo "   • Export configurations before closing the app"
echo "   • The generated files integrate with your project structure"
echo ""
echo "📞 Need help? Check STREAMLIT_README.md for detailed instructions"
