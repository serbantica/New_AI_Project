#!/bin/bash

# 🚀 AI Project Charter Tool Runner
# This script runs the Streamlit application from the project root.

echo "🎯 Starting AI Project Charter Tool..."
echo "🔧 Make sure you have all dependencies installed:"
echo "   pip install -r requirements.txt"
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed. Installing..."
    pip install streamlit pyyaml
fi

# Define the path to the app
APP_PATH="charter_tool/streamlit_app.py"

# Check if we're in the right directory
if [ ! -f "$APP_PATH" ]; then
    echo "❌ $APP_PATH not found. Make sure you're running this from the project root directory."
    exit 1
fi

echo "🚀 Launching Streamlit application..."
echo "📱 The app will open in your browser at http://localhost:8502"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

# Run the Streamlit app, specifying the path
# This ensures that relative paths inside the app (like 'configs/' or 'docs/') still work from the root
streamlit run "$APP_PATH" --server.port=8502 --server.address=0.0.0.0